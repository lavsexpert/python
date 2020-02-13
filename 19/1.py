import os

print(os.name)

#for (key, value) in os.environ.items():
#    print(key, "=", value)

print(os.getlogin())
print(os.getpid())
#print(os.uname())

print(os.getcwd())
os.chdir("C:/Users/211ET/Desktop/Python/GitHub/python/18")
print(os.getcwd())

print(os.access("C:/Users/211ET/Desktop/Python/GitHub/python/19/1.py", os.F_OK)) #существование
print(os.access("C:/Users/211ET/Desktop/Python/GitHub/python/19/1.py", os.R_OK)) #доступ на чтение
print(os.access("C:/Users/211ET/Desktop/Python/GitHub/python/19/1.py", os.W_OK)) #доступ на запись
print(os.access("C:/Users/211ET/Desktop/Python/GitHub/python/19/1.py", os.X_OK)) #доступ на исполнение

print(os.listdir(os.getcwd()+"/server"))
#os.mkdir(os.getcwd()+"/test", dir_fd=None)
#os.makedirs(os.getcwd()+"/test/1/2/3")

#os.rename(os.getcwd()+"/test", os.getcwd()+"/new")

#os.rmdir(os.getcwd()+"/new/1/2/3")

#os.removedirs(os.getcwd()+"/new/1")
#print(os.getcwd())

os.truncate(os.getcwd()+"/Задание.txt", 100)

os.chdir("C:/Users/211ET/Desktop/Python/")
#object = os.walk(os.getcwd())
#for item in object:
#    print(item)

#os.system("notepad")
#os.system("calc")

print(os.urandom(1000).decode(encoding="ansi"))




