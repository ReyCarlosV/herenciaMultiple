from empleado import Empleado
from area import Area

class Director(Empleado, Area):
    def __init__(self):
        super().__init__()
        super().__init__()
        self._region = ""
        self._vision_estrategica = ""
        self._presupuesto_total = 0

    # Getter y Setter
    def get_region(self):
            return self._region

    def set_region(self, region):
        self._region = region

    def get_vision_estrategica(self):
            return self._vision_estrategica

    def set_vision_estrategica(self, vision_estrategica):
        self._vision_estrategica = vision_estrategica

    def get_presupuesto_total(self):
        return self._presupuesto_total

    def set_presupuesto_total(self, presupuesto_total):
        self._presupuesto_total = presupuesto_total

    def mostrar_informacion(self):
        base_info_empleado = super(Empleado, self).mostrar_informacion()
        base_info_area = super(Area, self).mostrar_informacion()
        return f"{base_info_empleado}, Area: {base_info_area} La region del Director es: {self.get_region()}, y su Vision estrategica: {self.get_vision_estrategica()}, Presupuesto total: {self.get_presupuesto_total()}"
