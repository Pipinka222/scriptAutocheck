import os
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def scan_system():
    logging.info("Обновление списка пакетов и установка Lynis...")
    os.system("sudo apt-get update && sudo apt-get install -y lynis")
    logging.info("Запуск аудита Lynis...")
    os.system("lynis audit system --cronjob > /tmp/lynis_report.txt")
    logging.info("Аудит Lynis завершен.")

def send_email(subject, body, to_email):
    from_email = "SecurityNotifications@yandex.ru"
    password = os.getenv('YANDEX_PASSWORD')  # Получение пароля из переменной окружения

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with open('/tmp/lynis_report.txt', 'r') as file:
            attachment = MIMEText(file.read())
            attachment.add_header('Content-Disposition', 'attachment', filename='lynis_report.txt')
            msg.attach(attachment)

        server = smtplib.SMTP('smtp.yandex.ru', 587)
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        logging.info("Email успешно отправлен.")
    except Exception as e:
        logging.error(f"Не удалось отправить email: {e}")

def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("Начало сканирования системы на уязвимости...")

    try:
        scan_system()
        logging.info("Сканирование системы завершено.")
    except Exception as e:
        logging.error(f"Не удалось сканировать систему: {e}")

    subject = "Отчет о сканировании системы на уязвимости"
    body = "Пожалуйста, проверьте прикрепленный отчет."
    to_email = "Nikitas0408@gmail.com"

    send_email(subject, body, to_email)
    logging.info("Отчет отправлен на email администратора.")

if __name__ == "__main__":
    main()
