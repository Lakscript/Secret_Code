import random
str=""
encodelist=[]
def secret_code():
    a=input("enter the message: ")
    l=a.split()
    for i in range(0,len(l)):
        q=""
        if len(l[i])==2:
            s=l[i][::-1]
            encodelist.append(s)
        else:
            str=l[i][1:] + l[i][0]
            for i in range(3):
              str += chr(random.choice([random.randint(65, 90),random.randint(97, 122)]))
        
            for i in range(3):
              q += chr(random.choice([random.randint(65, 90),random.randint(97, 122)]))
            str = q + str
            encodelist.append(str)
    
    finalstr=""
    for i in range(0,len(encodelist)):
    
       finalstr=finalstr + " " + encodelist[i]
    print(finalstr)
    


def decode():
    str = input("Enter the secret message: ")
    t = []
    l = str.split()
    sd = ""

    for i in l:
        q = ""
        if len(i) <= 2:
            s = i[::-1]
            t.append(s)

        else:
            q = i[-4] + i[3:-4]
            t.append(q)

    for i in t:
        sd += i + " "

    print(sd)
    

def conti():
    while True:
        try:
            choice = int(input("\nENTER 1 FOR MAKING A SECRET CODE.\nENTER 2 FOR DECODING THE SECRET CODE:\n"))
            if choice == 1:
                secret_code()
            elif choice == 2:
                decode()
            else:
                print("Invalid input. Please enter 1 or 2.")
                continue

            again = input("\nDo you wish to continue? Enter 1 for Yes, 2 for No: ")
            if again == '1':
                continue
            elif again == '2':
                print("Goodbye!")
                break
            else:
                print("Invalid input. Exiting.")
                break
        except ValueError:
            print("Please enter valid numeric input.")

# Start the program
conti()
 