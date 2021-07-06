def parse(val):
    for i in val:
        total = 0
        if (i == "I" and (val[i + 1] == "V" or val[i + 1] == "X")):
            total -= 1
        if (i == "I"):
            total += 1
        if (i == "V"):
            total += 5
        if (i == "X"):
            total += 10
    # if val == "I":
    #     return 1
    # elif val == "II":
    #     return 2
    # elif val == "III":
    #     return 3
    # elif val == "IV":
    #     return 4
    # elif val == "V":
    #     return 5
    # elif val == "VI":
    #     return 6
    # elif val == "VII":
    #     return 7
    # elif val == "VIII":
    #     return 8

