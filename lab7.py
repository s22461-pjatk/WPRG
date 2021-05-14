names = (
    "Franek",
    "Marek",
    "Zbyszek",
    "Asia",
    "Basia",
    "Kasia",
    "Mateusz",
    "Andrzej"
    "Maria"
)

surnames = (
    "Banach",
    "Currie",
    "Kowalski",
    "Studencki",
    "Paszyn",
    "Małysz",
    "Ciupaga"
)

for x in names:
    if x[-1] == 'a':
        print(x)


print("\nzad polish_surnames")

def pol_surname(surname):
    polish_suffixes = ('ski', 'cki')
    for suff in polish_suffixes:
        if surname.endswith(suff):
            return True  
    return False

for surname in surnames:
    if pol_surname(surname):
        print(surname)



print("\nzad people")

people = []


for n in names:
    for s in surnames:
        if n[-1] == 'a' and pol_surname(surname):
            s = s[:-1] + 'a'
        people.append((n, s,))
        print(n, s)    
