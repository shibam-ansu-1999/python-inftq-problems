airline=input("Enter your airline name[First 2 letters]: ")
source=input("Enter your source name: ")
destination=input("Enter your destination name: ")
count=int(input("Enter no of passengers: "))
ticket_list=[]

def ticket_generator(ai,sou,des,num):
    t_no=101
    ai=ai.upper()
    sou=sou[:3].capitalize()
    des=des[:3].capitalize()
    for i in range(num):
        s=ai+":"+sou+":"+des+":"+str(t_no)
        ticket_list.append(s)
        t_no+=1
    return ticket_list
    

print(ticket_generator(airline,source,destination,count))
    
