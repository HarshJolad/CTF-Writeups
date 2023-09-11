# Lenore Blum

## Description
> Lenore Carol Blum (née Epstein born December 18, 1942) is an American computer scientist and mathematician who has made contributions to the theories of real number computation, cryptography, and pseudorandom number generation. She was a distinguished career professor of computer science at Carnegie Mellon University until 2019 and is currently a professor in residence at the University of California, Berkeley. She is also known for her efforts to increase diversity in mathematics and computer science. - Wikipedia Entry

> Chal: Connect to `0.cloud.chals.io 28827` and return the flag to the computational mathematics professor from this random talk

### Attachments
[chal1.bin](./chal1.bin)

## Solution
* The binary implements **Blum Blum Shub algorithm**(BBS) which is a pseudorandom number generating technique.
* The program asks you to play a game. If you say yes, you are given a "**seed**" number and asked to guess the next random number. 
* When looking at the binary you can determine that the program generates three values, one of which is given to you and is called the "seed".
* By looking at the functions which generate these numbers, it can be seen that the p and q are generated according to the rules set for the algorithm (they must be congruent to 3 mod 4) however the seed is not.
* The `rand()` value the p and q are based off is used to get the seed value, which ends up just being the random value multiplied by 1337.
* We can solve this by writing a script which connects to the remote service, gets the seed value, and uses it to calculate the 2 random value which the remote server generates
* Using [script2.py](./script2.py) we can get the flag
* The functions in the script: `find_prime_congruent_to_3_mod_4`, `bbs`, `is_prime` are taken from the binary using `Ghidra`.


### FLAG
```
chctf{tH3_f1rsT_Blum}
```