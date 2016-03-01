##############################################
####WHATSAPP CONVERSATIONS TO JEKYLL POSTS####
##########BY ABDULRAHMAN ALAMOUDI#############
##############################################
file_destination = open('whatsapp.txt','r')
file_output = open('output.txt','a')

colon = 0
container_one = ""
container_two = ""
data = []
for line in file_destination.readlines():
    if line[4:8] == "/16," or line[3:7] == "/16," or line[5:9] == "/16,":
        container_one += "`"
        data.append(container_one + container_two + "\n")
    for i in line.split():
        control_space = 0
        if i[-4:] == "/16,":
            colon = 0
            container_one = ""
            container_one += "`"
            container_two = ""
        for x in i:
            if colon <= 3:
                container_one += x
                if control_space != len(i)-1:
                    control_space += 1
                else:
                    container_one += " "
            else:
                container_two += x
                if control_space != len(i)-1:
                    control_space += 1
                else:
                    container_two += " "
            if x == ":":
                colon += 1
data.append(container_one + container_two)
file_destination.close()

for g in data[1:]:
   print(g)
    ask_user = input("""press "SPACE" and "ENTER" to pick it. to skip press ANY key. """)
    if ask_user == chr(32):
        file_output.write(g + "\n")
    else:
        pass
    
file_output.close()

