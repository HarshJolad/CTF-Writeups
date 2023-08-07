# OTP Portal Intrigue

## Description
> Your mission, should you choose to accept it, is to infiltrate a mysterious portal secured by OTP authentication.   
`159.65.146.255`

## Solution

* We are provided with an IP address: `159.65.146.255`
* Performing an `nmap` scan on it, we find the FTP port open.
* We can login to the FTP server using anonymous.
* Upon listing the files in the FTP server, we find a file named `my_database.sql`.
* We can download the file and view its contents.
`mget my_database.sql`
* On opening the file, we find the credentials`admin:admin` and a `TOTP`  
`YDTN2JY6CWKSK6PB3HNOAY4APASUVREM`

![sql file](image.png)
* On doing some research on TOTP, we find that it is a Time-based One-Time Password algorithm.
* We can add `YDTN2JY6CWKSK6PB3HNOAY4APASUVREM` to Google Authenticator and login with the credentials we found from the **SQL** file.
* We are asked for an OTP.
* Entering the OTP which is displayed in the Google Authenticator app, we get the flag.
* Flag:   
`KPMG_CTF{324b7e52953f62f1624fb64a2e8202e4}`
