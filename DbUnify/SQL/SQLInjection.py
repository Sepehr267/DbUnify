import re

class SQLInjection:
    def __init__(self):
        self.suspicious_patterns = [
            r"(?i)\bUNION\b\s+\bSELECT\b",
            r"(?i)\bOR\b\s+1\s*=\s*1\b",
            r"(?i)\bAND\b\s+1\s*=\s*1\b",
            r"(?i)\b--\b",
            r"(?i)\b;--\b",
            r"(?i)\b;?\s*DROP\b\s+\bTABLE\b",
            r"(?i)\bSELECT\b.*\bFROM\b.*\bWHERE\b.*\bOR\b",
            r"(?i)\bEXEC\b\s+\bXP_",
            r"(?i)\bSLEEP\b\(\d+\)",
            r"(?i)\bWAITFOR\b\s+DELAY\b",
            r"(?i)\bINFORMATION_SCHEMA\b",
            r"(?i)\bHAVING\b\s+\b1\b\s*=\s*\b1\b",
            r"(?i)\bSELECT\b\s+1\b\s*=\s*\b1\b",
            r"(?i)\bCONCAT\b\s*\(.*\)",
            r"(?i)\bBENCHMARK\b\s*\(\d+,.+\)",
            r"(?i)\bCAST\b\s*\(.+\bAS\b",
            r"(?i)\bCONVERT\b\s*\(.+\bUSING\b",
            r"(?i)\bSUBSTRING\b\s*\(.*\)",
            r"(?i)\bUPDATEXML\b\s*\(",
            r"(?i)\bEXTRACTVALUE\b\s*\(",
            r"(?i)\bATTACH\b\s+DATABASE\b",
            r"(?i)\bPRAGMA\b",
            r"(?i)\bSQLITE_MASTER\b",
            r"(?i)\bROWID\b",
            r"(?i)\bLIMIT\b\s+\d+\s*\bOFFSET\b\s*\d+",
            r"(?i)\bINSERT\b\s+INTO\b\s+SQLITE_",
            r"(?i)\bANALYZE\b\s+\bSQLITE_",
            r"(?i)\bVACUUM\b",
            r"(?i)\bUNION\b\s+SELECT\b.*\bFROM\b\s+DUAL\b",
            r"(?i)\bIF\b\s*\(\d+\s*=\s*\d+\)\s+WAITFOR\b\s+DELAY\b",
            r"(?i)\bDECLARE\b\s+@?\w+\s+INT\s*;\s+SET\b\s+@?\w+\s*=\s*\d+",
            r"(?i)\bEXEC\b\s+(\w+|@@)\s*\(",
        ]
        self.red_color_code = "\033[91m"
        self.reset_color_code = "\033[0m"

    def detect(self, query: str, *args) -> bool:
        """
        Detects if the given SQL query contains any suspicious patterns
        that could indicate a SQL injection attempt.

        :param query: The SQL query to analyze.
        :return: True if a suspicious pattern is detected, otherwise False.
        """
        query_temp = "{} {}".format(query, " ".join(map(str, args)))
        for pattern in self.suspicious_patterns:
            if re.search(pattern, query_temp):
                print(f'{self.red_color_code}[SQLINJ] Potential SQL injection detected. SQL Command: {query}, Parameters: {args}{self.reset_color_code}')
                return True
        return False