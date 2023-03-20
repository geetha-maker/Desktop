print ("""select the option as you need
petrol-1
diesel-2""")
a=int(input("enter option no"))
if a==1:
    print("""select the option
    to check petrol details-1
    to find amount of petrol for your vehical-2""")
    b=int(input("enter option no"))
    if b==1:
        print({"date":"14.03.2023","time":"6am","petrol per liter":"101.72"})
    elif b==2:
        n=int(input("how many vehicals"))
        l1=[]
        for i in range(1,n+1):
            ta1=0
            print(i)
            p=101.72
            l=int(input("enter liter of petrol needed"))
            ta=p*l
            if i==1:
                print(ta)
            elif i>1:
                ta1=ta1+ta*i
                print("total amount",ta1)
elif a==2:
    print("""select the option
    to check diesel details-1
    to find amount of disel for your vehical-2""")
    b=int(input("enter option no"))
    if b==1:
        print({"date":"14.03.2023","time":"6am","petrol per liter":"87.71"})
    elif b==2:
        n=int(input("how many vehicals"))
        l1=[]
        for i in range(1,n+1):
            ta1=0
            print(i)
            p=87.71
            l=int(input("enter liter of petrol needed"))
            ta=p*l
            if i==1:
                print(ta)
            elif i>1:
                ta1=ta1+ta*i
                print("total amount",ta1)

            
                
