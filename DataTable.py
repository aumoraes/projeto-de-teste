from Column import Column

class DataTable:
    def __init__(self, name):
        self._name = name
        self._columns = []
        self._references = []
        self._referenced = []
        self._data = []

    def _get_name(self):
        print("Getter executado!")
        return self._name

    def _set_name(self, _name):
        print("Setter executado!")
        self._name = _name

    def _del_name(self):
        print("Deletter executado!")
        raise AttributeError("Não pode deletar esse atributo")

    name = property(_get_name, _set_name, _del_name)

    def add_column(self, name, kind, description=""):
        self._validate_kind(kind)
        column = Column(name, kind, description=description)
        self._columns.append(column)
        return column

    def _validate_kind(self, kind):
        if not kind in ('bigint', 'numeric', 'varchar'):
            raise Exception("Tipo inválido")