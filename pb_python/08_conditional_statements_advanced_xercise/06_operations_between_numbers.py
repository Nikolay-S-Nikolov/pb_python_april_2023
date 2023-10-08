n1 = int(input())
n2 = int(input())
math_operator = input()  # "+", "-", "*", "/", "%".
result = 0
even_odd = ""
if math_operator == "+":
    result = n1 + n2
    if result % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    print(f"{n1} {math_operator} {n2} = {result} - {even_odd}")
elif math_operator == "-":
    result = n1 - n2
    if result % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    print(f"{n1} {math_operator} {n2} = {result} - {even_odd}")
elif math_operator == "*":
    result = n1 * n2
    if result % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    print(f"{n1} {math_operator} {n2} = {result} - {even_odd}")
elif math_operator == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 / n2
        print(f"{n1} {math_operator} {n2} = {result:.02f}")
elif math_operator == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 % n2
        print(f"{n1} {math_operator} {n2} = {result}")
