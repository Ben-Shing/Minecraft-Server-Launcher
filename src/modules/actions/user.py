import os
import subprocess

class ActionHandler():

    def __init__(self):
        pass

    def cmdChoice(self, timeout=15, default='Y'):
        if os.environ["Path"].find("C:\\Windows\\System32") == -1:
            os.environ["Path"] = os.environ["Path"] + ";C:\\Windows\\System32"
        process = subprocess.Popen(['cmd.exe', '/c', 'choice /C YNP /N /T {} /D {}'.format(timeout, default)], stdout=subprocess.PIPE)
        output, error = process.communicate()
        choice = output.strip().decode('utf-8')
        if choice == 'P':
            self.pause()
            return 'N'
        else:
            return choice

    def pause(self):
        input("Press Enter to continue...")

    def test(self):
        print('Testing action handler:')
        print('cmd_choice:')
        self.cmdChoice()
        print('Pause:')
        self.pause()
        print('Test complete.')


def testMode():
    print('Entering test mode...')
    ActionHandler().test()

if __name__ == '__main__':
    testMode()