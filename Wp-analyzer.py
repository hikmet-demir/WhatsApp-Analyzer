import os
from dateutil.parser import parse
class WhatsAppAnalyzer:

    def __init__(self):
        self.file_name_input = "WhatsApp Chat with Oryantasyon’18 Saha Ekibi (1).txt"
        self.file_name_output = "trial.txt"
        self.people = {}
        self.messages = []
        self.input_lines = []
        self.group = {}
        self.read_data = ""
        self.output_data = ""
        self.d = {}
        self.merged_lines = []

    def get_files(self):

        self.file_name_input = input("Enter your file name example ( trial.txt) : " ) 
        print()
        
        with open(self.file_name_input,'r', encoding = "utf8") as f:
            self.read_data = f.read()

        self.input_lines = self.read_data.splitlines()

        self.output_data = open(self.file_name_output,'w+',encoding ="utf8")


    def merge_real_line(self):
        merge_lines = []
        for j in self.input_lines:
            if ('/') in j[0:10] and ',' in j[0:10]:
                merge_lines.append(j)
            else:
                merge_lines[-1] = merge_lines[-1] + " " + j
        
        self.input_lines = merge_lines


    def Merge_lines_func(self):
        
       # for i in self.input_lines:
        #    print(i)
        #    print("-")
        
        for line in self.input_lines:
            if ':' in line:
                temp_message = {}
                temp_date = line.split('-')[0]
                try:
                    date = parse(temp_date)
                    temp_message['date'] = date.date()
                    temp_message['time'] = date.time()
                    temp_message['minute'] = date.minute
                    temp_message['hour'] = date.hour
                    temp_message['day'] = date.day
                    temp_message['month'] = date.month
                    temp_message['year'] = date.year

                    index1 = line.find(" - ")
                    index2 = line.find(": ")
                    person = line[index1+3:index2]
                    temp_message['person'] = person

                    message = line[index2+2:]
                    temp_message['message'] = message
                    self.messages.append(temp_message)
                except:
                    print(temp_date)


    def find_message_counts(self):
        for message in self.messages:
            Person_name = message["person"]
            if not Person_name in self.people:
                self.people[ Person_name ] = {}
                self.people[Person_name]["name"] = Person_name
                self.people[Person_name]["Message_Count"] = 0
                self.people[Person_name]["time"] = []
                self.people[Person_name]["date"] = []
                self.people[Person_name]["Night_owl"] = 0
                self.people[Person_name]["Ice_breaker"] = 0
            else:
                self.people[Person_name]["Message_Count"] +=1
                self.people[Person_name]["time"].append(message['time'])
                self.people[Person_name]["date"].append(message['date'])

    def Night_owl_count(self):
        for person in self.people.keys():
            for message_times in self.people[person]["time"]:
                hour  = message_times.hour
                if(hour <= 6):
                    self.people[person]["Night_owl"] +=1

    def Group_timing(self):
        for i in range(0,24):
            self.group[str(i)] = 0
        for i in self.messages:
            hour = i["time"].hour
            self.group[str(hour)] += 1


    def print_outputs(self):
        t = []
        for i in self.people.keys():
            t.append((self.people[i]["Message_Count"],self.people[i]["Night_owl"], i ))
        
        t.sort(reverse=True)
        counter = 0
        for person in t:
             print( "kişi adı: " +person[2]+ " message sayısı === " + str(person[0]) + "//// Night owl count == " + str(person[1]))
             print()
             counter +=1
             if counter >10:
                 break
  

        print("----")
        print("Group Dynamics")
        print("----")

        for i in range(0,24):
            print("In time "+str(i)+":00-" + str(i) +":59 " + "  =  " + str(self.group[str(i)]) + " Message ")

        """for i in messages:
            print(i)"""


    def main(self):
        self.get_files()
        self.merge_real_line()
        self.Merge_lines_func()
        self.find_message_counts()
        self.Night_owl_count()
        self.Group_timing()
        self.print_outputs()


if __name__ == '__main__':
    WhatsAppAnalyzer().main()
