# Oink Oink v2

## Description
> In a very Beautiful Fort, there were many pigs OINKing. This is what they said..

[chal.txt](./chal.txt)

## Solution
* From the description, we can understand that we have to decrypt using `Beaufort cipher`
* Before that we have to Convert the `binary text` to `base 10`. Then to ASCII. We get this  
`zevq_kg{z1xe_a_gkte_ud3_nr1la_h0o53_6783}`
> Binary => base 10 => ASCII => Beaufort cipher with `OINK` as the key
* Decrypting using `Beaufort cipher` with `OINK` as the key, we get the flag


### FLAG
```
pesu_ec{o1nk_i_have_th3_br1ck_h0u53_6783}
```