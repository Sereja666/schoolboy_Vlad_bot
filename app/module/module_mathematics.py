import random


async def matematics():
    n1 = random.randint(0, 100)
    n2 = random.randint(0, 100-n1)
    if n1 <= n2:
        result = n1 + n2
        query = f'{n1} + {n2}'
        print(query)
        print(result)
    else:

        # Выбираем случайное действие
        action = random.choice(['+', '-'])

        # Выполняем выбранное действие над числами a и b
        query = f'{n1} {action} {n2}'
        print(query)
        result = eval(query)

        print(result)
    return query, result
