# Fast Fernet

## Description
> At a blink, I lost my flag

[chal.py](./chal.py)  
[output.txt](./output.txt)

## Solution
* In the python file, at the end of line 4, theres a comment which says `secret_keyword=zoom`
* Using `zoom` as the `key_str`, we get an error saying `Fernet key must be 32 url-safe base64-encoded bytes`
* So the key must be `zoomzoomzoomzoomzoomzoomzoomzoom`
* Using [script.py](./script.py), we get the flag.
```bash
$ python3 script.py
FLAG:  b'pesu_ec{Z29vZF9qb2JfY29tcmFkZQ==}'
```

### FLAG
```
pesu_ec{Z29vZF9qb2JfY29tcmFkZQ==}
```