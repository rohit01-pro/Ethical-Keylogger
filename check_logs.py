#!/usr/bin/env python3
"""
Quick utility to check where logs are saved and view their contents
"""

import config
from pathlib import Path
from datetime import datetime

def check_logs():
    
    
    print("\n" + "="*80)
    print(" KEYLOGGER PROJECT - LOG STATUS")
    print("="*80)
    
    
    print("\n KEYSTROKE LOGS:")
    keystroke_file = config.KEYSTROKE_LOG_FILE
    if keystroke_file.exists():
        size = keystroke_file.stat().st_size
        modified = datetime.fromtimestamp(keystroke_file.stat().st_mtime)
        print(f"  ✓ File: {keystroke_file.absolute()}")
        print(f"    Size: {size} bytes")
        print(f"    Last modified: {modified}")
        
       
        encrypted_file = keystroke_file.with_suffix(keystroke_file.suffix + '.enc')
        if encrypted_file.exists():
            enc_size = encrypted_file.stat().st_size
            print(f"  ✓ Encrypted: {encrypted_file.name} ({enc_size} bytes)")
    else:
        print(f"  ✗ No keystrokes logged yet")
        print(f"    Will be saved to: {keystroke_file.absolute()}")
    
   
    print("\n SCREENSHOTS:")
    screenshot_dir = config.SCREENSHOT_DIR
    if screenshot_dir.exists():
        screenshots = list(screenshot_dir.glob('*.png'))
        if screenshots:
            print(f"  ✓ Directory: {screenshot_dir.absolute()}")
            print(f"    Total screenshots: {len(screenshots)}")
            print(f"    Latest: {screenshots[-1].name}")
            
            
            print("\n  Recent screenshots:")
            for screenshot in sorted(screenshots)[-3:]:
                size = screenshot.stat().st_size / 1024  
                print(f"    - {screenshot.name} ({size:.1f} KB)")
        else:
            print(f"  ✗ No screenshots captured yet")
            print(f"    Will be saved to: {screenshot_dir.absolute()}")
    else:
        print(f"  ✗ Directory not created yet: {screenshot_dir.absolute()}")
    
    
    print("\n FILE ACTIVITY LOGS:")
    activity_file = config.LOGS_DIR / 'activities' / 'file_activity.log'
    if activity_file.exists():
        size = activity_file.stat().st_size
        print(f"  ✓ File: {activity_file.absolute()}")
        print(f"    Size: {size} bytes")
        
        
        with open(activity_file, 'r') as f:
            lines = f.readlines()
            if lines:
                print("\n  Last 5 activities:")
                for line in lines[-5:]:
                    print(f"    {line.strip()}")
    else:
        print(f"  ✗ No file activity logged yet")
        print(f"    Will be saved to: {activity_file.absolute()}")
    
    
    print("\n ENCRYPTION:")
    key_file = config.ENCRYPTION_KEY_FILE
    if key_file.exists():
        print(f"  ✓ Key exists: {key_file.absolute()}")
        print(f"      Keep this key safe! Needed to decrypt logs.")
    else:
        print(f"  ✗ No encryption key generated yet")
        print(f"    Will be created at: {key_file.absolute()}")
    
    print("\n" + "="*80)
    print("\n TIP: Run 'python3 main.py' to start monitoring")
    print(" TIP: Run 'python3 view_logs.py' to decrypt and view keystroke logs\n")

if __name__ == '__main__':
    check_logs()
