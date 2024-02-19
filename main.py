class Asiento:
    def __init__(self, color, precio, registro):
            self.color = color
            self.precio = precio
            self.registro = registro

    def cambiarColor(self, opciones):
        if opciones == "rojo" or opciones == "verde" or opciones == "amarillo" or opciones == "negro" or opciones == "blanco":
            self.color = opciones


class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, numero):
        self.registro = int(numero)

    def asignarTipo(self, asignar):
        if asignar == "electrico" or asignar == "gasolina":
            self.tipo = asignar


class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        contador = 0
        for i in self.asientos:
            if isinstance(i, Asiento) == True:
                contador += 1
        return contador
    
    def verificarIntegridad(self):
        for i in self.asientos:
            if isinstance(i, Asiento) == True:
                if self.registro != i.registro:
                    return "Las piezas no son originales"
        
        if self.registro != self.motor.registro:
            return "Las piezas no son originales"
        
        return "Auto original"