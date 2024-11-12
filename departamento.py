class Departamento:
    def __init__(self):
        self._nombre_departamento = ""
        self._direccion = ""
        self._codigo_departamento = ""

    # Getter y Setter
    def get_nombre_departamento(self):
        return self._nombre_departamento

    def set_nombre_departamento(self, nombre_departamento):
        self._nombre_departamento = nombre_departamento

    def get_direccion(self):
        return self._direccion

    def set_direccion(self, direccion):
        self._direccion = direccion

    def get_codigo_departamento(self):
        return self._codigo_departamento

    def set_codigo_departamento(self, codigo_departamento):
        self._codigo_departamento = codigo_departamento

    def mostrar_informacion(self):
        return f"Departamento: {self._nombre_departamento}, Dirección: {self._direccion}, Codigo de Departamento: {self._codigo_departamento}"
