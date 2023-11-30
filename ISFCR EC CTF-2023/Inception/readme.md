# Inception

## Description
> You have a file, but what are you going to do with it? Where will you look?

> HINT: There is more to the file than what is written in it. A hidden message under all the snow, perhaps?

[password.txt](./password.txt)

## Solution
* We see that the file contains whitespaces. 
* Morse Decode the first line `- --- - . --`: `TOTEM`
* Decrypt the file using:
```
stegsnow -C -p "TOTEM" password.txt
```

### FLAG: 
```
pesu_ec{r34l1ty_15_n0t_3n0ugh}
```