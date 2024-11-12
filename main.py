from director import Director
from gerente import Gerente
from jefearea import JefeArea


def main():
    director = Director()
    director.set_nombre("Johanna")
    director.set_apellido("Xwomen")
    director.set_edad(40)
    director.set_cargo("Director")
    director.set_sueldo(120000)
    director.set_nomina("BBVA")
    director.set_nombre_departamento("Contabilidad")
    director.set_direccion("Edificio A")
    director.set_codigo_departamento("123456")
    director.set_nombre_area("Finanzas")
    director.set_codigo_area("7890")
    director.set_especializacion("Analisis de Costos")
    director.set_region("Sur")
    director.set_vision_estrategica("Ser un área clave en la transformación organizacional")
    director.set_presupuesto_total(500000)

    gerente = Gerente()
    gerente.set_nombre("Carlos")
    gerente.set_apellido("Hernandez")
    gerente.set_edad(32)
    gerente.set_cargo("Gerente")
    gerente.set_sueldo(80000)
    gerente.set_nomina("BBVA")
    gerente.set_nombre_departamento("Contabilidad")
    gerente.set_direccion("Edificio A")
    gerente.set_codigo_departamento("123456")
    gerente.set_nombre_area("Finanzas")
    gerente.set_codigo_area("7890")
    gerente.set_especializacion("Analisis de Costos")
    gerente.set_proyectos("Implementación de una nueva plataforma de reclutamiento digital")
    gerente.set_presupuesto_area(200000)

    jefearea = JefeArea()
    jefearea.set_nombre("Ana")
    jefearea.set_apellido("Ramirez")
    jefearea.set_edad(26)
    jefearea.set_cargo("Jefe de Area")
    jefearea.set_sueldo(55000)
    jefearea.set_nomina("BBVA")
    jefearea.set_nombre_departamento("Contabilidad")
    jefearea.set_direccion("Edificio A")
    jefearea.set_codigo_departamento("123456")
    jefearea.set_nombre_area("Finanzas")
    jefearea.set_codigo_area("7890")
    jefearea.set_especializacion("Analisis de Costos")
    jefearea.set_subarea("Administración de Personal")
    jefearea.set_capacitacion_equipo("Programa trimestral de actualización en normativas laborales")

    print("Director:")
    print(director.mostrar_informacion())

    print("\nGerente:")
    print(gerente.mostrar_informacion())

    print("\nJefeArea:")
    print(jefearea.mostrar_informacion())

if __name__ == "__main__":
    main()
