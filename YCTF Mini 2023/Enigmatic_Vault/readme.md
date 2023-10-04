# Enigmatic Vault

## Challenge Description
> In the heart of the mysterious forest, a hidden vault guards ancient relics.

## Attached files
* [challange.doc](./challange.doc)

## Solution
* Opening the doc file, we find weird brackets.
* Using [dcode.fr](https://www.dcode.fr/cipher-identifier), we can figure out that `JSFuck` Language has been used
* After `JSfuck` decoding the doc file contents, we find another string which uses `Kenny Language`
* `Kenny language` decoding gives an encoded string
* Using [cyberchef](https://gchq.github.io/CyberChef/#recipe=From_Base58('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz',false)From_Base85('!-u',true,'z')&input=Q1l5bnhxZHN0akd0V1BYWkJIeU1tR2EzSGk3VGZBMTFWV2tKM2FqWGE2YW5yYkVGVjNhekhGaEFOc1pXNG5kSFpMdQ), `Base58, Base85` decoding gives us the flag

## FLAG
```
xCTF{HiddenVaultEntranceBehindTheFalls}
```



