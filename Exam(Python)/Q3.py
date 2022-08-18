
grade = int(input("Enter your Average marks : "))

if grade<=100 and grade>=91:
    print("A1")
elif grade<=90 and grade>=81:
    print("A2")
elif grade<=80 and grade>=71:
    print("B1")
elif grade<=70 and grade>=61:
    print("B2")
elif grade<=60 and grade>=51:
    print("C1")
elif grade<=50 and grade>=41:
    print("C2")
elif grade<=40 and grade>=33:
    print("D")
elif grade<=32 and grade>=21:
    print("E1")
elif grade<=20 and grade>=0:
    print("E2")