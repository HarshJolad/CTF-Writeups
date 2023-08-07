# Breakout - Unleash the Flag

## Description :

> You find yourself locked within an environment where you are equipped with only what you bring. Your mission is to find creative ways to break free from the restrictions and ultimately obtain the coveted flag.

## Solution

* Looking at the source code, there are 2 comments which say `User-Agent` needs to be `Anish Mitra` and `cookie` needs to be **What KPMG stands for** .
* This can be done by intercepting the request using burpsuite and changing the `User-Agent` and setting the `cookie` values.
* `User-Agent: Anish Mitra`
* `cookie: Klynveld Peat Marwick Goerdeler`
* We have to give a command in the text-box provided
* Typing `ls` shows us the directory listing and there is a `flag.txt` file in there.
* changing the command to `cat flag.txt` in the request gives us the flag.
