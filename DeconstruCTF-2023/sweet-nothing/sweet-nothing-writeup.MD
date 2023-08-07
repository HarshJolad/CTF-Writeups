# sweet-nothing


## Description
> What can be sweeter than doing nothing? The flag is right in front of you.  
**FLAG FORMAT:**
dsc{[a-zA-Z0-9_]+}

## Solution
* We get 3 images of: Colosseum, pizza and a Ferrari logo which are related to Italy
* So we change `Accept-Language` header to `it-IT` after intercepting it.
We get a response which says: 
```
Almost there! Your **secret** query is "spaghetti".
```
* add `/?secret=spaghetti` to the `GET` request and `it-IT` to language gives us the flag  
`https://{URL}/?secret=spaghetti`
* Flag:  
`dsc{1a_d01c3_vit4}`
