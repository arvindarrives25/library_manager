from db.db_handler import DBHandler
from models.book import Book
from models.member import Member

if __name__ == "__main__":
    db = DBHandler()

    book = Book(1, "The Alchemist", "Paulo Coelho", "9780061122415")
    db.insert_book(book)

    member = Member(1, "Alice", "Smith", "alice.smith@example.com", "Gold")
    db.insert_member(member)
