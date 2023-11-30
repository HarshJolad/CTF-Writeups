# I walk alone

## Description
> I walk a lonely road The only one that I have ever known...

[chal.png](./chal.png)

## Solution
* Running `binwalk` on the image, we see there are files embedded in it.
* Extracting the files using `binwalk -e chal.png` gives us a png file with flag at the bottom of the image.

### Flag
```
pesu_ec{b1n_fl4g}
```
