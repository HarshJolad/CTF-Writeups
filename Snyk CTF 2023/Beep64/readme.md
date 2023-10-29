# Beep64

## Challenge Description
> Every CTF needs a base64 challenge... right?

## Attachments
* [chall.zip](./chall.zip)

## Solution
* Unzip the file, we get a wav file which is 37 mins long
* Listening to the audio file, it is DTMF tones
* Online decoders dont work for such a long audio file
* Using [this repo](https://github.com/ribt/dtmf-decoder) we can decode the audio file
* DTMF Output: [out.txt](./out.txt)
* Removing the `*` and replacing with `spaces`
* Decoding the rest using [T9 Decoder](https://www.cachesleuth.com/vanity.html)
* Replace
    * `SPACE`: nothing
    * `ZERO`: 0
    * `ONE`: 1
* Decode using Binary and then Base64 decoding gives us the flag

[**Cyberchef Recipe**](https://tinyurl.com/mr22fpe2)

### FLAG
```
flag{0421a964add97ff041431e2418e64508}
```

### Resources

* DTMF Decoder: https://github.com/ribt/dtmf-decoder
* T9 Decoder: https://www.cachesleuth.com/vanity.html
* Cyberchef: https://gchq.github.io/CyberChef/ 
