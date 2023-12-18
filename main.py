import bakery_process
import os
import time


while(True):
    print("\n\n-------WELCOME OT SOFTBAKERY--------")
    resp  = input("\n\nFor REGISTRATION PRESS r/R \nFOR PLACING ORDER PRESS o/O \nFOR ORDER DETAIL PRESS d/D\nFOR EXIT press   e/E\nEnter key :  ")
    
    if resp == "r" or resp =="R":
        os.system("clear") 
        bakery_process.register()
        res = input("\n\nFOR GONG BACK PRESS b/B\n TO EXIT PREE E/e :")
    
        if res == "b" or res== "B":
            os.system("clear") 
            continue  
        elif res == "e" or res== "E":
            break
        else:
            continue
            
        
        
        
            
    elif resp == "o" or resp == "O":
        os.system("clear") 
        bakery_process.place_order()
        
        res = input("\n\nFOR GONG BACK PRESS b/B\nTO EXIT PREES  E/e  : ")
    
        if res == "b" or res== "B":
            os.system("clear") 
            continue  
        elif res == "e" or res== "E":
            break
        else:
            continue
            
        

    elif resp == "d"  or resp == "D":
        os.system("clear")  
        bakery_process.order_details() 
        res = input("\n\nFOR GONG BACK PRESS b/B\n TO EXIT PREE E/e : ")
    
        if res == "b" or res== "B":
            os.system("clear") 
            continue  
        elif res == "e" or res== "E":
            break
        else:
            continue
            
        
        

    elif resp == "e"  or resp == "E":
        print("Please come again")
        break;      
    
    else:
        print("Pease press appropriate key")
        time.sleep(3)
        os.system("cls||clear")
        continue    