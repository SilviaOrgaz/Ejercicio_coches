class Vehiculo:

    def __init__(self, col, n_ruedas):
        self.color = col
        self.ruedas = n_ruedas

    def __str__(self):
        return "El color del vehículo es {} y el número de ruedas es {}".format(self.color, self.ruedas)

class Coche(Vehiculo):

    def __init__(self, vel, cil, col, n_ruedas):
        super().__init__(col, n_ruedas)
        self.velocidad = vel
        self.cilindrada = cil

    def __str__(self):
        return super().__str__ ()+ "\n" + "La velocidad del vehículo es {} km/h y cilindrada {} cc".format(self.velocidad, self.cilindrada)

class Camioneta(Coche):
    def __init__(self, carga, vel, cil, col, n_ruedas):
        super().__init__(vel, cil, col, n_ruedas)
        self.carga = carga
    
    def __str__(self):
        return super().__str__() + "\n" + "La carga del camión es de {} kg".format(self.carga)

    

        
A = Vehiculo("rojo", 5)
print(A)
B= Coche(100, 50, "azul", 4)
print(B)
C= Camioneta(1000, 200, 60, "negro", 6)
print(C)
