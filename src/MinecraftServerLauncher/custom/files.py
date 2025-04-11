import os

class PropertiesHandler():

    def __init__(self):
        self.properties = {
            "server-name": "",
            "min-ram": "",
            "max-ram": "",
            "custom-jdk": "",
            "auto-restart": ""
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
    
    def getPropertiesValue(self, *keys):
        """
        Get the value of a key in the properties.
        
        :param *keys: Key(s) to get the value of.
        :return: Value(s) of the key in the properties.
        """
        if keys.count() == 0:
            raise ValueError('No keys provided.')
        if keys.count() == 1:
            key = keys[0]
            if key not in self.properties:
                raise KeyError(f'Key {key} not found in properties.')
            return self.properties[key]
        else:
            values = []
            for key in keys:
                if key not in self.properties:
                    raise KeyError(f'Key {key} not found in properties.')
                values.append(self.properties[key])
            return values
        
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


class ServerHandler():
    """
    Handle Minecraft server.
    """

    def __init__(self, custom_jdk: str = None, system: str = 'win'):
        self.custom_jdk = custom_jdk
        self.system = system
        self.server = None

    def locateServer(self):
        """
        Locate the Minecraft server executable.
        """
        # Check if the server folder exists
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        server_folder_path = os.path.join(current_dir, 'server')
        if not os.path.exists(server_folder_path):
            raise FileNotFoundError(f"Server folder not found: {server_folder_path}")

        #  Finding old forge server jar file
        for root, dirs, files in os.walk(server_folder_path):
            for file in files:
                if file.startswith('forge-') and file.endswith('.jar'):
                    self.server = os.path.join(root, file)
                    self.version = file.split('-')[1]
                    self.loader = 'forge'
                    self.loader_version = file.split('-')[2]
                    self.forge = 'old'
                    break

        #  Finding new forge server jar file
        sub_path = os.path.join('libraries', 'net', 'minecraftforge', 'forge')
        if os.path.exists(sub_path):
            for root, dirs, files in os.walk(sub_path):
                for file in files:
                    if file.endswith('.jar'):
                        self.server = os.path.join(root, file)
                        self.version = file.split('-')[1]
                        self.loader = 'forge'
                        self.loader_version = file.split('-')[2]
                        self.forge = 'new'
                        break

        # Finding fabric server jar file
        server_executable = os.path.join(server_folder_path, 'fabric-server-launch.jar')
        if os.path.isfile(server_executable):
            self.server = server_executable
            self.loader = 'fabric'

        # Finding spigot server jar file
        # TODO: Need Test
        server_executable = os.path.join(server_folder_path, 'spigot.jar')
        if os.path.isfile(server_executable):
            self.server = server_executable
            self.loader = 'spigot'
        
        # Finding paper server jar file
        # TODO: Need Test
        server_executable = os.path.join(server_folder_path, 'paper.jar')
        if os.path.isfile(server_executable):
            self.server = server_executable
            self.loader = 'paper'
        
        # Finding vanilla server jar file
        server_executable = os.path.join(server_folder_path, 'server.jar')
        if os.path.isfile(server_executable):
            self.server = server_executable
            self.loader = 'vanilla'

        # No server executable found
        if not self.server:
            raise FileNotFoundError("No server executable found in the server folder.")

        return self.server


    def startServer(self, min_ram: str = None, max_ram: str = None, *args):
        """
        Start the Minecraft server.
        """
        # Check if the server is located
        if not self.server:
            raise RuntimeError("Server not located. Please locate the server before starting.")
        
        # Check if custom JDK is provided
        if self.custom_jdk:
            java = self.custom_jdk
        else:
            java = 'java'
        
        # Parsing command for different loaders
        # * Only vanilla, fabric and forge are done currently
        if self.loader == 'vanilla' or self.loader == 'fabric':
            command = f'{java} -Xms{min_ram} -Xmx{max_ram} -jar {self.server} nogui {" ".join(args)}'
        elif self.loader == 'forge':
            if self.forge == 'old':
                command = f'{java} -Xms{min_ram} -Xmx{max_ram} -jar {self.server} nogui {" ".join(args)}'
            elif self.forge == 'new':
                command = f'{java} -Xms{min_ram} -Xmx{max_ram} @libraries/net/minecraftforge/forge/{self.version}-{self.loader_version}-{self.system}_args.txt nogui {" ".join(args)} %*'
        


        os.system(command)


    def test(self):
        print('Testing server handler:')
        print('Start server:')
        self.startServer()
        print('Test complete.')


def testMode():
    print('Entering test mode...')
    PropertiesHandler().test()
    ServerHandler().test()

if __name__ == '__main__':
    testMode()