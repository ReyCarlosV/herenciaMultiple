from departamento import Departamento

class Area(Departamento):
    def __init__(self):
        super().__init__()
        self._nombre_area = ""
        self._codigo_area = ""
        self._especializacion = ""

    # Getter y Setter
    def get_nombre_area(self):
        return self._nombre_area

    def set_nombre_area(self, nombre_area):
        self._nombre_area = nombre_area

    def get_codigo_area(self):
        return self._codigo_area

    def set_codigo_area(self, codigo_area):
        self._codigo_area = codigo_area

    def get_especializacion(self):
        return self._especializacion

    def set_especializacion(self, especializacion):
        self._especializacion = especializacion

    def mostrar_informacion(self):
        base_info = super().mostrar_informacion()
        return f"{base_info}, Area: {self._nombre_area}, Codigo de Area: {self._direccion}, Especializacion: {self._especializacion}"
