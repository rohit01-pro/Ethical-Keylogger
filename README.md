Keylogger Activity Monitor
Educational Endpoint Security Monitoring Tool

Python 3.8+
License: MIT
Educational Purpose

 DISCLAIMER: This tool is designed exclusively for educational purposes to demonstrate endpoint security concepts. Unauthorized use of keylogging software is illegal and may violate privacy laws including the IT Act 2000 (India), Computer Fraud and Abuse Act (USA), and GDPR (EU).

Table of Contents
Overview

Features
Legal & Ethical Notice
Tech Stack
Installation
Project Structure
Usage
Configuration
How It Works
Security Features
Testing
Troubleshooting
Educational Value
Future Enhancements
Contributing
License

🎯 Overview
The Keylogger Activity Monitor is a comprehensive Python-based endpoint security monitoring tool built to demonstrate how system-level monitoring works from both offensive and defensive security perspectives. This project captures keystroke activity, periodic screenshots, and file system events while implementing industry-standard encryption to secure all collected data.

What This Project Demonstrates
System-Level Programming: Interaction with OS-level keyboard and file system APIs
Event-Driven Architecture: Real-time monitoring using event listeners and handlers
Cryptography: AES-128 symmetric encryption using Fernet
Multi-Threading: Concurrent execution of monitoring modules
Security Protocols: Secure email transmission via SMTP with TLS/SSL
Ethical Development: Mandatory consent mechanisms and legal compliance

✨ Features
Core Functionality
✅ Keystroke Logging

Captures all keyboard input in real-time
Handles special keys (Enter, Space, Backspace, etc.)
Buffered writing for optimal performance
Timestamped log entries

✅ Screenshot Capture

Automated periodic screen captures
Configurable capture intervals
PNG format with compression
Threaded background execution

✅ File System Monitoring

Real-time file creation/modification/deletion tracking
Recursive directory monitoring
Detailed activity logs with timestamps
Multiple directory support

✅ Encryption & Security

AES-128 encryption (Fernet) for all logs
Secure key generation and storage
Encrypted data at rest
Secure key management practices

✅ Data Exfiltration Demo
Email transmission demonstration via SMTP
TLS/SSL encrypted connections
Attachment support for encrypted logs
Educational simulation only

✅ Ethical Safeguards

Mandatory consent dialog on startup
Legal disclaimer display
Graceful shutdown mechanisms (ESC key)
Clear educational labeling

⚖️ Legal & Ethical Notice
🚨 CRITICAL: READ BEFORE USE
This software is provided STRICTLY FOR EDUCATIONAL PURPOSES. You must:

✅ OWN the device you're monitoring, OR have explicit written permission from the owner

✅ Obtain informed consent from all users before monitoring

✅ Use ONLY in controlled environments (virtual machines, test systems)

✅ Comply with all applicable laws and regulations

✅ Label your use as educational/research

Legal Framework
India: IT Act 2000 - Sections 43, 66, 72

USA: Computer Fraud and Abuse Act (CFAA)
EU: General Data Protection Regulation (GDPR)
UK: Computer Misuse Act 1990
Violations can result in:
Criminal prosecution
Civil liability
Fines and imprisonment
Permanent criminal record

Ethical Use Policy
This tool should be used to:

✅ Learn about endpoint security mechanisms

✅ Understand threat actor techniques

✅ Develop defensive security skills

✅ Conduct authorized security research

✅ Build cybersecurity portfolio projects

NEVER use this tool to:

❌ Monitor individuals without their knowledge

❌ Spy on employees, family members, or partners

❌ Steal credentials or sensitive information

❌ Deploy on public or shared computers

❌ Conduct unauthorized surveillance

🛠️ Tech Stack
Technology	Version	Purpose
Python	3.8+	Core programming language
pynput	1.7.7	Keyboard and mouse event monitoring
watchdog	4.0.0	File system event monitoring
Pillow	10.1.0	Screenshot capture and image processing
cryptography	41.0.7	Fernet symmetric encryption (AES-128)
schedule	1.2.0	Task scheduling for periodic operations
smtplib	Built-in	Email transmission.

📥 Installation

Prerequisites
Python 3.8 or higher

pip3 package manager

Virtual environment (recommended)

Step 1: Clone the Repository
~~~bash
git clone https://github.com/yourusername/keylogger-activity-monitor.git
cd keylogger-activity-monitor
~~~

Step 2: Create Virtual Environment
~~~bash
python3 -m venv venv 
~~~

# Activate virtual environment
# On Linux/Mac:
~~~bash
source venv/bin/activate
~~~

# On Windows:
~~~bash
venv\Scripts\activate
~~~

Step 3: Install Dependencies
~~~bash
pip install -r requirements.txt
~~~

Or install manually:

~~~bash
pip install pynput==1.7.7 watchdog==4.0.0 Pillow==10.1.0 cryptography==41.0.7 schedule==1.2.0
~~~

Project Structure
text
keylogger-activity-monitor/
│
├── main.py                      # Main entry point with consent mechanism
├── keylogger.py                 # Core keystroke capture module
├── screenshot_capture.py        # Screenshot automation module
├── file_monitor.py              # File system monitoring module
├── encryption_manager.py        # Encryption/decryption handler
├── exfiltration_demo.py         # Email transmission demo (optional)
├── config.py                    # Centralized configuration settings
├── check_logs.py                # Utility to check log status
├── view_logs.py                 # Utility to decrypt and view logs
│
├── logs/                        # Generated logs directory
│   ├── keystrokes/              # Keystroke logs
│   ├── screenshots/             # Screenshot images
│   └── activities/              # File activity logs
│
├── keys/                        # Encryption keys (NEVER commit!)
│   └── key.key                  # Fernet encryption key
│
├── docs/                        # Documentation
│   ├── ETHICS.md                # Ethical guidelines
│   ├── LEGAL_DISCLAIMER.md      # Legal notices
│   └── ARCHITECTURE.md          # System architecture
│
├── requirements.txt             # Python dependencies
├── .gitignore                   # Git ignore rules
├── LICENSE                      # MIT License
└── README.md                    # This file

 Usage
Basic Usage
Start the monitoring tool:

~~~bash
python3 main.py
~~~

Grant consent when prompted (type I AGREE)

Monitor output in the terminal showing:

Keystroke capture status

Screenshot capture notifications

File activity events

Storage locations

Stop monitoring:

Press ESC key to stop keylogger

Press Ctrl+C to stop all services

View Logs
Check log status:

~~~bash
python3 check_logs.py
~~~

View keystroke logs:

~~~bash
python3 view_logs.py
~~~
Decrypt Logs Manually
python
from encryption_manager import EncryptionManager

# Initialize encryption manager
encryption = EncryptionManager()

# Decrypt a file
decrypted_file = encryption.decrypt_file('logs/keystrokes/keylog.txt.enc')
 Configuration
Edit config.py to customize behavior:

python
# Screenshot interval (seconds)
SCREENSHOT_INTERVAL = 300  # 5 minutes

# Keystroke buffer size (keystrokes before writing to file)
LOG_BUFFER_SIZE = 50

# Directories to monitor for file changes
WATCH_DIRECTORIES = [os.path.expanduser('~/Documents')]

# Email settings (for demo - use environment variables)
SENDER_EMAIL = os.getenv('SENDER_EMAIL', '')
SENDER_PASSWORD = os.getenv('SENDER_PASSWORD', '')
RECEIVER_EMAIL = os.getenv('RECEIVER_EMAIL', '')
Environment Variables (Optional Email Demo)
bash
export SENDER_EMAIL="your_email@gmail.com"
export SENDER_PASSWORD="your_app_password"
export RECEIVER_EMAIL="receiver@email.com"
export SMTP_SERVER="smtp.gmail.com"

How It Works
Architecture Overview
text
┌─────────────────────────────────────────────────────────────┐
│                     USER LAUNCHES APPLICATION                │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│              CONSENT DIALOG (Terminal-Based)                 │
│  "Do you agree to monitoring? Type 'I AGREE' or 'NO'"       │
└────────────────┬────────────────────────────────────────────┘
                 │
        ┌────────┴────────┐
        │                 │
       NO                YES
        │                 │
        ▼                 ▼
   ┌────────┐    ┌───────────────────────────────────────────┐
   │  EXIT  │    │    START MONITORING (3 Parallel Threads)  │
   └────────┘    └───────────────────────────────────────────┘
                         │
         ┌───────────────┼───────────────┐
         │               │               │
         ▼               ▼               ▼
   ┌──────────┐   ┌──────────┐   ┌──────────────┐
   │Keylogger │   │Screenshot│   │File Monitor  │
   │(pynput)  │   │(Pillow)  │   │(watchdog)    │
   └─────┬────┘   └─────┬────┘   └──────┬───────┘
         │              │                │
         └──────────────┼────────────────┘
                        │
                        ▼
              ┌──────────────────┐
              │Encryption Manager│
              │   (Fernet)       │
              └─────────┬────────┘
                        │
                        ▼
              ┌──────────────────┐
              │ Encrypted Logs   │
              │ (AES-128)        │
              └─────────┬────────┘
                        │
                ┌───────┴────────┐
                │                │
                ▼                ▼
        ┌───────────┐    ┌──────────────┐
        │Email Demo │    │Local Storage │
        │(Optional) │    │ (Default)    │
        └───────────┘    └──────────────┘
Module Responsibilities
1. Keylogger Module (keylogger.py)

Listens to keyboard events using pynput.keyboard.Listener

Buffers keystrokes for efficient disk I/O

Handles special keys (Enter, Space, Backspace, etc.)

Writes timestamped logs to file

Implements graceful shutdown on ESC key

2. Screenshot Module (screenshot_capture.py)

Captures full-screen screenshots using PIL.ImageGrab

Runs in background daemon thread

Saves images with timestamp naming

Configurable capture intervals

Thread-safe start/stop operations

3. File Monitor Module (file_monitor.py)

Uses watchdog.observers.Observer for file system events

Monitors file creation, modification, deletion, and movement

Recursive directory monitoring

Logs all activities with timestamps

Supports multiple directory paths

4. Encryption Manager (encryption_manager.py)

Generates Fernet encryption keys

Encrypts logs using AES-128 in CBC mode

Provides decrypt functionality for log analysis

Secure key storage and management

Automatic key generation on first run

5. Main Controller (main.py)

Enforces consent mechanism

Orchestrates all modules

Handles graceful shutdown

Manages threading and lifecycle

Displays storage locations

🔒 Security Features
Data Protection
Encryption at Rest: All logs encrypted with AES-128

Key Management: Secure key generation and storage

No Plaintext Storage: Original logs encrypted immediately after capture

Secure Transmission: Email demo uses TLS/SSL encryption

Access Control
Mandatory Consent: Cannot bypass consent dialog

Graceful Shutdown: ESC key provides user control

No Stealth Mode: Clearly visible operation

Legal Disclaimers: Prominent warnings and notices

Development Best Practices
No Hardcoded Credentials: Environment variables only

Secure Defaults: Conservative configuration settings

Error Handling: Comprehensive exception management

Logging: Detailed operational logs for debugging

Code Documentation: Extensive comments and docstrings

🧪 Testing
Recommended Testing Environment
⚠️ CRITICAL: NEVER test on production systems!

Use isolated virtual machine (VM) environments:

VirtualBox (Free)

VMware Workstation

UTM (Mac M1/M2)

QEMU/KVM (Linux)

Testing Checklist
 Consent dialog displays correctly

 Keylogger captures all keystrokes

 Special keys (Enter, Space, Backspace) handled properly

 Screenshots captured at specified intervals

 File system monitoring detects changes

 Logs are properly encrypted

 Decryption works correctly

 ESC key stops keylogger gracefully

 Ctrl+C stops all services

 No plaintext logs remain after encryption

 Error handling prevents crashes

 Storage locations are displayed

Unit Testing
bash
# Test keylogger module
python3 -c "from keylogger import Keylogger; print('✓ Keylogger import successful')"

# Test encryption
python3 -c "from encryption_manager import EncryptionManager; e = EncryptionManager(); print('✓ Encryption working')"

# Test screenshot
python3 -c "from screenshot_capture import ScreenshotCapture; print('✓ Screenshot module working')"
🐛 Troubleshooting
Common Issues
Issue 1: pynput not detecting keystrokes

bash
# Solution: Run with elevated privileges (testing VM only!)
sudo python3 main.py
Issue 2: Screenshot capture fails

bash
# Check PIL installation
python3 -c "from PIL import ImageGrab; ImageGrab.grab().show()"

# Install missing dependencies (Linux)
sudo apt-get install python3-tk python3-dev
Issue 3: Encryption key not found

bash
# Ensure keys directory exists
mkdir -p keys

# Check permissions
chmod 700 keys/
Issue 4: Email sending fails

bash
# For Gmail: Enable 2-factor authentication and use App Password
# Set environment variables properly
export SENDER_EMAIL="your_email@gmail.com"
export SENDER_PASSWORD="your_16_char_app_password"
Issue 5: Watchdog not monitoring files

bash
# Verify directory exists
ls ~/Documents

# Check permissions
ls -la ~/Documents
Issue 6: Antivirus quarantines the program

Expected behavior: Security tools detect monitoring software

Solution: Add exception for testing purposes only

Important: This validates that security software is working correctly

📚 Educational Value
Learning Outcomes
Completing this project provides hands-on experience with:

Security Concepts:

Endpoint security monitoring

Attack surface analysis

Threat actor techniques (MITRE ATT&CK)

Detection and prevention strategies

Incident response procedures

Technical Skills:

System-level API interaction

Event-driven programming

Multi-threaded applications

Cryptographic implementations

Network protocols (SMTP, TLS/SSL)

File I/O operations

Error handling and logging

Professional Development:

Ethical hacking principles

Responsible disclosure practices

Legal compliance awareness

Technical documentation

Code organization and structure

Resume Impact
This project demonstrates competencies valued by cybersecurity employers:

Endpoint Security: System monitoring and data collection

Cryptography: Implementation of encryption standards

Python Development: Professional-grade code structure

Security Engineering: Threat modeling and mitigation

Ethical Mindset: Responsible security practices

Target Roles:

Security Analyst / SOC Analyst

Cybersecurity Engineer

Incident Response Analyst

Penetration Tester (Entry-level)

Security Operations Engineer

🚀 Future Enhancements
Beginner Level
 GUI dashboard using Tkinter or PyQt5

 Process monitoring (running applications)

 Network traffic monitoring basics

 HTML report generation

 Log search and filtering

Intermediate Level
 Web-based dashboard (Flask/Django)

 SQLite database integration

 Machine learning for keystroke pattern analysis

 Real-time alerts for specific keywords

 Multiple user profile support

Advanced Level
 Integration with SIEM platforms (Splunk, ELK Stack)

 Build corresponding detection/prevention tool

 Remote administration via secure API

 Cross-platform compatibility (Windows, Linux, Mac)

 Mobile device monitoring (Android/iOS)
Behavioral analysis and anomaly detection

Related Projects to Build
Network packet sniffer (using scapy)
Port scanner and vulnerability checker
Password strength analyzer and cracker
Malware sandbox environment
Intrusion Detection System (IDS)
Web Application Firewall (WAF)
Ransomware simulation and detection
Phishing email detector using ML

🤝 Contributing
Contributions are welcome! Please follow these guidelines:

Fork the repository

Create a feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request

Contribution Guidelines
Follow PEP 8 style guidelines
Add comprehensive docstrings
Include unit tests for new features
Update documentation accordingly
Maintain ethical use standards
Add appropriate legal disclaimers

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

MIT License Summary
✅ Commercial use allowed

✅ Modification allowed

✅ Distribution allowed

✅ Private use allowed

⚠️ No liability or warranty

⚠️ License and copyright notice required

👨‍💻 Author
Your Name: Rohit

GitHub:github.com/rohit01-pro 
Instagram: ex.rohittt
Email: rockee.004@gmail.com

🙏 Acknowledgments
pynput - For excellent keyboard/mouse monitoring library
watchdog - For robust file system monitoring
cryptography - For professional-grade encryption tools
Python Community - For extensive documentation and support
Cybersecurity Community - For ethical hacking resources and guidance

📖 References & Resources
Official Documentation
pynput Documentation
watchdog Documentation
Pillow Documentation
cryptography Documentation
Learning Resources
MITRE ATT&CK Framework

OWASP Top 10

NIST Cybersecurity Framework
Cybersecurity Platforms
TryHackMe - Hands-on cybersecurity training
HackTheBox - Penetration testing labs
CyberDefenders - Blue team challenges

⚠️ Final Warning
This tool is a double-edged sword. While it's an excellent learning resource for understanding endpoint security, it can also cause serious harm if misused.

Remember:

🎓 Learning about security tools != Using them maliciously
⚖️ Knowledge brings responsibility
🤝 Ethical hacking requires permission
📚 Use for good, not evil

Always prioritize:
Consent - Get explicit permission
Transparency - Be open about monitoring
Compliance - Follow all applicable laws
Ethics - Consider the impact on others

📞 Support
If you encounter issues or have questions:
Check the Troubleshooting section
Review closed issues
Open a new issue
Join discussions in the Discussions tab

<div align="center">
Built with rohit01-pro for Cybersecurity Education

⭐ Star this repository if you found it helpful!
Report Bug · Request Feature · Documentation
Remember: With great power comes great responsibility. Use wisely.
</div>
