from empleado import Empleado
from area import Area

class Gerente(Empleado, Area):
    def __init__(self):
        super().__init__()
        super().__init__()
        self._proyetos = ""
        self._presupuesto_area = 0

    # Getter y Setter
    def get_proyectos(self):
            return self._proyetos

    def set_proyectos(self, proyectos):
        self._proyetos = proyectos

    def get_presupuesto_area(self):
        return self._presupuesto_area

    def set_presupuesto_area(self, presupuesto_area):
        self._presupuesto_area = presupuesto_area

    def mostrar_informacion(self):
        base_info_empleado = super(Empleado, self).mostrar_informacion()
        base_info_area = super(Area, self).mostrar_informacion()
        return f"{base_info_empleado}, Area: {base_info_area} Proyectos: {self.get_proyectos()}, Presupuesto del Area: {self.get_presupuesto_area()}"
