from persona import Persona

class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self._cargo = ""
        self._sueldo = 0
        self._nomina = ""

    # Getter y Setter
    def get_cargo(self):
            return self._cargo

    def set_cargo(self, cargo):
        self._cargo = cargo

    def get_sueldo(self):
            return self._sueldo

    def set_sueldo(self, sueldo):
        self._sueldo = sueldo

    def get_nomina(self):
            return self._nomina

    def set_nomina(self, nomina):
        self._nomina = nomina

    def mostrar_informacion(self):
        base_info = super().mostrar_informacion()
        return f"{base_info}, Cargo: {self._cargo}, Sueldo: {self._sueldo}, Nomina: {self._nomina}"
