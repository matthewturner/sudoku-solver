import os

from watchdog.events import FileSystemEventHandler


class RerunEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        os.system('cls && python ./main.py')
