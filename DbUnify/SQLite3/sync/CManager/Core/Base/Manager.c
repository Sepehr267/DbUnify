#include <stdio.h>
#include <stdlib.h>
#include <sqlite3.h>
#include <string.h>
#include "cache.h"

int connect_db(sqlite3 **db, const char *db_name);
void close_db(sqlite3 *db);
int execute_query(sqlite3 *db, const char *query, sqlite3_callback callback, void *data);
int create_table(sqlite3 *db, const char *table_name, const char *columns);
int drop_table(sqlite3 *db, const char *table_name);
int add_column(sqlite3 *db, const char *table_name, const char *column_name, const char *data_type, const char *constraints);
int insert_row(sqlite3 *db, const char *table_name, const char *values);
int delete_row(sqlite3 *db, const char *table_name, const char *condition);
int update_row(sqlite3 *db, const char *table_name, const char *values, const char *condition);
int get_table_columns(sqlite3 *db, const char *table_name);
int fetch_all(sqlite3 *db, const char *query, sqlite3_callback callback, void *data);

int connect_db(sqlite3 **db, const char *db_name) {
    if (sqlite3_open(db_name, db)) {
        fprintf(stderr, "Can't open database: %s\n", sqlite3_errmsg(*db));
        return EXIT_FAILURE;
    }
    init_cache();
    return EXIT_SUCCESS;
}

void close_db(sqlite3 *db) {
    sqlite3_close(db);
    free_cache();
}

int execute_query(sqlite3 *db, const char *query, sqlite3_callback callback, void *data) {
    char *err_msg = NULL;
    int rc = sqlite3_exec(db, query, callback, data, &err_msg);
    if (rc != SQLITE_OK) {
        fprintf(stderr, "SQL error: %s\n", err_msg);
        sqlite3_free(err_msg);
    }
    return rc;
}

int create_table(sqlite3 *db, const char *table_name, const char *columns) {
    size_t query_size = strlen(table_name) + strlen(columns) + 50;
    char *query = (char *)malloc(query_size);
    if (!query) {
        fprintf(stderr, "Memory allocation failed\n");
        return EXIT_FAILURE;
    }
    snprintf(query, query_size, "CREATE TABLE %s (%s);", table_name, columns);
    int result = execute_query(db, query, NULL, NULL);
    free(query);
    return result;
}

int drop_table(sqlite3 *db, const char *table_name) {
    size_t query_size = strlen(table_name) + 30;
    char *query = (char *)malloc(query_size);
    if (!query) {
        fprintf(stderr, "Memory allocation failed\n");
        return EXIT_FAILURE;
    }
    snprintf(query, query_size, "DROP TABLE IF EXISTS %s;", table_name);
    int result = execute_query(db, query, NULL, NULL);
    free(query);
    return result;
}

int add_column(sqlite3 *db, const char *table_name, const char *column_name, const char *data_type, const char *constraints) {
    size_t query_size = strlen(table_name) + strlen(column_name) + strlen(data_type) + strlen(constraints) + 50;
    char *query = (char *)malloc(query_size);
    if (!query) {
        fprintf(stderr, "Memory allocation failed\n");
        return EXIT_FAILURE;
    }
    snprintf(query, query_size, "ALTER TABLE %s ADD COLUMN %s %s %s;", table_name, column_name, data_type, constraints);
    int result = execute_query(db, query, NULL, NULL);
    free(query);
    return result;
}

int insert_row(sqlite3 *db, const char *table_name, const char *values) {
    size_t query_size = strlen(table_name) + strlen(values) + 30;
    char *query = (char *)malloc(query_size);
    if (!query) {
        fprintf(stderr, "Memory allocation failed\n");
        return EXIT_FAILURE;
    }
    snprintf(query, query_size, "INSERT INTO %s VALUES (%s);", table_name, values);
    cache_set(query, "");
    int result = execute_query(db, query, NULL, NULL);
    free(query);
    return result;
}

int delete_row(sqlite3 *db, const char *table_name, const char *condition) {
    size_t query_size = strlen(table_name) + strlen(condition) + 30;
    char *query = (char *)malloc(query_size);
    if (!query) {
        fprintf(stderr, "Memory allocation failed\n");
        return EXIT_FAILURE;
    }
    snprintf(query, query_size, "DELETE FROM %s WHERE %s;", table_name, condition);
    cache_set(query, "");
    int result = execute_query(db, query, NULL, NULL);
    free(query);
    return result;
}

int update_row(sqlite3 *db, const char *table_name, const char *values, const char *condition) {
    size_t query_size = strlen(table_name) + strlen(values) + strlen(condition) + 50;
    char *query = (char *)malloc(query_size);
    if (!query) {
        fprintf(stderr, "Memory allocation failed\n");
        return EXIT_FAILURE;
    }
    snprintf(query, query_size, "UPDATE %s SET %s WHERE %s;", table_name, values, condition);
    cache_set(query, "");
    int result = execute_query(db, query, NULL, NULL);
    free(query);
    return result;
}

int get_table_columns(sqlite3 *db, const char *table_name) {
    size_t query_size = strlen(table_name) + 30;
    char *query = (char *)malloc(query_size);
    if (!query) {
        fprintf(stderr, "Memory allocation failed\n");
        return EXIT_FAILURE;
    }
    snprintf(query, query_size, "PRAGMA table_info(%s);", table_name);
    int result = execute_query(db, query, NULL, NULL);
    free(query);
    return result;
}

int fetch_all(sqlite3 *db, const char *query, sqlite3_callback callback, void *data) {
    return execute_query(db, query, callback, data);
}
