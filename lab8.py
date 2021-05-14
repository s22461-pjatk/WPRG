n = int(input("Podaj liczbę: "))



for x in range(1, n+1):
    fizz_buzz = []
    if x%3 == 0 and x%5 == 0:
        fizz_buzz.append("FizzBuzz")
    elif x%3 == 0:
        fizz_buzz.append("Fizz")
    elif x%5 == 0:
        fizz_buzz.append("Buzz")


    
    print(x, "".join(fizz_buzz))