# Oink Oink v0

## Description
> This is how pigs used to communicate ...

> Flag format : pesu_ec{<string>}  
Example: string recieved is helloworld  
Flag should be: pesu_ec{helloworld}

[piggy_lang.png](./piggy_lang.png)
## Solution
* From the description, we can understand that we have to decrypt using `pigpen cipher`
* Using [dcode.fr](https://www.dcode.fr/pigpen-cipher) we can decrypt the cipher

### FLAG
```
pesu_ec{LITTLEPIGSSRAWHOUSE}
```