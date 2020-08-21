print("Welcome to our Solar System!")
name = input('What is your name? ')
print("Hi," + name + "!")
print("Whenever we see a star \"*\" press enter when you're ready to move on, lets try now, press enter!")
star = input('*')
print("Our Solar System is a very large and complex place. It is composed of eight planets, one star"
      " and many many other objects. ")
print("These objects include asteroids, comets, dwarf planets, and lots of dust.")
print("Lets start out with using your weight to calculate how much you would weigh on the different planets.")
weight = int(input('How much do you weigh on Earth? '))
print("We can use your weight and Newton's second law ( F = ma , Force is equal to Mass times Acceleration)"
      " to calculate your weight on the different planets in our solar system.")
print("In this case our weight " + str(weight) + " lbs is the force, mass is what we want to calculate,"
      "and acceleration is 9.8 m/s\u00b2.")
input('*')
print("F = ma")
print("F = " + str(weight) + " lbs , which we can convert to kilograms by dividing by"
      " 2.2 which gives " + str(round(weight / 2.2)) + " kg")
print("m = ? , this is what we are looking for.")
print("a = 9.8 m/s\u00b2")
input('*')
print("m = " + str(weight) + " kg / 9.8 m/s\u00b2 = " + str(round(weight / 9.8)) + " kg")
qes2 = "yes"
degree_sign = u"\N{DEGREE SIGN}"
planet = input('Which planet would you like to learn about? ')

while qes2 == "yes":
    if planet == "Mercury":
        print("Mercury is the smallest and closest planet to the Sun. Being this close to the Sun"
              " means that during the day it can get extremely hot, like 900" + degree_sign + "F hot!")
        qes = input("Would you like a fun fact? ")
        if qes == "yes":
            x = (float((weight / 9.8) * 3.7))
            print("On Mercury you would weigh " + str(round(x)) + " lbs!")
            print("This is due to the fact that this smaller planet has a smaller force of gravity!")
            qes_1 = input("Would you like another fun fact? ")
            if qes_1 == "yes":
                print("One year on Mercury (the amount of time it takes Mercury to complete one "
                      "full orbit of the Sun) is equal to 88 days on Earth.")
                print("One day on Mercury lasts two Mercury years long, or you get one year of daylight and"
                      " one year of night.")
                qes2 = input('Would you like to see a different planet? ')
                if qes2 == "yes":
                    planet = input('Which planet would you like to learn about? ')
                else:
                    print("Thanks for your time! Have a nice day!")
            else:
                qes2 = input('Would you like to see a different planet? ')
                if qes2 == "yes":
                    planet = input('Which planet would you like to learn about? ')
                else:
                    print("Thanks for your time! Have a nice day!")
        else:
            qes2 = input('Would you like to see a different planet? ')
            y = "yes"
            if y == qes2:
                planet = input('Which planet would you like to learn about? ')
            else:
                print("Thanks for your time! Have a nice day!")
    elif planet == "Venus":
        print("Venus is considered Earth's twin sister. This is because Venus and Earth are similar in size"
              " but this is where the similarities end.")
        qes = input("Would you like a fun fact? ")
        if qes == "yes":
            x = (float((weight / 9.8) * 8.87))
            print("On Venus you would weigh " + str(round(x)) + " lbs!")
            print("This should be pretty close to how much you weigh on Earth, this is due to the fact"
                  " that Venus and Earth are almost the same size and density! ")
            qes_1 = input("Would you like another fun fact? ")
            if qes_1 == "yes":
                print("Venus and Uranus both have a very unique feature that helps them stand out."
                      " Both of these planets spin in the opposite direction of the other planets in our "
                      "solar system. On Venus the Sun rises in the west and sets in the east. This makes"
                      "for some pretty interesting days.")
                qes2 = input('Would you like to see a different planet? ')
                if qes2 == "yes":
                    planet = input('Which planet would you like to learn about? ')
                else:
                    print("Thanks for your time! Have a nice day!")
            else:
                qes2 = input('Would you like to see a different planet? ')
                if qes2 == "yes":
                    planet = input('Which planet would you like to learn about? ')
                else:
                    print("Thanks for your time! Have a nice day!")
        else:
            qes2 = input('Would you like to see a different planet? ')
            y = "yes"
            if y == qes2:
                planet = input('Which planet would you like to learn about? ')
            else:
                print("Thanks for your time! Have a nice day!")
    elif planet == "Earth":
        print("Welcome to Earth, this is where you were born and currently live!")
        qes = input("Would you like a fun fact? ")
        if qes == "yes":
            x = (float((weight / 9.8) * 9.8))
            print("On Earth you weigh " + str(round(x)) + " lbs!")
            print("This is because earth has a specific acceleration due to gravity and that's"
                  " what we use to calculate weigh!")
            qes_1 = input("Would you like another fun fact? ")
            if qes_1 == "yes":
                print("Earth is the only planet that we know of that has living things.")
                qes2 = input('Would you like to see a different planet? ')
                if qes2 == "yes":
                    planet = input('Which planet would you like to learn about? ')
                else:
                    print("Thanks for your time! Have a nice day!")
            else:
                qes2 = input('Would you like to see a different planet? ')
                if qes2 == "yes":
                    planet = input('Which planet would you like to learn about? ')
                else:
                    print("Thanks for your time! Have a nice day!")
        else:
            qes2 = input('Would you like to see a different planet? ')
            if qes2 == "yes":
                planet = input('Which planet would you like to learn about? ')
            else:
                print("Thanks for your time! Have a nice day!")
    elif planet == "Mars":
        print("Mars is known as the red planet, this red color comes from its thin "
              "atmosphere and distance from the Sun.")
        qes = input("Would you like a fun fact? ")
        if qes == "yes":
            x = (float((weight / 9.8) * 3.7))
            print("On Mars you would weigh " + str(round(x)) + " lbs!")
            print("This is due to size, Mars is only just over half the size of Earth"
                  " but again has a similar density!")
            qes = input("Would you like another fun fact? ")
            if qes == "yes":
                print("Mars has two moons Phobos and Deimos, named after the Greek mythological twins")
                print("who followed their father Ares into battle.")
                qes2 = input('Would you like to see a different planet? ')
                if qes2 == "yes":
                    planet = input('Which planet would you like to learn about? ')
                else:
                    print("Thanks for your time! Have a nice day!")
            else:
                qes2 = input('Would you like to see a different planet? ')
                if qes2 == "yes":
                    planet = input('Which planet would you like to learn about? ')
                else:
                    print("Thanks for your time! Have a nice day!")
        else:
            qes2 = input('Would you like to see a different planet? ')
            if qes2 == "yes":
                planet = input('Which planet would you like to learn about? ')
            else:
                print("Thanks for your time! Have a nice day!")
    elif planet == "Jupiter":
        print("Jupiter is the largest planet in our solar system, I hope you enjoy your visit!")
        qes = input("Would you like a fun fact? ")
        if qes == "yes":
            x = (float((weight / 9.8) * 24.79))
            print("On Jupiter you would weigh " + str(round(x)) + " lbs!")
            print("This is due to the immense gravitational pull of this large planet!")
            qes_1 = input("Would you like another fun fact? ")
            if qes_1 == "yes":
                print("Jupiter has four large moons Io, Europa, Ganymede, and Callisto referred "
                      "to as the Galilean Moons. These are the initial four moons Galileo discovered"
                      " orbiting around Jupiter")
                qes2 = input('Would you like to see a different planet? ')
                if qes2 == "yes":
                    planet = input('Which planet would you like to learn about? ')
                else:
                    print("Thanks for your time! Have a nice day!")
            else:
                qes2 = input('Would you like to see a different planet? ')
                if qes2 == "yes":
                    planet = input('Which planet would you like to learn about? ')
                else:
                    print("Thanks for your time! Have a nice day!")
        else:
            qes2 = input('Would you like to see a different planet? ')
            if qes2 == "yes":
                planet = input('Which planet would you like to learn about? ')
            else:
                print("Thanks for your time! Have a nice day!")
    elif planet == "Saturn":
        print("Saturn has many rings and moons.")
        qes = input("Would you like a fun fact? ")
        if qes == "yes":
            x = (float((weight / 9.8) * 10.44))
            print("On Saturn you would weigh " + str(round(x)) + " lbs!")
            print("This is pretty close to how much you weigh on Earth, although Saturn is "
                  "much larger it is much less dense!")
            qes_1 = input("Would you like another fun fact? ")
            if qes_1 == "yes":
                print("Saturn's rings are made up of ice, rock, and dust. These ingredients may"
                      " come from comets, asteroids, and potentially broken moons.")
                qes2 = input('Would you like to see a different planet? ')
                if qes2 == "yes":
                    planet = input('Which planet would you like to learn about? ')
                else:
                    print("Thanks for your time! Have a nice day!")
            else:
                qes2 = input('Would you like to see a different planet? ')
                if qes2 == "yes":
                    planet = input('Which planet would you like to learn about? ')
                else:
                    print("Thanks for your time! Have a nice day!")
        else:
            qes2 = input('Would you like to see a different planet? ')
            if qes2 == "yes":
                planet = input('Which planet would you like to learn about? ')
            else:
                print("Thanks for your time! Have a nice day!")
    elif planet == "Uranus":
        print("Uranus lays on its side and is known as the icy giant.")
        qes = input("Would you like a fun fact? ")
        if qes == "yes":
            x = (float((weight / 9.8) * 8.87))
            print("On Uranus you would weigh " + str(round(x)) + " lbs!")
            print("Although Uranus is much larger than Earth it is much less dense than Earth!")
            qes_1 = input("Would you like another fun fact? ")
            if qes_1 == "yes":
                print("Uranus sits on its side with the north and south poles facing towards and"
                      " away from the Sun. Because of this Uranus has 21 years of night in winter "
                      "and 21 years of daylight in the summer.")
                qes2 = input('Would you like to see a different planet? ')
                if qes2 == "yes":
                    planet = input('Which planet would you like to learn about? ')
                else:
                    print("Thanks for your time! Have a nice day!")
            else:
                qes2 = input('Would you like to see a different planet? ')
                if qes2 == "yes":
                    planet = input('Which planet would you like to learn about? ')
                else:
                    print("Thanks for your time! Have a nice day!")
        else:
            qes2 = input('Would you like to see a different planet? ')
            if qes2 == "yes":
                planet = input('Which planet would you like to learn about? ')
            else:
                print("Thanks for your time! Have a nice day!")
    elif planet == "Neptune":
        print("Neptune is named after the Roman god of the sea and is very blue.This blue color "
              "is due to the methane in the atmosphere absorbing red light and reflecting blue light")
        qes = input("Would you like a fun fact? ")
        if qes == "yes":
            x = (float((weight / 9.8) * 11.15))
            print("On Neptune you would weigh " + str(round(x)) + " lbs!")
            print("On Neptune the force of gravity is slightly more than Earths causing you "
                  "to feel pretty heavy!")
            qes_1 = input("Would you like another fun fact? ")
            if qes_1 == "yes":
                print("Although Pluto was once considered to be the farthest planet (now dwarf planet)"
                      " from the Sun there is a 20 year period during Neptune's orbit in "
                      "which Neptune is farther away from the sun than Pluto is.")
                qes2 = input('Would you like to see a different planet? ')
                if qes2 == "yes":
                    planet = input('Which planet would you like to learn about? ')
                else:
                    print("Thanks for your time! Have a nice day!")
            else:
                qes2 = input('Would you like to see a different planet? ')
                if qes2 == "yes":
                    planet = input('Which planet would you like to learn about? ')
                else:
                    print("Thanks for your time! Have a nice day!")
        else:
            qes2 = input('Would you like to see a different planet? ')
            if qes2 == "yes":
                planet = input('Which planet would you like to learn about? ')
            else:
                print("Thanks for your time! Have a nice day!")
    elif planet == "Pluto":
        print("Although no longer a planet Pluto, the now dwarf planet, is still remembered "
              "and cherished by many.")
        qes = input("Would you like a fun fact? ")
        if qes == "yes":
            x = (float((weight / 9.8) * 0.62))
            print("On Pluto you would weigh " + str(round(x)) + " lbs!")
            print("This is because Pluto is so small!")
            qes_1 = input("Would you like another fun fact? ")
            if qes_1 == "yes":
                print("Pluto has five small moons that orbit around it, the largest of these moons is "
                      "named Charon.")
                qes2 = input('Would you like to see a different planet? ')
                if qes2 == "yes":
                    planet = input('Which planet would you like to learn about? ')
                else:
                    print("Thanks for your time! Have a nice day!")
            else:
                qes2 = input('Would you like to see a different planet? ')
                if qes2 == "yes":
                    planet = input('Which planet would you like to learn about? ')
                else:
                    print("Thanks for your time! Have a nice day!")
        else:
            qes2 = input('Would you like to see a different planet? ')
            if qes2 == "yes":
                planet = input('Which planet would you like to learn about? ')
            else:
                print("Thanks for your time! Have a nice day!")
    else:
        print("Invalid Entry. Try Again!")
        planet = input('Which planet would you like to learn about? ')

print("done!")
