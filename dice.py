import datetime
import matplotlib.pyplot as plt
import random


dice = [1,2,3,4,5,6]
puntuation = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
percentage = {1:[],2:[],3:[],4:[],5:[],6:[]}
throw = 0
throw_serie = []
nineteen_perc = False
nineteen_perc_throw = int()
zero_percent = False
zero_percent_throw = int()
almost_zero_percent = False
almost_zero_percent_throw = int()

def throw_the_dices():
    global throw
    for i in range(0,6):
        score = random.choice(dice)
        puntuation[score] += 1
        throw += 1
    throw_serie.append(throw)
    percetage_calc()

def percetage_calc():
    for n in range(1,7):
        percentagee = puntuation.get(n)/(throw)*100
        percentage[n].append(percentagee)
    one_percent_diference()

def one_percent_diference():
    global nineteen_perc_throw
    global nineteen_perc
    global zero_percent_throw
    global zero_percent
    global almost_zero_percent_throw
    global almost_zero_percent

    list_of_perc = []
    for n in range(1,7):
        list_of_perc.append(percentage[n][len(throw_serie) - 1])
    rest = sorted(list_of_perc)[5] - sorted(list_of_perc)[0]
    print(rest," Diferences between percentages")
    if rest <= 1 and not nineteen_perc:
        nineteen_perc = True
        nineteen_perc_throw = throw
    if rest <= 0.1 and not almost_zero_percent:
        almost_zero_percent = True
        almost_zero_percent_throw = throw
    if rest <= 0.01:
        print("REACH")
        zero_percent = True
        zero_percent_throw = throw


def draw_graphic():
    plt.xlabel('throw series')
    plt.ylabel('percentage')
    plt.plot(throw_serie,percentage[1])
    plt.plot(throw_serie,percentage[2])
    plt.plot(throw_serie,percentage[3])
    plt.plot(throw_serie,percentage[4])
    plt.plot(throw_serie,percentage[5])
    plt.plot(throw_serie,percentage[6])
    print(nineteen_perc_throw)
    if nineteen_perc:
        plt.axvline(x = nineteen_perc_throw, linestyle='dashed', color="y", label = "diferences lest than 1%")
    if almost_zero_percent:
        plt.axvline(x = almost_zero_percent_throw, linestyle='dashed', color="o", label = "diferences lest than 0.1%")
    if zero_percent:
        plt.axvline(x = zero_percent_throw, linestyle='dashed', color="r", label = "diferences lest than 0.01%")
    plt.show()

def calculate_time():
    finish_time = datetime.datetime.now() - start_time
    print("Time to complete %s" % finish_time)

i = 0
start_time = datetime.datetime.now()

while not zero_percent:
    i += 1
    print(i)
    throw_the_dices()

calculate_time()
draw_graphic()
