import random
import pandas as pd


def order_details():
    oid = int(input("Enter your order-id :"))
    st = check_usr(oid )
    if st :
        bk_ordrs = pd.read_csv("/home/aman01/Desktop/pythonPrograms/bakery_mangement/bakery_orders.csv")
        print("your order details are \n",bk_ordrs.loc[bk_ordrs["order_id"]== oid])
    else:
        print("worng user id")


def register():
    ncstmr={
        "name": [input("\nEnter your name: ")],
        "contact_deatils" : [input("Enter your contact details : ")],
        "address" : [input("Enter your address : ")],
        "customer_id" : [random.randint(1000,9999)]
    }
    ncstmr = pd.DataFrame(ncstmr)
    cstmrs = pd.read_csv("/home/aman01/Desktop/pythonPrograms/bakery_mangement/bakery_cstmrs.csv")
    cstmrs = pd.concat([cstmrs,ncstmr])
    cstmrs.to_csv("/home/aman01/Desktop/pythonPrograms/bakery_mangement/bakery_cstmrs.csv")
    print("\nyour registration completed.\nYour id is",ncstmr.iloc[-1,-1])

def place_order():
    cstmr_id = int(input("Enter Your cutomer-ID: "))
    st = check_usr(cstmr_id )
    
    if st:
        print("WELCOME BACK")
        print("place your order sir")
        ordr ={
        "customer_id" : [cstmr_id],
        "order_id" :[random.randint(100,999)],
        "cake": [int(input("Enter quantity of cake at 250/quantity: "))],
        "pastry" : [int(input("Enter quantity of pastry at 100/quantity: "))],
        "biscuit" : [int(input("Enter quantity of buiscuit at 45/quantity: "))]
        }
        ordr = pd.DataFrame(ordr)
        ordr["cake_price"] = ordr["cake"]*250
        ordr["pastry_price"] = ordr["pastry"]*100
        ordr["biscuit_price"] = ordr["biscuit"]*45
        ordr["total_price"] = ordr["cake_price"]+ordr["pastry_price"]+ordr["biscuit_price"]
        print("\n\nYou order is \n " ,ordr.iloc[-1,:])
        ps= input("Press y/n :")
        if ps=="y":
            bk_ordrs = pd.read_csv("/home/aman01/Desktop/pythonPrograms/bakery_mangement/bakery_orders.csv")
            bk_ordrs = pd.concat([bk_ordrs,ordr])
            bk_ordrs.to_csv("/home/aman01/Desktop/pythonPrograms/bakery_mangement/bakery_orders.csv")
            print("your order id is ",ordr.loc[ordr["customer_id"] == cstmr_id,"order_id"])
            print("order placed successfully.")
        else :
             print("you canceled your order.")  
    else:
        print("wrong cutomer id")
    

def check_usr(id): 
    data = pd.read_csv("/home/aman01/Desktop/pythonPrograms/bakery_mangement/bakery_cstmrs.csv")
    ordrs = pd.read_csv("/home/aman01/Desktop/pythonPrograms/bakery_mangement/bakery_orders.csv")
    if id in list(data["customer_id"]) or id in list(ordrs["order_id"]):
        return True

    else:
        return False  
    

    
    
    
            

            


