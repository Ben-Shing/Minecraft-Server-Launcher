import logging
import rich.logging

import log



class ColorLog(log.Log):

    
    def __init__(self, name, level = logging.INFO):
        self.logger = logging.getLogger(name)
        console_handler = rich.logging.RichHandler()
        console_handler.setLevel(level)
        self.logger.addHandler(console_handler)
        self.logger.setLevel(level)
        self.logger.info('Initializing ' + name + ' logger')
        self.logger.info('Logging level: ' + logging.getLevelName(level))


if __name__ == '__main__':
    print('Entering test mode...')
    logger = ColorLog('test', level = logging.DEBUG)
    print()
    print('Testing logging...')
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')
    print('Exiting...')
