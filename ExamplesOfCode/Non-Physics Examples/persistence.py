# Creating a counter class
class Counts:
    def __init__(self, start):
        self.start = start
    def counter(self):
        self.start += 1
        return self.start
    def show(self):
        return self.start

# Creating two counter objects
counter1 = Counts(0)
counter2 = Counts(0)


def additive(n):
#   Converting the number into a string to be able to iterate over
    n = str(n)
#   Making sure the number is more than 1 digit
    if len(n) <= 1:
        return 'Additive: ' + ' The result is ' + n + ', 0 steps'
    elif len(n) > 1:
#   Creating a sum variable equal to 0 to add to
        Sum = 0
#   Begining iterating over the string and adding the values to the Sum variable
        for x in n:
            Sum += int(x)
#   Adding one step to the counter1
        counter1.counter()
        Sum = str(Sum)
#   Ending the function once only 1 digit is left
        if len(Sum) == 1:
            return 'Additive: ' + 'The result is ' + str(Sum) + ', ' + str(counter1.show())+ ' ' + 'Steps'
#   Continuing the function until 1 digit is left
        else:
            return additive(int(Sum))
print(additive(123456))

def multi(n):
#   Converting the number into a string to be able to iterate over  
    n = str(n)
#   Making sure the number is more than 1 digit
    if len(n) <= 1:
        return 'Multiplicative: ' + ' The result is ' + n + ', 0 steps'
    elif len(n) > 1:
#   Creating a mult variable equal to 1 to multiply with
        mult = 1
#   Begining iterating over the string and multiplying the values to the mult variable
        for x in n:
            mult *= int(x)
#   Adding one step to the counter2
        counter2.counter()
        mult = str(mult)
#   Ending the function once only 1 digit is left
        if len(mult) == 1:
            return 'Multiplicative: ' + 'The result is ' + str(mult) + ', ' + str(counter2.show())+ ' ' + 'Steps'
#   Continuing the function until 1 digit is left
        else:
            return multi(int(mult))
print(multi(123456))
