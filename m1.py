print("""Welcome To Software Company
         select project department no for its details
         Planning-1
         Execution-2
         Monitoring & Controling-3
         Risk Management-4""")
a=int(input("enter department no"))
if a==1:
    l=[]
    for i in range(1,5):
        print(i)
        name=input("enter member name")
        age=int(input("enter member age"))
        pno=int(input("enter member p no"))
        address=input("enter member address")
        c=[name,age,pno,address]
        l.append(c)
    print("""Planning department has 4 members
             select member no for their details
             member1-1
             member2-2
             member3-3
             member4-4""")
    b=int(input("enter member no"))
    if b==1:
        print("Member Name:",l[0][0])
        print("Member Age:",l[0][1])
        print("Member Phno:",l[0][2])
        print("Member Address:",l[0][3])
    elif b==2:
        print("Member Name:",l[1][0])
        print("Member Age:",l[1][1])
        print("Member Phno:",l[1][2])
        print("Member Address:",l[1][3])
    elif b==3:
        print("Member Name:",l[2][0])
        print("Member Age:",l[2][1])
        print("Member Phno:",l[2][2])
        print("Member Address:",l[2][3])
    elif b==4:
        print("Member Name:",l[3][0])
        print("Member Age:",l[3][1])
        print("Member Phno:",l[3][2])
        print("Member Address:",l[3][3])

elif a==2:
    l=[]
    for i in range(1,5):
        print(i)
        name=input("enter member name")
        age=int(input("enter member age"))
        pno=int(input("enter member p no"))
        address=input("enter member address")
        c=[name,age,pno,address]
        l.append(c)
    print("""Execution department has 4 members
             select member no for their details
             member1-1
             member2-2
             member3-3
             member4-4""")
    b=int(input("enter member no"))
    if b==1:
        print("Member Name:",l[0][0])
        print("Member Age:",l[0][1])
        print("Member Phno:",l[0][2])
        print("Member Address:",l[0][3])
    elif b==2:
        print("Member Name:",l[1][0])
        print("Member Age:",l[1][1])
        print("Member Phno:",l[1][2])
        print("Member Address:",l[1][3])
    elif b==3:
        print("Member Name:",l[2][0])
        print("Member Age:",l[2][1])
        print("Member Phno:",l[2][2])
        print("Member Address:",l[2][3])
    elif b==4:
        print("Member Name:",l[3][0])
        print("Member Age:",l[3][1])
        print("Member Phno:",l[3][2])
        print("Member Address:",l[3][3])


elif a==3:
    l=[]
    for i in range(1,4):
        print(i)
        name=input("enter member name")
        age=int(input("enter member age"))
        pno=int(input("enter member p no"))
        address=input("enter member address")
        c=[name,age,pno,address]
        l.append(c)
    print("""M & C department has 3 members
             select member no for their details
             member1-1
             member2-2
             member3-3""")
    b=int(input("enter member no"))
    if b==1:
        print("Member Name:",l[0][0])
        print("Member Age:",l[0][1])
        print("Member Phno:",l[0][2])
        print("Member Address:",l[0][3])
    elif b==2:
        print("Member Name:",l[1][0])
        print("Member Age:",l[1][1])
        print("Member Phno:",l[1][2])
        print("Member Address:",l[1][3])
    elif b==3:
        print("Member Name:",l[2][0])
        print("Member Age:",l[2][1])
        print("Member Phno:",l[2][2])
        print("Member Address:",l[2][3])


if a==4:
    l=[]
    for i in range(1,5):
        print(i)
        name=input("enter member name")
        age=int(input("enter member age"))
        pno=int(input("enter member p no"))
        address=input("enter member address")
        c=[name,age,pno,address]
        l.append(c)
    print("""Risk Management department has 4 members
             select member no for their details
             member1-1
             member2-2
             member3-3
             member4-4""")
    b=int(input("enter member no"))
    if b==1:
        print("Member Name:",l[0][0])
        print("Member Age:",l[0][1])
        print("Member Phno:",l[0][2])
        print("Member Address:",l[0][3])
    elif b==2:
        print("Member Name:",l[1][0])
        print("Member Age:",l[1][1])
        print("Member Phno:",l[1][2])
        print("Member Address:",l[1][3])
    elif b==3:
        print("Member Name:",l[2][0])
        print("Member Age:",l[2][1])
        print("Member Phno:",l[2][2])
        print("Member Address:",l[2][3])
    elif b==4:
        print("Member Name:",l[3][0])
        print("Member Age:",l[3][1])
        print("Member Phno:",l[3][2])
        print("Member Address:",l[3][3])
        
