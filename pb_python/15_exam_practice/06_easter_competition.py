# Първоначално от конзолата се прочита броя на козунаците – цяло число в интервала [1… 100]
# След това за всеки козунак се прочита:
# •	Името на пекаря, който е направил козунака – текст
# •	До получаване на командата "Stop" се прочита
# o	оценка за козунак от един човек  – цяло число в интервала [1... 10]
bread_count = int(input())
points_new_number_1 = 0
baker_won = ""
for _ in range(bread_count):
    baker_name = input()
    command = input()
    points = 0
    while not command == "Stop":
        points += int(command)
        command = input()
    print(f"{baker_name} has {points} points.")
    if points > points_new_number_1:
        points_new_number_1 = points
        print(f"{baker_name} is the new number 1!")
        baker_won = baker_name
print(f"{baker_won} won competition with {points_new_number_1} points!")



