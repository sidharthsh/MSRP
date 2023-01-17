
def checker(temp):
    for x in temp:
        if (x in forbidden):
            return False
    return True

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1] 

def get_power_set(s):
  power_set=[[]]
  for elem in s:
    for sub_set in power_set:
      power_set=power_set+[list(sub_set)+[elem]]
  return power_set

def qsetcalc(base, forbidden, limit):
    setofspecialnumbers = []
    specialcorrespondsto = {}
    currentnumber = 1

    while (currentnumber <= limit):

        temp = numberToBase(currentnumber, base)
    
        if (checker(temp) == True):
            setofspecialnumbers.append(temp)
            specialcorrespondsto[str(temp)] = currentnumber


        currentnumber = currentnumber + 1

    i = 2
    j = 0

    quotientset = set()


    while (i < len(setofspecialnumbers)):
        j = i - 1
        while (j >= 0):
            quotient = specialcorrespondsto[str(setofspecialnumbers[i])]/specialcorrespondsto[str(setofspecialnumbers[j])]
            modulus = specialcorrespondsto[str(setofspecialnumbers[i])]%specialcorrespondsto[str(setofspecialnumbers[j])]
            if (modulus == 0):
                quotientset.add(int(quotient))
            j = j - 1
        i = i + 1

    quotientset = list(quotientset)
    quotientset.sort()
    filename = "b" + str(base) + "_" + str(forbidden) + "_till_" + str(limit) + ".txt"
    f = open(filename, "w+")
    for x in quotientset:
        f.write(str(x) + "\n")
    f.close()
    print(filename)

base = 6
possibleforbidden = [1, 2, 3, 4, 5]
possiblelimits = [1000, 10000, 100000]

while (base < 7):  
    allforbidden = get_power_set(possibleforbidden)
    for forbidden in allforbidden:
        if forbidden == []:
            continue
        for limit in possiblelimits:
            qsetcalc(base, forbidden, limit)
    
    base = base + 1
    possibleforbidden.append(base - 1)

   