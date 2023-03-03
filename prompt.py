# Make a prompt asking a question

answer = input("Answer this question? y/n ")

# If the answer was y, gives the "answer" variable the value 1, otherwise give it 0
if answer == "y": answer = 1
else: answer = 0
print(answer)
