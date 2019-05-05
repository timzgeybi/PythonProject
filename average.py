no_list = [22, 68, 90, 78, 90, 88]


def average(x):
    ave = 0
    for i in no_list:
        ave += i
    return ave / len(no_list)


print(average(no_list))
