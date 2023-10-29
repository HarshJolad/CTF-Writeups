from pwn import *

conn = remote('challenge.ctf.games', 30107)

conn.recvuntil(b'(Y/n): ')
conn.sendline(b'Y')

for i in range(1,101):
    question = conn.recvuntil(b'?').decode('utf-8').split(' ')

    if "Correct!\nWhat" in question:
        num1 = float(question[3])
        operator = question[4]
        num2 = float(question[5][:-1])
        print("Question: {} {} {}".format(num1, operator, num2))
    else:
        num1 = float(question[4])
        operator = question[5]
        num2 = float(question[6][:-1])
        print("Received Question: {} {} {}".format(num1, operator, num2))
        
    operator_functions = {
        '+': lambda a, b: round(a + b, 1),
        '-': lambda a, b: round(a - b, 1),
        '*': lambda a, b: round(a * b, 1),
        '/': lambda a, b: int(a) // int(b) if a % 1 == 0 and b % 1 == 0 else round(a / b, 1)
    }
    answer = operator_functions[operator](num1, num2)
    conn.sendline(str(answer))
    print("Sent Answer: {}".format(answer))

q = conn.recvline()
print(q)
conn.interactive()
