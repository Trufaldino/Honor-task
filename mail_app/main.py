import os
from dotenv import load_dotenv
import imaplib
import email
import os
import schedule
import time
from logger import logger
from db import Attachment, Session


load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
IMAP_SERVER = os.getenv("IMAP_SERVER")
IMAP_PORT = int(os.getenv("IMAP_PORT"))
ATTACHMENTS_DIR = os.getenv("ATTACHMENTS_DIR")


def download_attachments():
    """
    Download email attachments and save them to the specified directory.
    """
    mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
    mail.login(EMAIL, PASSWORD)
    mail.select("inbox")

    result, data = mail.search(None, "(UNSEEN)")
    if not data[0]:
        logger.info("No emails with attachments found")
        mail.close()
        mail.logout()
        return

    for num in data[0].split():
        result, data = mail.fetch(num, "(RFC822)")
        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)

        for part in msg.walk():
            if part.get_content_maintype() == "multipart":
                continue
            if part.get("Content-Disposition") is None:
                continue

            filename = part.get_filename()
            if filename:
                filepath = os.path.join(ATTACHMENTS_DIR, filename)
                with open(filepath, "wb") as f:
                    f.write(part.get_payload(decode=True))
                logger.info(f"File '{filename}' downloaded and saved successfully")
    mail.close()
    mail.logout()


def upload_attachments_to_db():
    """
    Upload files from the specified directory to the database.
    """
    session = Session()
    files = os.listdir(ATTACHMENTS_DIR)
    for file in files:
        filepath = os.path.join(ATTACHMENTS_DIR, file)
        attachment = Attachment(filename=file, path=filepath)
        session.add(attachment)
        session.commit()
        logger.info(f"Attachment '{file}' uploaded to the database successfully")
    session.close()


def main():
    """
    Main function to run the application.
    """
    if not os.path.exists(ATTACHMENTS_DIR):
        os.makedirs(ATTACHMENTS_DIR)

    schedule.every().day.at("12:00").do(download_attachments)
    schedule.every().day.at("12:00").do(upload_attachments_to_db)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
