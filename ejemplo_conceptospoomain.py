
# class Animal:
    def __init__(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def hacer_sonido(self):
        print("El animal hace un sonido genérico.")


class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.__raza = raza

    def get_raza(self):
        return self.__raza

    def set_raza(self, raza):
        self.__raza = raza

    def hacer_sonido(self):
        print("El perro ladra.")


# Crear instancias de las clases
animal_generico = Animal("Animal Genérico")
perro = Perro("Firulais", "Labrador")

# Probar la funcionalidad de las clases
print(animal_generico.get_nombre())  # Salida: "Animal Genérico"
animal_generico.hacer_sonido()  # Salida: "El animal hace un sonido genérico."

print(perro.get_nombre())  # Salida: "Firulais"
print(perro.get_raza())  # Salida: "Labrador"
perro.hacer_sonido()  # Salida: "El perro ladra."Online Python - IDE, Editor, Compiler, Interpreter

def sum(a, b):
    return (a + b)

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

print(f'Sum of {a} and {b} is {sum(a, b)}')
