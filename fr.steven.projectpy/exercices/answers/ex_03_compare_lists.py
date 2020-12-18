
def getSameNumber():
    with open("primenumbers.txt", "r") as primeFile:
        for primeLine in primeFile:
            with open("happynumbers.txt", "r") as happyFile:
                for happyLine in happyFile:
                    if primeLine == happyLine:
                        print(primeLine.strip() + " : " + happyLine.strip())
getSameNumber()


def getSameNumberPrime():
    with open("primenumbers.txt", "r") as primeFile:
        for primeLine in primeFile:
            print(primeLine.strip())

def getSameNumberHappy():
    with open("happynumbers.txt", "r") as happyFile:
        for happyLine in happyFile:
            print(happyLine.strip())