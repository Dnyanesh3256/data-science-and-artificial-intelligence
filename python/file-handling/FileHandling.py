# open file in read(default) mode

# p = open(r"C:\Users\LENOVO\Downloads\DnyaneshwarTupe.txt")

# print(p.read())

# newFile = open(r"D:\data-science-and-artificial-intelligence\python\file-handling\test.txt", "w")

# newFile.write("hello this is file creation practical")

# newFile = open(r"D:\data-science-and-artificial-intelligence\python\file-handling\test.txt", "a")

# newFile.write(" and now i am appending some context in the file")

newFile = open(r"D:\data-science-and-artificial-intelligence\python\file-handling\test2.txt", "x")

newFile.write("hello this is test2")

newFile.close()