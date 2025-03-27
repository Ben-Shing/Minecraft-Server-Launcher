import logging
import rich.logging as rlogging

if __name__ == '__main__':
    import log
elif __name__ == 'logger.color':
    from logger import log



class ColorLog(log.Log):

    def __init__(self, name, level = logging.INFO):
        self.logger = logging.getLogger(name)
        console_handler = rlogging.RichHandler()
        console_handler.setLevel(level)
        self.logger.addHandler(console_handler)
        self.logger.setLevel(level)
        self.logger.info(f'Initializing logger: {name}, logging level: {logging.getLevelName(level)}')


def testMode():
    print('Entering test mode...')
    logger = ColorLog('test', level = logging.DEBUG)
    logger.test()   

if __name__ == '__main__':
    testMode()
