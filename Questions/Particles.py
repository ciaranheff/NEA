import math
ElectronCharge = (1.6 * 10**-19)

def roundsf(Number, sf):
    if Number == 0:
        return 0
    power = int(math.floor(math.log10(abs(Number))))
    return round(Number, sf - power - 1) # round function = number , dp
# Math explained - log10 finds the power of the exponent to a dp | abs gives the absolue value of the power so it is not a decimal
# number minus 1 as it is the first value (dont need it)

def Question1 (eV): # electron volts to volts
    Answer = (eV * (ElectronCharge))
    RoundedAnswer = roundsf(Answer,3)
    print("What is the value of" , eV , "electron volts in Volts rounded to 3dp where e = x10^ ")
    UserAnswer = float(input("")) #answer given like 8e-19
    ###
    if UserAnswer == RoundedAnswer:
        print(True)
    else:
        print(False)

def Question2 (V): # Volts to electron volts
    Answer = (V / (ElectronCharge))
    RoundedAnswer = roundsf(Answer,3)
    print(RoundedAnswer)
    print("What is the value of" , V , "Volts in electron Volts rounded to 3dp where e = x10^ ")
    UserAnswer = float(input("")) #answer given like 8e19
    ###
    if UserAnswer == RoundedAnswer:
        print(True)
    else:
        print(False) #and from here


