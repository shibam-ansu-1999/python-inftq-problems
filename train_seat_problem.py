test_case=int(input("Enter Number of seats: "))

remainder=([0,1,6,7],[3,4,9,10])

seat_set=(1,2,3,4,5,6,7,8,9,10,11,12)

seat=[]

for i in range(test_case):
    seat.append(int(input("Enter the seat {} No:".format(i+1))))

for i in seat:
    denom=i//12
    rem=i%12

    if rem in remainder[0]:
        seat_type='WS'
    elif rem in remainder[1]:
        seat_type='AS'
    else:
        seat_type='MS'
    
    if rem!=0:
        print('{} {}'.format(seat_set[-rem]+denom*12,seat_type))
    else:
        print('{} {}'.format(seat_set[rem]+(denom-1)*12,seat_type))
    





