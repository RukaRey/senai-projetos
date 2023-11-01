class FormaGeometrica:
    def area(self):raise NotImplementedError("Subclasse deve implementar método abstrato!")
    
class Retangulo(FormaGeometrica):
    def area(self):
        return self.base * self.altura
    
class Triangulo(FormaGeometrica):
    def area(self):
        return (self.base * self.altura)/2
    
class Circulo(FormaGeometrica):
    def area(self):
        return 3.14 * self.raio**2
    
ret= Retangulo()
ret.base=10
ret.altura=5
cir= Circulo()
cir.raio=4
tri= Triangulo()
ret.base=13
ret.altura=3

def calcArea(forma):
    print(forma.area())

calcArea(ret)
calcArea(cir)
calcArea(tri)