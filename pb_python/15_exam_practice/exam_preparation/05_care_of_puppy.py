# •	Закупеното количество храна за кученцето в килограми – цяло число в интервала [1 …100]
# •	На всеки следващ ред до получаване на команда Adopted ще получавате колко грама изяжда кученцето на всяко хранене - цяло число в интервала [10 …1000]
available_food = int(input())
command = input()

available_food = available_food * 1000
while not command == "Adopted":
    command = int(command)
    available_food -= command
    command = input()
if available_food >= 0:
    print(f"Food is enough! Leftovers: {available_food} grams.")
else:
    print(f"Food is not enough. You need {- available_food} grams more.")
