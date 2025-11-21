import sys
import signal
import time
from keylogger import Keylogger
from screenshot_capture import ScreenshotCapture
from file_monitor import FileSystemMonitor
from encryption_manager import EncryptionManager
import config

def show_consent():
    
    print("\n" + "="*80)
    print("  ETHICAL KEYLOGGER - EDUCATIONAL PURPOSE ONLY ")
    print("="*80)
    print("\nThis software monitors and records:")
    print("  - All keyboard inputs")
    print("  - Periodic screenshots")
    print("  - File system activities")
    print("\nBy typing 'I AGREE', you acknowledge:")
    print("  1. You own this device OR have written permission to monitor it")
    print("  2. This is for educational/research purposes only")
    print("  3. You will NOT use this for unauthorized surveillance")
    print("  4. You accept full legal responsibility for your usage")
    print("\nUnauthorized use may violate laws including:")
    print("  - IT Act 2000 (India)")
    print("  - Computer Fraud and Abuse Act (USA)")
    print("  - General Data Protection Regulation (EU)")
    print("="*80)
    
    response = input("\nType 'I AGREE' to continue or 'NO' to exit: ").strip().upper()
    return response == 'I AGREE'

def signal_handler(sig, frame):
    
    print("\n\n[*] Shutting down gracefully...")
    sys.exit(0)

def main():
    
    signal.signal(signal.SIGINT, signal_handler)
    
    
    if not show_consent():
        print("\n Consent denied. Exiting...")
        sys.exit(0)
    
    print("\n Consent granted. Starting monitoring...")
    print("[*] Press ESC key to stop keylogger")
    print("[*] Press Ctrl+C to stop all monitoring\n")
    
    try:
        
        print("[*] Initializing encryption...")
        encryption = EncryptionManager()
        
        
        print("[*] Starting screenshot capture...")
        screenshot = ScreenshotCapture(
            save_dir=config.SCREENSHOT_DIR,
            interval=config.SCREENSHOT_INTERVAL
        )
        screenshot.start()
        
        
        print("[*] Starting file system monitor...")
        file_monitor = FileSystemMonitor(config.WATCH_DIRECTORIES)
        file_monitor.start()
        
        
        print("[*] Starting keylogger...")
        keylogger = Keylogger(config.KEYSTROKE_LOG_FILE)
        keylogger.start()
        
        
        print("\n[*] ESC pressed. Stopping all services...")
        screenshot.stop()
        file_monitor.stop()
        
       
        print("[*] Encrypting logs...")
        if config.KEYSTROKE_LOG_FILE.exists():
            encryption.encrypt_file(config.KEYSTROKE_LOG_FILE)
            print(f"[✓] Keylog encrypted")
        
        print("\n[✓] All monitoring stopped successfully")
        
    except Exception as e:
        print(f"\n[!] Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
