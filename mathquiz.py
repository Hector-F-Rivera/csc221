from random import randint
right = 0
numd = 10
for x in 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15:
    print("Question " + str(x) + ".")
    numr1 = randint(1,numd)
    numr2 = randint(1,10)
    q = "What is " + str(numr1) + " times " + str(numr2) + "?"
    a = int(input(q))
    numsum = numr1 * numr2
    print("The answer is " + str(numsum) +".")
    if numsum == a:
        print("correct")
        right = right + 1
        numd = numd + 5
    else:
        print("wrong, try again")
        numd - 2
    print(" ")
print("I asked you 15 questions.  You got " + str(right) + " of them right.")
if 15 == right:
    print("Perfect,Great Job!")
else:
    if right > 9:
        print("Well done!")
    else:
        print("do better.")
