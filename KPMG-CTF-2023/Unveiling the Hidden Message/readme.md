# Unveiling the Hidden Message

## Description
> The objective of this challenge is to reverse engineer a given binary executable file and extract flag embedded within the program. 

## Solution
* We are given a binary executable file.
* Running the command:
`strings payload`
And going through output we find the flag split into 2 parts: `KPMG_CTF` and `e59ff97941044f85df5297e1c302d260`
* Flag:  
`KPMG_CTF{e59ff97941044f85df5297e1c302d260}`
