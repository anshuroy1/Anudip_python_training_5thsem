# 2. Write a program to copy entire content from one file into another
f1 = open("classwork/file_handling_10th_june/sentence.txt", "r")
f2 = open("classwork/file_handling_10th_june/copy.txt", "w")
data = f1.read()
f2.write(data)
f1.close()
f2.close()

