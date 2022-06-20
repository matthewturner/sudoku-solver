import sys
import time
import logging

from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from rerun_event_handler import RerunEventHandler

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = RerunEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
