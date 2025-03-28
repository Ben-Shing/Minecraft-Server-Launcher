import os

class PropertiesHandler():

    def __init__(self):
        self.properties = {
            "server-name": "",
            "min-ram": "",
            "max-ram": "",
        }

    def propertiesPath(self):
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        properties_file = os.path.join(current_dir, "MinecraftServerLauncher.properties")
        return properties_file

    def checkFileExist(self):
        """
        Check if the properties file exists.

        :return: True if the file exists, False otherwise.
        """
        path = self.propertiesPath()
        return os.path.isfile(path)
    
    def createPropertiesFile(self):
        """
        Create the properties file in the fixed location.

        :return: True if the file was created, False otherwise.
        """
        path = self.propertiesPath()
        try:
            with open(path, 'w') as properties_file:
                for key, value in self.properties.items():
                    properties_file.write(f'{key}={value}\n')
        except Exception as e:
            return False
        return True
        
    def readPropertiesFile(self):
        """
        Read the properties file and store the key and value in self.properties

        :return: Dictionary of properties.
        """
        path = self.propertiesPath()
        with open(path, 'r') as properties_file:
            for line in properties_file:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()
                if not value:
                    continue
                else:
                    self.properties[key] = value
        return self.properties
    
    def getPropertiesValue(self, key):
        """
        Get the value of a key in the properties.
        
        :param key: Key to get the value of.
        :return: Value of the key in the properties.
        """
        if key not in self.properties:
            raise KeyError(f'Key {key} not found in properties.')
        return self.properties[key]
        
    def setPropertiesValue(self, key, value):
        """
        Set the value of a key in the properties.
        
        :param key: Key to set the value of.
        :param value: Value to set the key to.
        """
        if key not in self.properties:
            raise KeyError(f'Key {key} not found in properties.')
        self.properties[key] = value


    def test(self):
        path = self.propertiesPath()
        properties = self.readPropertiesFile()
        print('Properties:')
        for key, value in properties.items():
            print(f'{key}={value}')

def testMode():
    print('Entering test mode...')
    PropertiesHandler().test()

if __name__ == '__main__':
    testMode()