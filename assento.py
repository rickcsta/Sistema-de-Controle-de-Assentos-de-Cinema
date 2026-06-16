class Assento:
    def __init__(self, fileira, numero):
        self.fileira = fileira
        self.numero = numero
        self.ocupado = False
        self.comprador = ""

    def coordenada(self):
        return f"{self.fileira}{self.numero}"

    def __str__(self):
        if self.ocupado:
            return f"{self.coordenada()} - Ocupado por {self.comprador}"
        else:
            return f"{self.coordenada()} - Disponível"

    def linha_armazenamento(self):
        return f"{self.fileira}:{self.numero}:{self.ocupado}:{self.comprador}"