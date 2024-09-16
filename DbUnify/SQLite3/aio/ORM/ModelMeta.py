from .Field import Field

class ModelMeta(type):

    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return super().__new__(cls, name, bases, attrs)
        
        fields = {k: v for k, v in attrs.items() if isinstance(v, Field)}
        for field_name in fields.keys():
            attrs.pop(field_name)

        new_class = super().__new__(cls, name, bases, attrs)
        new_class._fields = fields
        
        return new_class
