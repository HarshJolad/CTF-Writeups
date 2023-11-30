# Hands Up

## Description
> Two friends wanted to try out something fun and understand some stuff, but little do they know that someone was eavesdropping. Let us teach them a lesson so that they never fall into this trap!

> Flag format : The flag format is pesu_ec{Answer seperated with underscore}

[capture.pcapng](./capture.pcapng)

## Solution
* Open the pcapng file in wireshark
* Following TCP Stream, in stream `34` we find a base64 encoded string
`OBSXG5K7MVRXW53JOIZXG2BUOJVV62JVL5RTAMCMPU======`
* Decoding the string, we get our flag.

### FLAG
```
pesu_ec{wir3sh4rk_i5_c00L}
```