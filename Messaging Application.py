from abc import ABC, abstractmethod
from datetime import datetime

class User:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info

class Conversation:
    def __init__(self, users):
        self.users = users
        self.history = []

    def add_message(self, message):
        self.history.append(message)

class Message(ABC):
    def __init__(self, sender, conversation, content):
        self.sender = sender
        self.conversation = conversation
        self.content = content
        self.timestamp = datetime.now()

    @abstractmethod
    def display(self):
        pass

class TextMessage(Message):
    def display(self):
        print(f"{self.timestamp} {self.sender.name}: {self.content}")

class MultimediaMessage(Message):
    def __init__(self, sender, conversation, content, media_file):
        super().__init__(sender, conversation, content)
        self.media_file = media_file

    def display(self):
        print(f"{self.timestamp} {self.sender.name}: {self.content} [{self.media_file}]")

class MessagingApp:
    def __init__(self):
        self.users = []
        self.conversations = []

    def create_user(self, name, contact_info):
        user = User(name, contact_info)
        self.users.append(user)
        return user

    def create_conversation(self, users):
        conversation = Conversation(users)
        self.conversations.append(conversation)
        return conversation

    def send_message(self, sender, conversation, content, media_file=None):
        if media_file:
            message = MultimediaMessage(sender, conversation, content, media_file)
        else:
            message = TextMessage(sender, conversation, content)

        conversation.add_message(message)
        return message

    def display_conversation_history(self, conversation):
        for message in conversation.history:
            message.display()



app = MessagingApp()

user1 = app.create_user("Gevorg", "gevorg@yandex.com")
user2 = app.create_user("Larisa", "larisa@gmail.com")
user3 = app.create_user("Anjelika", "anjelika@mail.ru")

conversation1 = app.create_conversation([user1, user2])
conversation2 = app.create_conversation([user1, user3])

message1 = app.send_message(user1, conversation1, "Hello, Gevorg!")
message2 = app.send_message(user2, conversation1, "Hi, Larisa!")
message3 = app.send_message(user1, conversation2, "Hey, Lika!")

print("Conversation 1:")
app.display_conversation_history(conversation1)

print("\nConversation 2:")
app.display_conversation_history(conversation2)
