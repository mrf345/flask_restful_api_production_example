from sqlalchemy.orm.collections import InstrumentedList


class GenericMixin:
    '''Handy generic utility methods shared between models'''

    @classmethod
    def get(cls, id):
        '''Get first matching record.

        Parameters
        ----------
        id : int
            record's id.

        Returns
        -------
        SQLAlchemy Model Instance
            first record matches the id.
        '''
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_all(cls):
        ''' Get all records.

        Returns
        -------
        list
            find all matching records.
        '''
        return cls.query.all()

    @classmethod
    def get_module_columns(cls):
        ''' Retrieve SQLAlchemy module columns names.

        Returns
        -------
            List of module columns names.
        '''
        return [
            getattr(column, 'name', None)
            for column in getattr(getattr(cls, '__mapper__', None), 'columns', [])
            if getattr(column, 'name', None) != 'password_hash'
        ] + getattr(cls, 'props', [])

    def update(self, data):
        for key, value in data.items():
            if key not in getattr(self, 'props', []):
                setattr(self, key, value)

    def to_dict(self):
        dictted = {}

        for key in self.get_module_columns():
            value = getattr(self, key)
            dictted[key] =\
                [getattr(v, 'id', v) for v in value]\
                if type(value) is InstrumentedList else value

        return dictted


class NameMixin:
    @classmethod
    def get_by_name(cls, name):
        ''' Get first role by name.

        Parameters
        ----------
        name : str
            role's name to get by.

        Returns
        -------
        Role
            first role found.
        '''
        return cls.query.filter_by(name=name).first()
