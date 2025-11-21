from cryptography.fernet import Fernet
from pathlib import Path
import config

class EncryptionManager:
    def __init__(self, key_file=config.ENCRYPTION_KEY_FILE):
        
        self.key_file = Path(key_file)
        self.key = self._load_or_generate_key()
        self.cipher = Fernet(self.key)
    
    def _load_or_generate_key(self):
        
        if self.key_file.exists():
            with open(self.key_file, 'rb') as f:
                key = f.read()
                print(f"[*] Loaded encryption key from: {self.key_file}")
                return key
        else:
            
            key = Fernet.generate_key()
            
            
            self.key_file.parent.mkdir(parents=True, exist_ok=True)
            
            
            with open(self.key_file, 'wb') as f:
                f.write(key)
            
            print(f"[*] Generated new encryption key: {self.key_file}")
            print(f"[!] IMPORTANT: Keep this key safe! You need it to decrypt logs.")
            return key
    
    def encrypt_file(self, file_path):
        
        try:
            file_path = Path(file_path)
            
           
            with open(file_path, 'rb') as f:
                data = f.read()
            
           
            encrypted_data = self.cipher.encrypt(data)
            
            
            encrypted_file = file_path.with_suffix(file_path.suffix + '.enc')
            with open(encrypted_file, 'wb') as f:
                f.write(encrypted_data)
            
            print(f"[*] Encrypted: {file_path.name} -> {encrypted_file.name}")
            return encrypted_file
            
        except Exception as e:
            print(f"[!] Encryption error: {e}")
            return None
    
    def decrypt_file(self, encrypted_file_path):
        
        try:
            encrypted_file_path = Path(encrypted_file_path)
            
           
            with open(encrypted_file_path, 'rb') as f:
                encrypted_data = f.read()
            
            
            decrypted_data = self.cipher.decrypt(encrypted_data)
            
            
            original_file = Path(str(encrypted_file_path).replace('.enc', ''))
            
            
            with open(original_file, 'wb') as f:
                f.write(decrypted_data)
            
            print(f"[*] Decrypted: {encrypted_file_path.name} -> {original_file.name}")
            return original_file
            
        except Exception as e:
            print(f"[!] Decryption error: {e}")
            return None
