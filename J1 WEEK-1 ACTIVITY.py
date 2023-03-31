def runAgain():
    print(""" Welcome To Employee Management record
        Enter 1 : To View Employee's List 
        Enter 2 : To Add New Employee 
        Enter 3 : To Search Employee 
        Enter 4 : To Remove Employee
        Enter 5 : to find the salary""")

def option():
    userInput = int(input("Please Select An Above Option: "))
    listStd=[["manu",5,"chnadru@gmail.com.com",9011502851,"mysuru"],

            ["anuradha",6,"anuradhashety@gmail.com",987265352,"Narasipura"],
             
            ["mahadev",7,"manumahadev@gmail.com",9474729030,"bengalore"],
             
            ["akash",8,"akashgowda@gmail.com",9172891102,"HD kote"],
             
            ["hemavathi","hema@gamil.com",987265352,"vijay nagar"],
             
            ["meghana",10,"anjaligeetha@gamil.com",9209155729,"shriranga patna"]]
    n_l=[]
    ssn_l=[]
    for i in range (0,len(listStd)):
        n_l.append(listStd[i][0])
        ssn_l.append(listStd[i][1])
        

    if(userInput == 1): 
        for i in listStd:
            print(i)
            
    elif(userInput == 2):
        n=int(input("enter number of employe's:"))
        for i in range (0,n):
            print("empolyee",i)
            name=input("enter your name:")
            ssn=int(input("enter yuor ssn:"))
            email=input("enter your e_mail id")
            m_no=int(input("enter employee phone number:"))
            address=input("enter the employee address:")
            l=[name,ssn,email,m_no,address]
            listStd.append(l)
        print(l)
        
        
    elif(userInput == 3):
        srcStd = input("Enter Employee Name To Search: ")
        if (srcStd== "manu" or "anuradha" or "mahadev" or "akash" or "hemavathi" or "meghana"):
            print("record is found")
        else:
            print("No Record Found Of Employee {}".format(srcStd))
                         
    elif(userInput == 4):
        print("""list of the empolyees:
                      manu-5
                      anuradha-6
                      mahadev-7
                      akash-8
                      hemavathi-9
                      meghana-10""")   
        n= int(input("Enter the ssn number To Remove the record:"))
        if (n==5 & n in ssn_l):
            r_i=ssn_l.index(n)
            listStd.remove(listStd[r_i])
            print("the employee record is removed")
        elif(n==6 & n in ssn_l):
            r_i=ssn_l.index(n)
            listStd.remove(listStd[r_i])
            print("the employee record is removed")
            print(runAgain())  
        elif(n==7 & n in ssn_l):
            r_i=ssn_l.index(n)
            listStd.remove(listStd[r_i])
            print("the employee record is removed")
            print(runAgain())  
        elif(n==8 & n in ssn_l):
            r_i=ssn_l.index(n)
            listStd.remove(listStd[r_i])
            print("the employee record is removed")
            print(runAgain())  
        elif(n==9 & n in ssn_l):
            r_i=ssn_l.index(n)
            listStd.remove(listStd[r_i])
            print("the employee record is removed")
            print(runAgain())  
        elif(n==10 & n in ssn_l):
            r_i=ssn_l.index(n)
            listStd.remove(listStd[r_i])
            print("the employee record is removed")

    elif(userInput==5):
        u=int(input("enter the  salary:"))
        u1=u/3
        print("The employee tax of the salary is:",u1)        
        
    elif(userInput < 6 and  userInput > 1): 
        print("Please Enter Valid Option")
        
    opt=input("Do you want to know any other details(Y or N): ")
    
    if opt=='Y':
        option()
    else:
        print("Thank You!")
        
runAgain()
option()
      


						



