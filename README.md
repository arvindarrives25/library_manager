# 📚 Library Management System

This is a simple command-line-based **Library Management System** built using **Python** and **MySQL**, following clean modular structure and **Object-Oriented Programming (OOP)** principles. It includes AES encryption for securely handling the database password and logs all operations.

## ✅ Features

- Add Book and Member records
- Enforce consistent formatting for names and emails
- AES-encrypted MySQL credentials via `config.ini`
- Auto-incremented primary key in MySQL table
- Simple logging mechanism
- Modular project structure
- No UI – details are passed via class objects

## 🧱 Project Structure

```
library_manager/
├── main.py
├── config.ini                # Not pushed to GitHub (contains secrets)
├── requirements.txt
├── README.md
├── models/
│   ├── __init__.py
│   ├── base.py               # BaseWorker class (abstract)
│   ├── book.py               # Book class
│   └── member.py             # Member class
├── db/
│   ├── __init__.py
│   └── db_handler.py         # Database operations
├── utils/
│   ├── __init__.py
│   ├── config_loader.py      # Reads config.ini
│   └── crypto_utils.py       # AES encrypt/decrypt
└── logs/
    └── app.log               # Log file
```

## ⚙️ Requirements

Install required packages using:

```bash
pip install -r requirements.txt
```

`requirements.txt` content:

```text
pycryptodome
mysql-connector-python
```

## 🛠️ MySQL Setup

1. Start your MySQL server locally.

2. Create the database and table using this SQL:

```sql
CREATE DATABASE library_db;
USE library_db;

CREATE TABLE IF NOT EXISTS library (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    location VARCHAR(100),
    role VARCHAR(20),
    book_title VARCHAR(100)
);
```

## 🔐 AES Key & Encrypted Password Generation

Use this script to generate your AES key and encrypted password for `config.ini`:

```python
from Crypto.Cipher import AES
import base64
import os

key = os.urandom(32)
key_hex = key.hex()
print("AES Key (hex):", key_hex)

password = "your_mysql_password"
cipher = AES.new(key, AES.MODE_EAX)
nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(password.encode())
enc_password = base64.b64encode(nonce + ciphertext).decode()
print("Encrypted password:", enc_password)
```

## 🧾 Example `config.ini`

```ini
[mysql]
host = localhost
user = root
password = <ENCRYPTED_PASSWORD>
database = library_db
port = 3306

[crypto]
key = <YOUR_AES_KEY_IN_HEX>
```

> ⚠️ Make sure to add `config.ini` to your `.gitignore` so that secrets are not pushed to GitHub.

## 🚀 How to Run

```bash
python main.py
```

## 🧪 Sample Usage

Inside `main.py`:

```python
from db.db_handler import DBHandler
from models.book import Book
from models.member import Member

db = DBHandler()

book = Book("John", "Doe", "Mumbai", "Python 101")
member = Member("Alice", "Smith", "Delhi", "Zero to One")

db.insert_record(book)
db.insert_record(member)
```

## 📝 License



    



  
