import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return math.pi * self.radio ** 2
    
    def perimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return self.lado ** 2
    
    def perimetro(self):
        return 4 * self.lado

class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return (self.base * self.altura) / 2
    
    def perimetro(self):
        return self.base + self.altura + math.sqrt(self.base ** 2 + self.altura ** 2)
    
    def hipotenusa(self):
        return math.sqrt(self.base ** 2 + self.altura ** 2)
    
    def tipo_triangulo(self):
        if self.base == self.altura:
            return "Equil�tero"
        elif self.base == self.hipotenusa() or self.altura == self.hipotenusa():
            return "Is�sceles"
        else:
            return "Escaleno"

if __name__ == "__main__":
    circulo = Circulo(5)
    print("C�rculo de radio 5:")
    print("�rea:", circulo.area())
    print("Per�metro:", circulo.perimetro())
    
    rectangulo = Rectangulo(3, 4)
    print("Rect�ngulo de base 3 y altura 4:")
    print("�rea:", rectangulo.area())
    print("Per�metro:", rectangulo.perimetro())
    
    cuadrado = Cuadrado(5)
    print("Cuadrado de lado 5:")
    print("�rea:", cuadrado.area())
    print("Per�metro:", cuadrado.perimetro())
    
    triangulo = TrianguloRectangulo(3, 4)
    print("Tri�ngulo rect�ngulo de base 3 y altura 4:")
    print("�rea:", triangulo.area())
    print("Per�metro:", triangulo.perimetro())
    print("Hipotenusa:", triangulo.hipotenusa())
    print("Tipo de tri�ngulo:", triangulo.tipo_triangulo())