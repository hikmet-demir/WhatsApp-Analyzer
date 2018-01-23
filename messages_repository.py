from message import Message
from message_type import MessageType


class MessagesRepository:

    def __init__(self, file_path = "_chat.txt"):
        with open(file_path, 'r', encoding="utf8") as f:
            read_data = f.read()
            print(file_path + " read!")

            lines = read_data.splitlines()

            merged_lines = self.merge_lines(lines)

            self.messages = self.create_messages(merged_lines)
            print("Messages created!")

    def get_messages(self):
        return self.messages

    def merge_lines(self, lines):
        merged_lines = []
        m_track = -1
        for i in lines:
            if (len(i) < 11):
                merged_lines[m_track] += "\n" + i
            elif (i[0] == '['):
                merged_lines.append(i)
                m_track += 1
            else:
                merged_lines[m_track] += "\n" + i

        return merged_lines

    def create_messages(self, merged_lines):
        messages = []
        for i in merged_lines:
            temp = i
            index1 = temp.find(" - ", 15, 25)
            index2 = temp.find(": ", 15,70)
            if(index2 == -1):
                None
            else:
                person = temp[ index1+3 : index2 ]

                index1 = temp.find(", ",0,30)
                index2 = temp.find(" - ",0,40)
                time = temp[ index1+2: index2]

                index1 = temp.find(": ")
                text = temp[index1+2:]

                index1 = temp.find(", ")
                date = temp[:index1]

                message = Message(
                    sender=person,
                    date=date,
                    time=time,
                    text=text,
                    type=MessageType.TEXT
                )

                messages.append(message)

        return messages
