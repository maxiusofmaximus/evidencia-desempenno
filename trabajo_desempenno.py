# Construye dos superclases, donde una será la clase empleados
# que pida en consola el nombre del empleado en un metodo de instancia. 

# La segunda clase será salario que pida  en consola el
# salario del empleado en un metodo de instancia.

# Cree una clase hija llamada Designación que herede las
# dos clases anteriores y que tenga un metodo de instancia 
# que designe el cargo del empleado.

# Verifique el codigo, instanciando un objeto de la clase hija,
# verificacndo si el objeto tiene el metodo nombre y salario.


# este es el ejercicio para la activdad Desempenno
class Empleados:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}\n"


class Salario:
    def __init__(self, salario):
        self.salario = salario

    def __str__(self) -> str:
        return f"Salario: {str(self.salario)}\n"
    

class Designacion(Empleados, Salario):
    def __init__(self, nombre, salario, cargo):
        Empleados.__init__(self, nombre)
        Salario.__init__(self, salario)
        self.cargo = cargo

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}\nSalario: {self.salario}\nCargo: {self.cargo}\n"
    

def nombre() -> str: return input("Ingrese el nombre del empleado: ")
def salario() -> float: return float(input("Ingrese el salario del empleado: "))
def cargo() -> str: return input("Ingrese el cargo del empleado: ")


empleado = Designacion(nombre(), salario(), cargo())
print(str(empleado))