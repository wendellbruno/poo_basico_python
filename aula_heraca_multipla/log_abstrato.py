from pathlib import Path
from abc import ABC, abstractmethod

LOG_FILE = Path(__file__).parent / 'log.txt'

# Abstração
class Log(ABC):

    @abstractmethod
    def _log(self, msg): ...
        
    
    def logo_error(self, msg):
        return self._log(f'Error: {msg}')
    

    def logo_sucess(self, msg):
        return self._log(f'Sucess: {msg}')
    

class LogFileMixin(Log):

    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')

    
class LogPrintMixin(Log):
    
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        return print(msg_formatada)


if __name__ == '__main__':
    log = LogFileMixin()
    log.logo_sucess('Sucesso aqui')
    log.logo_error('Erro aqui aqui')