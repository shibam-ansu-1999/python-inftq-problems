#gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]
#price_list=[1760,2119,1599,3920,3999]

def calculate_price(reqd_gems,reqd_qnt):
    gems_price={"Emerald":1760,"Ivory":2119,"Jasper":1599,"Ruby":3920,"Garnet":3999}
    total_price=0
    for i in range(len(reqd_gems)):
        gem=reqd_gems[i]
        
        if reqd_gems[i]in gems_price:
            total_price+=gems_price.get(gem)*reqd_qnt[i]     
        else:
            return -1
           
    
    if total_price>30000:
        total_price=total_price-(total_price*0.05)
        
    return total_price

reqd_gems=["Ivory","Emerald","Garnet"]
reqd_qnt=[3,10,12]

print("The total amount you have to pay is:",calculate_price(reqd_gems,reqd_qnt))
    


