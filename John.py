ofile = open('John.txt', 'w')
userName = raw_input("Enter your name:")
nameList = [str(userName)]
ofile.write(str(nameList))
while userName!= "John":
        userName = raw_input("Enter your name:") 
        nameList2 = [str(userName)]
        ofile.write(str(nameList2))
ofile.close()

f = open('John.txt', 'r+')
print("Incorrect names:")
for list in f:
    print(list)
f.close()


        

                      

    
