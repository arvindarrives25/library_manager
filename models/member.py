from models.base import Base

class Member(Base):

    def __init__(self, id, first_name, last_name, email, membership_type):
        super().__init__(id)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.membership_type = membership_type

    def get_details(self):
        return (
            self.id, self.first_name, self.last_name, self.email, self.membership_type,
            self.created_at, self.updated_at
        )