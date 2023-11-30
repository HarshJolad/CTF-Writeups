# Oink Oink v1

## Description
> Among the oinking demands of the Latin pigs, the Roman influence dictated the farm's daily flow

> Flag format : pesu_ec{<words seperated by underscore>}  
>Example: string recieved is abc 274 xyz  
> Flag should be: pesu_ec{abc_274_xyz}

[chal.txt](./chal.txt)
## Solution
* [dcode.fr](https://www.dcode.fr/cipher-identifier) tells us that it is a ROT47 cipher
* Decrypting using `ROT47` and then using `piglatin cipher` we get the flag

### FLAG
```
pesu_ec{5T1CK5_house_1s_mine_668}
```