class Carro:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._motor = None
        self._fabricante = None
    
    
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, nomeMotor):
         self._motor = nomeMotor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, nomeFabricante):
        self._fabricante = nomeFabricante

    def montarCarro(self):
        return f'{self.nome} usa o motor : {self.motor} e seu fabricante é {self.fabricante}'



class Motor:
    def __init__(self, nomeMotor) -> None:
        self.nomeMotor= nomeMotor




class Fabriante:
    def __init__(self, nomeFabricante) -> None:
        self.nomeFabricante = nomeFabricante


fabricante1 = Fabriante('fiat')
motor1 = Motor('v8')
carro1 = Carro('UNO')
carro1.fabricante = fabricante1
carro1.motor = motor1
print(carro1.nome, carro1.fabricante, carro1.motor)
