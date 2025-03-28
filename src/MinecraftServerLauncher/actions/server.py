import os

class ServerHandler():
    """
    Handle Minecraft server.
    """

    def __init__(self, custom_jdk: str = None):
        self.custom_jdk = custom_jdk

    def locateServer(self):
        """
        Locate the Minecraft server.
        """
        pass

    def startServer(self):
        """
        Start the Minecraft server.
        """
        pass

    def test(self):
        print('Testing server handler:')
        print('Start server:')
        self.startServer()
        print('Test complete.')


def testMode():
    print('Entering test mode...')
    pass


if __name__ == '__main__':
    testMode()