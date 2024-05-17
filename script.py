import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def scan_system():
    os.system("sudo apt-get install lunis")
    os.system("lynis audit system --cronjob")

def send_email(subject, body, to_email):
    from_email = "temporarymessage0@gmail.com"
    password = "QxPnTGV23"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('Nikitas0408@gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

def main():
    print("Сканирование системы на наличие уязвимостей...")
    scan_system()
    
    subject = "Отчет о сканировании системы на уязвимости"
    body = "Пожалуйста, проверьте прикрепленный отчет."
    to_email = "Nikitas0408@gmail.com"

    send_email(subject, body, to_email)
    print("Отчет отправлен на почту администратору.")

if __name__ == "__main__":
    main()
