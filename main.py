#define function countA
def countA(w):

    a = 0

    for i in range (0,len(w)):
        if w[i] == "a":
            a = a + 1
    return a

print (countA("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))


