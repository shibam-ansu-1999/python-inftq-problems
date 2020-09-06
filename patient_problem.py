def cal_spe_count(y):

    spe_dict={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
    count_dict={"P":0,"O":0,"E":0}

    for i in range(1,len(y),2):
        count_dict[y[i]]+=1
    max_spe="P"
    max_val=0
    for s,v in count_dict.items():
        if v>max_val:
            max_val=v
            max_sep=s
    return spe_dict[max_sep]

y=[]
n=int(input("Enter the number of patients: "))
for i in range(0,n*2):
    if i%2==0:
        m=input("Enter patient ID number: ")
        y.append(m)
    else:
        m=input("Enter patient specialization (E/O/P): ")
        m=m.upper()
        y.append(m)

print("Name of the speciality is: ",cal_spe_count(y))
