import logging
import rich.logging as rlogging

import log


class ColorLog(log.Log):

    def __init__(self, name, level = logging.INFO):
        self.logger = logging.getLogger(name)
        console_handler = rlogging.RichHandler()
        console_handler.setLevel(level)
        self.logger.addHandler(console_handler)
        self.logger.setLevel(level)
        self.logger.info('Initializing ' + name + ' logger')
        self.logger.info('Logging level: ' + logging.getLevelName(level))


def testMode():
    print('Entering test mode...')
    logger = ColorLog('test', level = logging.DEBUG)
    logger.test()   

if __name__ == '__main__':
    testMode()
