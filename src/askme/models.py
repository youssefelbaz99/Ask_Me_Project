class Question:
    # [cite: 98]
    def __init__(self, question_id=-1, parent_id=-1, from_user=-1, to_user=-1, is_anonymous=False, text=""):
        # [cite: 99]
        self.question_id = question_id
        self.parent_id = parent_id
        self.from_user = from_user
        self.to_user = to_user
        self.is_anonymous = is_anonymous
        self.text = text

    @classmethod
    def from_line(cls, line):
        # [cite: 101]
        if not line or line.strip() == "":
            return None
        parts = line.split('|')
        if len(parts) < 6:
            return None
        
        is_anon = (parts[4] == '1')
        return cls(int(parts[0]), int(parts[1]), int(parts[2]), int(parts[3]), is_anon, parts[5])

    def to_line(self):
        # [cite: 102]
        is_anon_str = '1' if self.is_anonymous else '0'
        return f"{self.question_id}|{self.parent_id}|{self.from_user}|{self.to_user}|{is_anon_str}|{self.text}"

class User:
    # [cite: 114]
    def __init__(self, user_id=-1, username="", password="", name="", email="", allow_anonymous=True):
        # [cite: 115]
        self.user_id = user_id
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.allow_anonymous = allow_anonymous

    @classmethod
    def from_line(cls, line):
        # [cite: 117]
        if not line or line.strip() == "":
            return None
        parts = line.split('|')
        if len(parts) < 6:
            return None
        
        allow_anon = (parts[5] == '1')
        return cls(int(parts[0]), parts[1], parts[2], parts[3], parts[4], allow_anon)

    def to_line(self):
        # [cite: 118]
        allow_anon_str = '1' if self.allow_anonymous else '0'
        return f"{self.user_id}|{self.username}|{self.password}|{self.name}|{self.email}|{allow_anon_str}"