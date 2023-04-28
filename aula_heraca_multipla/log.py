from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

# Abstração
class Log:

    def _log(self, msg):
        raise NotImplementedError(
            'Implemente o método log'
        )
    
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