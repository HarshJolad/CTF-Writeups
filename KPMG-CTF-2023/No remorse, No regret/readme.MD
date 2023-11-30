# No remorse, No regret

## Description
> Agent X intercepts a high-stakes call between gangsters "Shadow" and "Viper." Critical intel lies within, but excessive background noise corrupts the message. Your mission should you choose to accept it is to decode the audio using the tools at your disposal.

## Solution
* We are provided with a mp3 file.
* Using [Audacity](https://www.audacityteam.org/) we can see that it has 2 channels.
* We can suppress one of the channels  
    * This can be done by moving the slider(on the left hand side) in the Audacity window to the left or right.

![audacity](image.png)
* Save the mp3 file and upload it to [Morse Decoder](https://morsecode.world/international/decoder/audio-decoder-adaptive.html).
* We get an url `RB.GY/3TPVV`
* Visting the url a zip file gets downloaded.
* The zip file contains an image. On extracting the zip file and running `strings` on the image we get the flag.  
`strings flag.jpg`
* FLAG:  
`KPMG_CTF{3ND_I$_H3R3}`
