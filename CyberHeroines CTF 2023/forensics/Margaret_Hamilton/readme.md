# Margaret Hamilton

## Description
> [Margaret Elaine Hamilton](https://en.wikipedia.org/wiki/Margaret_Hamilton_(software_engineer)) (née Heafield; born August 17, 1936) is an American computer scientist, systems engineer, and business owner. She was director of the Software Engineering Division of the MIT Instrumentation Laboratory, which developed on-board flight software for NASA's Apollo program. She later founded two software companies—Higher Order Software in 1976 and Hamilton Technologies in 1986, both in Cambridge, Massachusetts. - [Wikipedia Entry](https://en.wikipedia.org/wiki/Margaret_Hamilton_(software_engineer))

> Chal: Return the flag to NASAs first software engineer.

### Attachments
[Apollo-Mystery.jpg](./Apollo-Mystery.jpg)

## Solution
* Running `strings` on the image we see there is a `margaret_flag.png` after the IEND chunk.
* Using `binwalk` we can extract the file.
```
$ binwalk -e Apollo-Mystery.jpg
```
* We get a png file with the flag at the bottom of the image.
![flag](flag.png)

### FLAG
```
chctf{i_wr1t3_code_by_h4nd}
```