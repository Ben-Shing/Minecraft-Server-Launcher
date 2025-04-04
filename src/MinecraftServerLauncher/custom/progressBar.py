from rich.progress import Progress

class RichBar():
    
    def __init__(self):
        pass

    def create(self, description: str = 'Progress', total: int = 100):
        """
        Create a progress bar.

        :param task: The task name.
        """
        self.bar = Progress()
        self.id = self.bar.add_task(description=description, total=total)
        self.total = total
        self.bar.start()

    def update(self, current: int):
        """
        Update the progress bar with the current number of items.

        :param current: The current number of items.
        """
        self.bar.update(self.id, completed=current)

    def updateDescription(self, description: str):
        """
        Update the progress bar description.

        :param description: New description.
        """
        self.bar.update(self.id, description=description)

    def complete(self):
        """
        Complete the progress bar.
        """
        self.bar.update(self.id, completed=self.total)
        self.bar.stop()
        self.bar = None

    def test(self):
        """
        Test the progress bar.
        """
        import time
        self.create('Testing Start')
        time.sleep(1)
        self.update(5)
        time.sleep(3)
        self.update(50)
        self.updateDescription('Testing Mid')
        time.sleep(1)
        self.update(66)
        time.sleep(4)
        self.update(99)
        time.sleep(0.7)
        self.updateDescription('Almost Done')
        time.sleep(2)
        self.updateDescription('Done')
        self.complete()

def testMode():
    print('Entering test mode...')
    bar1 = RichBar()
    bar2 = RichBar()
    bar1.test()
    bar2.test()
    print('Test complete.')

if __name__ == '__main__':
    testMode()
