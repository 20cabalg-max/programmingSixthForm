
details = []
while True:
    choice=input("Do you want to enter another membership.")
    if choice=="No":
        break
    else:
        print("**************************************************************************")
        name=input("Enter name you wrote when doing your membership.")
        date=input("Enter date of birth.")
        print("**************************************************************************")
        print(name,date)
        result=input("Is this what you wrote.")
        print("**************************************************************************")
        details.append([name,date])
        myFile=open("dataEntry.txt","a")
        myFile.write(str(details))
        myFile.close()
        #myFile.open("dataEntry.txt","a")
        #myFile.write(name,date)
        #myFile.close()

userDetails=input("Do you want to search for user details.")
if userDetails=="Yes":
    line=input("")