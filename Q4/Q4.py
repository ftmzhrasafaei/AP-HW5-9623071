import random
#check for being in circle
def IsInCircle(x , y):
    if (x**2 + y**2 -0.25) < 0:
        return True
    else:
        return False
#making list o couple in range -0.5 , 0.5
def Generator(x):
    return[(random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5)) for i in range(x)]


def Find():
    mypi = 0
    counter = 1
    while abs(3.1415-mypi)>0.001:
        sum = 0
        myrandom = Generator(counter)
        for i in range(0,counter):
            if IsInCircle(myrandom[i][0],myrandom[i][1]):
                sum = sum + 1
        mypi = sum*4/counter
        counter += 1
    return [counter-1 ,mypi]


############### main ################
repeat = int(input("give me a number for calling Find() function : "))
resault = 0
counter = repeat
while counter > 0:
    resault += Find()[1]
    counter -= 1
piis = resault/repeat
print('PI is {:} with 5 digit of decimals {:.6} after {:} times calling Find() function '.format(piis , piis ,repeat))
