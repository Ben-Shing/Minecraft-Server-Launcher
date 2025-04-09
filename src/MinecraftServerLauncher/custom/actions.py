import os
import subprocess

class UserHandler():

    def __init__(self):
        pass

    def cmdChoice(self, timeout=15, default='Y'):
        """
        Run the choice command in cmd.exe and return the choice.
        If the timeout is reached, the default choice is selected.
        Available choices are 'Y', 'N', and 'P' (pause).

        :param timeout: The time in seconds before the default choice is selected. Default is 15 seconds.
        :param default: The default choice if the timeout is reached. Default is 'Y'.
        :return: The choice made by the user.
        """
        if os.environ["Path"].find("C:\\Windows\\System32") == -1:
            os.environ["Path"] = os.environ["Path"] + ";C:\\Windows\\System32"
        process = subprocess.Popen(['cmd.exe', '/c', 'choice /C YNP /N /T {} /D {}'.format(timeout, default)], stdout=subprocess.PIPE)
        output, _ = process.communicate()
        choice = output.strip().decode('utf-8')
        if choice == 'P':
            self.pause()
            return 'N'
        else:
            return choice

    def pause(self):
        """
        Pause the program until the user presses Enter.
        """
        input("Press Enter to continue...")

    def test(self):
        print('Testing action handler:')
        print('cmd_choice:')
        self.cmdChoice()
        print('Pause:')
        self.pause()
        print('Test complete.')


class ServerHandler():
    """
    Handle Minecraft server.
    """

    def __init__(self, custom_jdk: str = None):
        self.custom_jdk = custom_jdk

    def locateServer(self):
        """
        Locate the Minecraft server executable.
        """
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        server_folder_path = os.path.join(current_dir, 'server')
        if not os.path.exists(server_folder_path):
            raise FileNotFoundError(f"Server folder not found: {server_folder_path}")
        
        #TODO: Finding server executable inside the server folder
        #TODO: Need to handle different mod loaders and vanilla, also handle different versions of server

        #! Codes below is example placeholder and need to be replaced with working codes

        # Define possible server executable names for different mod loaders and vanilla
        possible_executables = [
            'server.jar',  # Vanilla
            'forge.jar',   # Forge
            'fabric-server-launch.jar'  # Fabric
        ]

        # Search for the server executable in the server folder and its /bin subfolder
        search_paths = [server_folder_path, os.path.join(server_folder_path, 'bin')]

        for search_path in search_paths:
            for executable in possible_executables:
                server_executable_path = os.path.join(search_path, executable)
                if os.path.exists(server_executable_path):
                    return server_executable_path

        # If no executable is found, raise an error
        raise FileNotFoundError("No valid server executable found in the server folder.")

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
    UserHandler().test()
    ServerHandler().test()

if __name__ == '__main__':
    testMode()