import random

def generate_task():
    operations = ['+', '-', '*', '/']
    op = random.choice(operations)

    a = random.randint(1, 20)
    b = random.randint(1, 20)

    if op == '/':
        a = a * b

    question = f"{a} {op} {b}"

    if op == '+':
        answer = a + b
    elif op == '-':
        answer = a - b
    elif op == '*':
        answer = a * b
    else:
        answer = a / b

    return question, answer