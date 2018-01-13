with open('inputFile.txt', 'r', encoding="utf8") as f:
    read_data = f.read()

ff = open('outputFile.txt', 'w+', encoding="utf8")

"""with open('WhatsApp Chat with not.txt', 'r', encoding="utf8") as qf:
    read_data = qf.read()
"""

d = {}

lines = read_data.splitlines()
valid_person = False
merged_lines = []
m_track = -1;
#To combine discrete messages
for i in lines:
    #print(i)
    if( len(i) < 11 ):
        merged_lines[m_track] += "\n"+  i
    elif( i[2] == '/' and i[5] == '/' and i[10] == ',' ):
        merged_lines.append(i);
        m_track +=1
    else:
        merged_lines[m_track] += "\n"+  i
#print(merged_lines[-1])

for i in merged_lines:
    #print( i)
    ff.write(i + "\n")

group = {}
for i in range(0,24):
    group[str(i)] = 0



for i in merged_lines:
    temp = i
    index1 = temp.find(" - ", 15, 25)
    index2 = temp.find(": ", 15,70)
    if(index2 != -1): #Eğer ": " indexini bulursa kişi bulmuş demektir bulamamışsa
        #istenmeyen bir kişiyi kişi olarak atadığı için bunu eliyoruz.
        valid_person = True
    if(valid_person):
        person = temp[ index1+3 : index2 ]
        if not person in d:
            #This place for creating dictionary and adding person & their required datas
            d[person] = {}
            d[person]["Message_Count"] = 0
            d[person]["Message_Time"] = []
            d[person]["Night_owl"] = 0
        d[person]["Message_Count"] +=1

        index1 = temp.find(", ",0,30)
        index2 = temp.find(" - ",0,40)
        Message_Time = temp[ index1+2: index2]
        d[person]["Message_Time"].append(Message_Time)
        Message_Time_int = int(Message_Time[0:2])*60 + int(Message_Time[3])
        if(Message_Time_int < 360):
            d[person]["Night_owl"] +=1
        group[str(int(Message_Time_int/60))] += 1

    valid_person = False
for i in d.keys():
    print( "kişi adı: " +i+ " message sayısı === " + str(d[i]["Message_Count"]) + " Night owl count == " + str(d[i]["Night_owl"]))

print("----")
print("Group Dynamics")
print("----")

for i in range(0,24):
    print("In time "+str(i)+":00-" + str(i) +":59 " + "  =  " + str(group[str(i)]) + " Message ")




"""temp = merged_lines[0]
i = temp.find(" - ",15,70)
j = temp.find(": ")
print( temp[i+3:j])"""
