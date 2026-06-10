#program to input 10 sentences from the user and them to a file
#open the file in write mode
f = open("classwork/file_handling_10th_june/sentence.txt", "w")
print("Enter 10 sentences")
for i in range(10):
    #input the sentence
    sentence = input()

    #append new line character to the sentence
    sentence += "\n"

    #write the sentence to the file
    f.write(sentence)

print("data successfully written to file")

#close the file
f.close()