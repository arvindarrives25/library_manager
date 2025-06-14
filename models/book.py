from models.base import Base

class Book(Base):

    def __init__(self, id, title, author, isbn, available=True):
        super().__init__(id)
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def get_details(self):
        return (
            self.id, self.title, self.author, self.isbn, self.available,
            self.created_at, self.updated_at
        )
