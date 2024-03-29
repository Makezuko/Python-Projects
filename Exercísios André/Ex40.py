import random
# Preguiça de fazer o resto.
for c in range(3):
    random_year = random.randrange(0, 2100) 
    if random_year < 1583:
        bissexto = False
    else: 
        if random_year % 4 == 0 and random_year % 100 != 0 or random_year % 400 == 0:
            bissexto = True
        else:
            bissexto = False

    random_month = random.randint(1,12)

    days31 = [1, 3, 5, 7, 8, 10, 12]
    days30 = [4, 6, 9, 11]

    if random_month in days31:
        max_days = 31
    elif random_month in days30:
        max_days = 30
    else:    
        if bissexto:
            max_days = 29
        else:
            max_days = 28

    random_day = random.randint(1, max_days)
    print('{:02}/{:02}/{:04}'.format(random_day, random_month, random_year))