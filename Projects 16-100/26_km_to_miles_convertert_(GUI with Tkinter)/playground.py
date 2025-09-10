# let's try to create a function in which I can sum every number I insert into argument
# So n numbers
# I call it args but every name is good
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

# print(add(1,10,3,4,5))

# Let's create a function that containing multiply keywords
def calculate(n, **kwargs):
    print(kwargs)
    # for (key, value) in kwargs.items(): # I can have access to all keys and all values of dictionary
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2,add= 5, multiply= 3) # it gives me a dictionary: {'add': 5, 'multiply': 3}

class Car:

    def __init__(self, **kw):
        self.km = kw.get("km") #uso .get() leggere a riga 34 il motivo
        self.model = kw.get("model")
        self.make = kw.get("make")

# Inizializzo l'oggetto car con le keyword "model" e "make", ma senza "km".
car = Car(model= "Panda", make= "Fiat")

#Avendo usato la funzione .get(kw) mi restituisce "None" al posto di darmi un errore
print(f"Your car is a {car.make} {car.model}, and it makes {car.km} km")