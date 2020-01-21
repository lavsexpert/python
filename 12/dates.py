def getdays(data1, data2):
    dayinmonth = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    split1 = data1.split(".")
    split2 = data2.split(".")
    (day1, mon1, year1) = (int(split1[0]), int(split1[1]), int(split1[2]))
    (day2, mon2, year2) = (int(split2[0]), int(split2[1]), int(split2[2]))

    countmon1 = 0
    for i in range(mon1-1):
        countmon1 = countmon1 + dayinmonth[i]
    countmon2 = 0
    for i in range(mon2-1):
        countmon2 = countmon2 + dayinmonth[i] 

    count1 = year1 * 365 + countmon1 + day1
    count2 = year2 * 365 + countmon2 + day2

    if count2 > count1:
        return count2 - count1
    else:
        return count1 - count2
