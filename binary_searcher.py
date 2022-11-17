import random




while True:

    tem = [random.randint(0, 99) for x in range(100)]


    if tem == []:

        continue


    break




lis = []


for i in tem:

    if i not in lis:

        lis.append(i)


lis.sort()




print(lis)









l, r = 0, len(lis) - 1




while True:

    o = input("Please enter an integer value.: ")


    try:

        o = int(o)

    except ValueError:

        continue    


    break








while l <= r:


    m = (r + l) // 2




    if o > lis[m]:

        l = m + 1

        continue


    elif o < lis[m]:

        r  = m - 1

        continue


    else:

        break









print(m if o == lis[m] else "suka")


