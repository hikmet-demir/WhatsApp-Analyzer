
from message_type import MessageType

class Message:

    def __init__(self, sender, text, date, time, type = MessageType.TEXT):
        self.time = time
        self.date = date
        self.text = text
        self.sender = sender
        self.type = type
