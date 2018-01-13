with open('WhatsApp Chat with Başak.txt', 'r', encoding="utf8") as f:
    read_data = f.read()

ff = open('outputFile.txt', 'w+', encoding="utf8")


d = {}
people = {}
lines = read_data.splitlines()
merged_lines = []
messages = []

group = {}



def Merge_lines_func():
    m_track = -1
    for i in lines:
        if( len(i) < 11 ):
            merged_lines[m_track] += "\n"+  i
        elif( i[2] == '/' and i[5] == '/' and i[10] == ',' ):
            merged_lines.append(i);
            m_track +=1
        else:
            merged_lines[m_track] += "\n"+  i

    for i in merged_lines:
        ff.write(i + "\n")

def find_message_counts():
    for i in messages:
        Person_name = i["from"]
        if not Person_name in people:
            people[ Person_name ] = {}
            people[Person_name]["name"] = Person_name
            people[Person_name]["Message_Count"] = 0
            people[Person_name]["Message_Time"] = []
            people[Person_name]["Message_date"] = []
            people[Person_name]["Night_owl"] = 0
            people[Person_name]["Ice_breaker"] = 0
        people[Person_name]["Message_Count"] +=1
        people[Person_name]["Message_Time"].append(i["time"])
        people[Person_name]["Message_date"].append(i["date"])

def Night_owl_count():
    for i in people.keys():
        for k in people[i]["Message_Time"]:
            Message_Time_int = int(k[0:2])*60 + int(k[3])
            if(Message_Time_int < 360):
                people[i]["Night_owl"] +=1

def Group_timing():
    for i in range(0,24):
        group[str(i)] = 0
    for i in messages:
        hour = int(i["time"][0:2])
        group[str(hour)] += 1

def create_messages():
    for i in merged_lines:
        temp = i
        index1 = temp.find(" - ", 15, 25)
        index2 = temp.find(": ", 15,70)
        if(index2 == -1):
            None
        else:
            temp_dict = {}
            person = temp[ index1+3 : index2 ]
            temp_dict["from"] = person

            index1 = temp.find(", ",0,30)
            index2 = temp.find(" - ",0,40)
            Message_Time = temp[ index1+2: index2]
            temp_dict["time"] = Message_Time

            index1 = temp.find(": ")
            Message_text = temp[index1+2:]
            temp_dict["text"] = Message_text

            index1 = temp.find(", ")
            Message_date = temp[:index1]
            temp_dict["date"] = Message_date

            messages.append(temp_dict)

def print_outputs():
    for i in people.keys():
        print( "kişi adı: " +i+ " message sayısı === " + str(people[i]["Message_Count"]) + "//// Night owl count == " + str(people[i]["Night_owl"]))

    print("----")
    print("Group Dynamics")
    print("----")

    for i in range(0,24):
        print("In time "+str(i)+":00-" + str(i) +":59 " + "  =  " + str(group[str(i)]) + " Message ")

    """for i in messages:
        print(i)"""

def main():
    Merge_lines_func()
    create_messages()
    find_message_counts()
    Night_owl_count()
    Group_timing()
    print_outputs()

if __name__ == '__main__':
    main()
