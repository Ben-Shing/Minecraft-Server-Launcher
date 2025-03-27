import logging

class Log():

    def __init__(self, name, level = logging.INFO):
        self.logger = logging.getLogger(name)        
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s: %(message)s"))
        self.logger.addHandler(console_handler)
        self.logger.info('Initializing ' + name + ' logger')
        self.logger.info('Logging level: ' + logging.getLevelName(level))

    def debug(self, message):
        self.logger.debug(message)
        
    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

    def test(self):
        print('Testing log:')
        self.debug('This is a debug message')
        self.info('This is an info message')
        self.warning('This is a warning message')
        self.error('This is an error message')
        self.critical('This is a critical message')
        print('Test complete.')

def test_mode():
    print('Entering test mode...')
    logger = Log('test', level = logging.DEBUG)
    logger.test()

if __name__ == '__main__':
    test_mode()