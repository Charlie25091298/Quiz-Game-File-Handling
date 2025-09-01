'''file = open("charlie.txt","a")
file.write("5000")
file.close()'''

'''file = open("charlie.txt","r")
read = file.read(4)
print(read)
file.close()'''

'''file = open("charlie.txt","r")
read = file.readlines()
print(read)
file.close()'''

file = open("charlie.txt","r")
read = file.readline()
read = read.split(" ")
print(read)
file.close()
