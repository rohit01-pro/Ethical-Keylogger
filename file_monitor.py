from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging
from datetime import datetime
import config

class ActivityHandler(FileSystemEventHandler):
    
    def __init__(self, log_file):
        self.log_file = log_file
        
        
        self.log_file.parent.mkdir(parents=True, exist_ok=True)
        
        
        logging.basicConfig(
            filename=str(log_file),
            level=logging.INFO,
            format='%(asctime)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        logging.info(f"\n{'='*60}\nFILE MONITORING STARTED\n{'='*60}")
    
    def on_created(self, event):
        
        if not event.is_directory:
            logging.info(f"FILE CREATED: {event.src_path}")
            print(f"[*] File created: {event.src_path}")
    
    def on_modified(self, event):
        
        if not event.is_directory:
            logging.info(f"FILE MODIFIED: {event.src_path}")
    
    def on_deleted(self, event):
        
            logging.info(f"FILE DELETED: {event.src_path}")
            print(f"[*] File deleted: {event.src_path}")
    
    def on_moved(self, event):
        
        if not event.is_directory:
            logging.info(f"FILE MOVED: {event.src_path} -> {event.dest_path}")
            print(f"[*] File moved: {event.src_path} -> {event.dest_path}")

class FileSystemMonitor:
    def __init__(self, directories=config.WATCH_DIRECTORIES):
       
        self.directories = directories
        self.observers = []
        
        log_file = config.LOGS_DIR / 'activities' / 'file_activity.log'
        self.handler = ActivityHandler(log_file)
    
    def start(self):
        
        for directory in self.directories:
            try:
                observer = Observer()
                observer.schedule(
                    self.handler,
                    directory,
                    recursive=True
                )
                observer.start()
                self.observers.append(observer)
                print(f"[*] Monitoring directory: {directory}")
            except Exception as e:
                print(f"[!] Error monitoring {directory}: {e}")
    
    def stop(self):
        
        for observer in self.observers:
            observer.stop()
            observer.join(timeout=2)
        print("[*] File system monitoring stopped")
