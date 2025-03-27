import os

class PropertiesHandler():

    def __init__(self):
        self.properties = {
            "server-name": "",
            "min-ram": "",
            "max-ram": "",
        }

    def properties_path(self):
        current_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        properties_file = os.path.join(current_dir, "MinecraftServerLauncher.properties")
        return properties_file

    def check_file_exist(self):
        path = self.properties_path()
        return os.path.isfile(path)
    
    def create_properties_file(self):
        path = self.properties_path()
        with open(path, 'w') as properties_file:
            for key, value in self.properties.items():
                properties_file.write(f'{key}={value}\n')
        return path
        
    def read_properties_file(self, path):
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
    
    def get_properties_value(self, key):
        if key not in self.properties:
            raise KeyError(f'Key {key} not found in properties.')
        return self.properties[key]
        
    def set_properties_value(self, key, value):
        if key not in self.properties:
            raise KeyError(f'Key {key} not found in properties.')
        self.properties[key] = value


    def test(self):
        path = self.properties_path()
        properties = self.read_properties_file(path)
        print('Properties:')
        for key, value in properties.items():
            print(f'{key}={value}')

def test_mode():
    print('Entering test mode...')
    PropertiesHandler().test()

if __name__ == '__main__':
    test_mode()