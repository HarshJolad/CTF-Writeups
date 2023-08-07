# MOVE

## DESCRIPTION
> There is an urgent need for a touch typist in our 13 year old organization, can you find the flag from the encrypted data?  
**FLAG FORMAT**:
DSC{[a-zA-Z0-9_]+}

* KEY.txt: 
```txt
U_E}M28NWV5?28S~
```

## Solution
* We are given a `key.txt` file
* We get 2 hints from the description: `13` and `typist`, which mean `ROT13` and `Keyboard Cipher`
* ROT13 decoding the contents in `key.txt` gives us `H_R}Z28AJI5?28F~`
* Keyboard Shift Cipher decrypt using [dcode.fr](https://www.dcode.fr/keyboard-shift-cipher) gives `DSC{V17_QU4L17Y`
* Add a `}` and submit the flag 
* FLAG:   
`DSC{V17_QU4L17Y}`
