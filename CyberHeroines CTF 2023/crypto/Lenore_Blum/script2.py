from pwn import *

HOST = '0.cloud.chals.io'
PORT = 28827
# context.log_level = "debug"

p = remote(HOST, PORT)

p.recvuntil("Would you like to play? Y/N >>> ")
p.sendline("y")

def find_prime_congruent_to_3_mod_4(param):
    local_10 = param
    while True:
        cVar1 = is_prime(local_10)
        if cVar1 and (local_10 & 3) == 3:
            break
        local_10 += 1
    return local_10

def bbs(param1, param2, param3):
    local_10 = (param3 * param3) % (param1 * param2)
    local_18 = 0
    for local_1c in range(0x3f):
        local_10 = (local_10 * local_10) % (param1 * param2)
        local_18 |= (local_10 & 1) << (local_1c & 0x3f)
    return local_18

def is_prime(param):
    if param < 2:
        return 0
    elif param < 4:
        return 1
    elif (param & 1) == 0 or param % 3 == 0:
        return 0
    else:
        for local_10 in range(5, int(param ** 0.5) + 1, 6):
            if param % local_10 == 0 or param % (local_10 + 2) == 0:
                return 0
        return 1


while True:
    # Receive the seed value
    seed_line = p.recvline().strip().decode()
    seed = int(seed_line.split(": ")[1])

    known_factor = 0x539  

    # Calculate the two primes
    prime1 = find_prime_congruent_to_3_mod_4(seed // 1337)
    prime2 = find_prime_congruent_to_3_mod_4(prime1 + 1)

    # Calculate the random number using BBS PRNG
    random_number = bbs(prime1, prime2, seed)

    p.sendline(str(random_number))

    # outcome = p.recvline().strip().decode()
    outcome = p.recvline()

    if b"Incorrect" in outcome:
        print(outcome)
    elif b"Great job!" in outcome:
        print(outcome)
        print(random_number)
        p.interactive()
        break

p.close()