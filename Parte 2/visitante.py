class Visitante:
    def __init__(self, nombre, hora_entrada, permanencia):
        self.nombre = nombre
        self.hora_entrada = int(hora_entrada)
        self.permanencia = int(permanencia)
        self.hora_salida = self.hora_entrada + self.permanencia
