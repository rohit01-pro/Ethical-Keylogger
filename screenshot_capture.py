from PIL import ImageGrab
import time
from datetime import datetime
import threading
import config

class ScreenshotCapture:
    def __init__(self, save_dir=config.SCREENSHOT_DIR, interval=config.SCREENSHOT_INTERVAL):
        
        self.save_dir = save_dir
        self.interval = interval
        self.running = False
        self.thread = None
        
       
        self.save_dir.mkdir(parents=True, exist_ok=True)
    
    def capture_screenshot(self):
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = self.save_dir / f'screenshot_{timestamp}.png'
        
        try:
           
            screenshot = ImageGrab.grab()
            screenshot.save(filename, 'PNG')
            print(f"[*] Screenshot saved: {filename.name}")
            return filename
        except Exception as e:
            print(f"[!] Screenshot error: {e}")
            return None
    
    def _screenshot_loop(self):
        
        while self.running:
            self.capture_screenshot()
            time.sleep(self.interval)
    
    def start(self):
        
        self.running = True
        self.thread = threading.Thread(
            target=self._screenshot_loop,
            daemon=True
        )
        self.thread.start()
        print(f"[*] Screenshot capture started (interval: {self.interval}s)")
    
    def stop(self):
        
        self.running = False
        if self.thread:
            self.thread.join(timeout=2)
        print("[*] Screenshot capture stopped")
