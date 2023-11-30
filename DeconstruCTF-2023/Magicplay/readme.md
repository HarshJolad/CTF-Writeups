#  Magicplay

## DESCRIPTION
> Dwayne's mischevious nephew played around in his pc and corrupted a very important file.. Help dwayne recover it!  
> Author: Rakhul

## Solution
* We get a corrupted image.
* On opening in a hex editor(I used `bless hex editor`), we see that the PNG header chunks are wrong
* On fixing them one by one, we get the flag
* [nayuki.io](https://www.nayuki.io/page/png-file-chunk-inspector) is a good online resource which will help you in fixing corrupted header chunks

![flag](magic_play.png)
* FLAG:   
`dsc{COrrupt3d_M4g1C_f1Ag}`
