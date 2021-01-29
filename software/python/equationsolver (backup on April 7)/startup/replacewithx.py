def replacer(equationlist):
    for i in range(0, len(equationlist)):
        if equationlist[i].isalpha():
            equationlist[i] = 'x'
    return equationlist