# Two Paths

## DESCRIPTION
> Logan gave me this image file before disappearing..
I've been breaking my head over it for long
Can you decode it?  
Author: Rakhul  
**FLAG FORMAT**:
dsc{[a-zA-Z0-9_]+}

## Solution
* Running strings on the jpg provided, we see there are few files embedded in it.
* Use Binwalk to extract(`binwalk -e <file-name>`), we get 2 more images which contain more embedded files 
    * greenpill.jpg
    * redpill.jpg
* Extracting greenpill gives us nothing but a troll image
* Extracting redpill.jpg gives us a wav file and a encrypted zip file
* Morse decode wav using [this tool](https://morsecode.world/international/decoder/audio-decoder-adaptive.html) gives us  
`T H E P A S S W O R D I S T H E H O V E R C R A F T O F M O R P H E U S` 
* Googling `THE HOVER CRAFT OF MORPHEUS` gives us `nebuchadnezzar`
* Using `nebuchadnezzar` as password for the zip file, we get a wav file named `deep_secret.wav`
* The name of the file is a hint: **deep**
* We can use [deepsound](https://jpinsoft.net/deepsound/overview.aspx) to extract flag file
* It gives us a text file which contains the flag
* Flag:   
`dsc{u_ch053_THE_cOrr3Ct_pill!}`
