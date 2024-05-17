import os
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def scan_system():
    os.system("sudo apt-get update && sudo apt-get install -y lynis")
    os.system("lynis audit system --cronjob")

def send_email(subject, body, to_email):
    from_email = "temporarymessage0@gmail.com"
    password = "QxPnTGV23"  # Получение пароля из переменной окружения

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        logging.info("Email sent successfully.")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")

def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("Scanning the system for vulnerabilities...")
    
    try:
        scan_system()
        logging.info("System scan completed.")
    except Exception as e:
        logging.error(f"Failed to scan the system: {e}")

    subject = "System Vulnerability Scan Report"
    body = "Please check the attached report."
    to_email = "Nikitas0408@gmail.com"

    send_email(subject, body, to_email)
    logging.info("The report has been sent to the administrator's email.")

if __name__ == "__main__":
    main()
