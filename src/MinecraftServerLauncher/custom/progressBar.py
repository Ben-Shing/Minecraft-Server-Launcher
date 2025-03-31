from rich.progress import Progress

class RichBar():
    
    def __init__(self):
        pass

    def createWithTask(self, task: str):
        """
        Create a progress bar with a task.

        :param task: The task name.
        """
        self.bar = Progress()
        self.bar.add_task(task)

    def createWithTotal(self, total: int):
        """
        Create a progress bar with the total number of items.

        :param total: The total number of items.
        """
        self.bar = Progress()
        self.id = self.bar.add_task('Progress', total=total)

    def update(self, current: int):
        """
        Update the progress bar with the current number of items.

        :param current: The current number of items.
        """
        self.bar.update(self.id, completed=current)

    def complete(self):
        """
        Complete the progress bar.
        """
        self.bar.stop()
        self.bar = None

