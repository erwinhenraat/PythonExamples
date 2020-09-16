def goCamp():
    print("ejoying the great outdoors!")
def goRideBike():
    print("also enjoying the great outdoors but at an increased pace")


corona = False
greatWeather = True
money = 0
familyWants = False
iWant = True


#example of nested if statements
if !corona:
    if greatWeather:
        if money > 3000:
            if familyWants:
                if iWant:
                    goCamp()
        else:
            goRideBike()

#nested if statements with logical operators
if !corona and greatWeather:
    if money > 3000:
        if familyWants and iWant:
            goCamp()
    else:
        goRideBike()
