# Unchained 1

## Challenge Description
> "Go from hacking web to solving puzzles"

> The admin seems to have forgotten the password, so he just want you to recover by bypassing the login page.

> Good Luck!

> Challenge link: https://harsh1tarora.pythonanywhere.com/

## Solution
* We are supposed to bypass the login page. So, we try SQL injection.
* We try `admin' or 1=1--` as the username and `1` as the password.
* We are presented with a shell after bypassing the login page.
![shell](image.png)
* Using `help` we can see the list of commands available.
* We can use `flag` to get the flag.
![flag](image-1.png)


## FLAG
```
xCTF{y0u_f0und_m3_n0_way!}
```
