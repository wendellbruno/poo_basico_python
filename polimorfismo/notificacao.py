from abc import ABC, abstractmethod

class Notificacao(ABC):

    def __init__(self, msg) -> None:
        self.msg = msg

    @abstractmethod
    def enviar(self) -> bool: ...



class NotificacaoEmail(Notificacao):

    def enviar(self) -> bool:
        print('E-mail: envinado:', self.msg)
        return True



class NotificacaoSMS(Notificacao):

    def enviar(self) -> bool:
        print('SMS: envinado:', self.msg)
        return False




def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação enviada')
    else:
        print('Notificação NÃO enviada')



notificacao_email = NotificacaoEmail('testando e-mail')
notificar(notificacao_email)

notificacao_SMS = NotificacaoSMS('testando SMS')
notificar(notificacao_SMS)

