user_name = input()
password = input()
data = input()
while password != data:
    data = input()
print(f"Welcome {user_name}!")
