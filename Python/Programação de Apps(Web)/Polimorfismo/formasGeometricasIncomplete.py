class FormaGeometrica:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    def area(self):raise NotImplementedError("Subclasse deve implementar método abstrato!")
    
class Retangulo(FormaGeometrica):
    def __init__(self,base,altura):
        super().__init__(base,altura)
    def area(self):
        return self.base * self.altura
    
class Triangulo(FormaGeometrica):
    def __init__(self,base,altura):
        super().__init__(base,altura)
    def area(self):
        return (self.base * self.altura)/2
    
class Circulo(FormaGeometrica):
    def __init__(self,raio):
        self.raio=raio
    def area(self):
        return 3.14 * self.raio**2
    
ret= Retangulo(4,5)
cir= Circulo(4)
tri= Triangulo(6,2)
print(ret.calcArea())
print(cir.calcArea())
print(tri.calcArea())

def calcArea(forma):
    print(forma.area())