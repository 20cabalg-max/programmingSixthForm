myfile=open("quote.txt", "r")

x=myfile.readline()
myfile.close()
print(x)

myfile.open("quote.txt", "a")
myfile.write("Donut\n")
myfile.close()