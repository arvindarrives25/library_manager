import mysql.connector
from configparser import ConfigParser
from utils.crypto_utils import decrypt_password
from utils.logger import logger
import os

class DBHandler:
    def __init__(self):
        config = ConfigParser()
        config.read(os.path.join("config", "config.ini"))
        password = decrypt_password(config["mysql"]["password"], config["crypto"]["key"])

        self.conn = mysql.connector.connect(
            host=config["mysql"]["host"],
            user=config["mysql"]["user"],
            password=password,
            database=config["mysql"]["database"],
            port=int(config["mysql"]["port"])
        )
        self.cursor = self.conn.cursor()

    def insert_book(self, book):
        try:
            self.cursor.execute("SELECT * FROM books WHERE id=%s", (book.id,))
            if self.cursor.fetchone():
                logger.warning(f"Book with ID {book.id} already exists.")
                return
            self.cursor.execute(
                "INSERT INTO books VALUES (%s, %s, %s, %s, %s, %s, %s)",
                book.get_details()
            )
            self.conn.commit()
            logger.info(f"Book '{book.title}' added.")
        except Exception as e:
            logger.error(f"Error inserting book: {e}")

    def insert_member(self, member):
        try:
            self.cursor.execute("SELECT * FROM members WHERE id=%s", (member.id,))
            if self.cursor.fetchone():
                logger.warning(f"Member with ID {member.id} already exists.")
                return
            self.cursor.execute(
                "INSERT INTO members VALUES (%s, %s, %s, %s, %s, %s, %s)",
                member.get_details()
            )
            self.conn.commit()
            logger.info(f"Member '{member.email}' added.")
        except Exception as e:
            logger.error(f"Error inserting member: {e}")
