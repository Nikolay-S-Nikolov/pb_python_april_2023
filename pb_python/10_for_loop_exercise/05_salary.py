FACEBOOK_PENALTY = 150
INSTAGRAM_PENALTY = 100
REDDIT_PENALTY = 50

count = int(input())
salary = int(input())
opened_site = ""
for _ in range(count):
    opened_site = input()
    if opened_site == "Facebook":
        salary -= FACEBOOK_PENALTY
    elif opened_site == "Instagram":
        salary -= INSTAGRAM_PENALTY
    elif opened_site == "Reddit":
        salary -= REDDIT_PENALTY
    if salary <= 0:
        break
if salary <= 0:
    print("You have lost your salary.")
else:
    print(salary)
