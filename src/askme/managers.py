import os
from .models import User, Question
from .utils import read_file_lines, write_file_lines, input_int

# [cite: 141, 143, 145]
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")

class UsersManager:
    # [cite: 181]
    def __init__(self):
        self.file_path = os.path.join(DATA_DIR, "users.txt")
        self.users = {} 
        self.last_id = 0
        self.load()

    def load(self):
        # [cite: 183]
        lines = read_file_lines(self.file_path)
        self.users.clear()
        for line in lines:
            user = User.from_line(line)
            if user:
                self.users[user.username] = user
                self.last_id = max(self.last_id, user.user_id)

    def save_user(self, user):
        # [cite: 184]
        if user.user_id == -1:
            self.last_id += 1
            user.user_id = self.last_id
        self.users[user.username] = user
        write_file_lines(self.file_path, [user.to_line()], append=True)

    def get_user(self, username, password):
        if username in self.users:
            user = self.users[username]
            if user.password == password:
                return user
        return None
    
    def get_user_by_id(self, user_id):
        for user in self.users.values():
            if user.user_id == user_id:
                return user
        return None
    
    def is_username_exist(self, username):
        return username in self.users

class QuestionsManager:
    # [cite: 147]
    def __init__(self):
        self.file_path = os.path.join(DATA_DIR, "questions.txt")
        self.questions = {} 
        self.last_id = 0
        self.load()

    def load(self):
        # [cite: 173]
        lines = read_file_lines(self.file_path)
        self.questions.clear()
        for line in lines:
            q = Question.from_line(line)
            if q:
                self.questions[q.question_id] = q
                self.last_id = max(self.last_id, q.question_id)

    def save_question(self, question):
        if question.question_id == -1:
            self.last_id += 1
            question.question_id = self.last_id
        self.questions[question.question_id] = question
        write_file_lines(self.file_path, [question.to_line()], append=True)
    
    def update_database(self):
        lines = [q.to_line() for q in self.questions.values()]
        write_file_lines(self.file_path, lines, append=False)

    def print_to_questions(self, user):
        # [cite: 175]
        print("\n--- Questions For You ---")
        found = False
        for q in self.questions.values():
            if q.to_user == user.user_id and q.parent_id == -1:
                found = True
                sender = "Anonymous" if q.is_anonymous else f"User {q.from_user}"
                print(f"ID: {q.question_id} | From: {sender} | Question: {q.text}")
                self._print_thread(q.question_id)
        if not found:
            print("No questions found.")

    def print_from_questions(self, user):
        # [cite: 176]
        print("\n--- Questions From You ---")
        found = False
        for q in self.questions.values():
            if q.from_user == user.user_id and q.parent_id == -1:
                found = True
                print(f"ID: {q.question_id} | To User: {q.to_user} | Question: {q.text}")
                self._print_thread(q.question_id)
        if not found:
            print("No questions sent.")

    def _print_thread(self, parent_id):
        for q in self.questions.values():
            if q.parent_id == parent_id:
                print(f"\tAnswer: {q.text}")

    def ask_question(self, from_user, users_manager):
        # [cite: 177]
        to_user_id = input_int("Enter User ID to ask: ")
        target_user = users_manager.get_user_by_id(to_user_id)
        
        if not target_user:
            print("User not found.")
            return

        is_anon = False
        if target_user.allow_anonymous:
            is_anon = input_int("Ask anonymously? (0: No, 1: Yes): ", 0, 1) == 1
        else:
            print("Note: This user does not allow anonymous questions.")

        text = input("Enter question text: ")
        q = Question(parent_id=-1, from_user=from_user.user_id, to_user=to_user_id, is_anonymous=is_anon, text=text)
        self.save_question(q)
        print("Question sent.")

    def answer_question(self, user):
        # [cite: 178]
        q_id = input_int("Enter Question ID to answer: ")
        if q_id not in self.questions:
            print("Question not found.")
            return
        
        parent_q = self.questions[q_id]
        if parent_q.to_user != user.user_id:
            print("Error: You can only answer questions sent to you.")
            return

        text = input("Enter answer text: ")
        ans = Question(parent_id=q_id, from_user=user.user_id, to_user=parent_q.from_user, is_anonymous=False, text=text)
        self.save_question(ans)
        print("Answer saved.")

    def delete_question(self, user):
        # [cite: 179]
        q_id = input_int("Enter Question ID to delete: ")
        if q_id not in self.questions:
            print("Question not found.")
            return

        q = self.questions[q_id]
        if q.from_user != user.user_id and q.to_user != user.user_id:
            print("Error: You can only delete your questions.")
            return

        del self.questions[q_id]
        
        ids_to_remove = [k for k, v in self.questions.items() if v.parent_id == q_id]
        for pid in ids_to_remove:
            del self.questions[pid]
            
        self.update_database()
        print("Question deleted.")

    def list_feed(self):
        # [cite: 180]
        print("\n--- Feed ---")
        for q in self.questions.values():
            if q.parent_id == -1: 
                print(f"Question ID: {q.question_id} | From: {q.from_user} To: {q.to_user}")
                print(f"Question: {q.text}")
                self._print_thread(q.question_id)
                print("-" * 20)