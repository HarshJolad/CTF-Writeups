# Finders Keepers

## Challenge Description
> Patch found a flag! He stored it in his home directory... should be able to keep it?

## Solution
* From the description, we know that the flag is in the home directory of the user `patch`.
* But we cannot access the home directory of `patch` because we don't have the permission to do so.
![patch](image.png)
* `sudo` wasnt even there 💀
![sudo](image-1.png)
* Looking for the flag using `find`
![Alt text](image-2.png)
* Looking for interesting binaries with `suid` bit set but nothing
![suid](image-3.png)
* Looking for interesting files with `sgid` bit set, we find the `find`
![sgid](image-4.png)
* Using `find` we can get the flag
![flag](image-5.png)

### Flag
```
flag{e4bd38e78379a5a0b29f047b91598add}
```
