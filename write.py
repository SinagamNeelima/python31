file=open("txtfile.txt","w")
file.write("this is my file\n")
file.close()
file=open("txtfile.txt","r")
con=file.read()
print(con)
file.close()