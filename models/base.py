from datetime import datetime

class Base:
    def __init__(self, id):
        self.id = id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()