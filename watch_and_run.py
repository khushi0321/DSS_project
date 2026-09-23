from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess, time

class DataChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".xlsx"):
            print(f"Detected change in {event.src_path}, re-running pipeline...")
            subprocess.run(["python", "run_pipeline.py"])

observer = Observer()
observer.schedule(DataChangeHandler(), path="data/raw", recursive=False)
observer.start()
print("Watching data/raw for changes... (Ctrl+C to stop)")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()