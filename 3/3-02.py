#file1 = open("text.txt")
#read = file1.read(3)
#print(read)
#read2 = file1.read(3)
#print(read2)
#read3 = file1.readline()
#print(read3)
#file1.close()

#file2 = open("text.txt")
#for i in file2:
#    print(i.replace("\n",""))
#file2.close()

file0 = open("text.txt")
text = file0.read()
file0.close()
print("-----")

file3 = open("text.txt", "w")
file3.write(text)
file3.write("\nfour")
file3.write("\nfive")
file3.write("\nsix")
file3.close()

file4 = open("text.txt")

len(name)
print(file4.read())
