from empleado import Empleado
from area import Area

class JefeArea(Empleado, Area):
    def __init__(self):
        super().__init__()
        super().__init__()
        self._subarea = ""
        self._capacitacion_equipo = ""

    # Getter y Setter
    def get_subarea(self):
            return self._subarea

    def set_subarea(self, subarea):
        self._subarea = subarea

    def get_capacitacion_equipo(self):
            return self._capacitacion_equipo

    def set_capacitacion_equipo(self, capacitacion_equipo):
        self._capacitacion_equipo = capacitacion_equipo

    def mostrar_informacion(self):
        base_info_empleado = super(Empleado, self).mostrar_informacion()
        base_info_area = super(Area, self).mostrar_informacion()
        return f"{base_info_empleado}, Area: {base_info_area} Su SubArea es: {self.get_subarea()}, Proxima capacitacion: {self.get_capacitacion_equipo()}"
