# Fire Accident

## Challenge Description
> In a remote village hidden within an ancient forest, a devastating fire reduced a 58 historic cottage to ruins, leaving behind a partially burned image and a cryptic message. Some of the villgeres do belive that this fire accident was because some villegers cheated while playing their anual game festival.Legends spoke of a long-guarded treasure within the cottage, now lost in the ashes.

## Attached files
* [time_taker.txt](./time_taker.txt)
* [yitsburnt.png](./yitsburnt.png)

## Solution
* Base58 decoding the txt file gives us: `cVGR{C3brt_Ou3zy_zp@g_Bmbv!}`, which is similar to the flag format.
* The png file shows us a matrix of 5x5, which is a hint for playfair cipher.
* Decrypt using [playfair cipher](https://www.dcode.fr/playfair-cipher) and the given matrix: `XCTFNVERCHATPLYFAICL`
* Adding the brackets, numbers and the underscores, we get the flag.

## FLAG
```
xCTF{N3ver_Ch3at_pl@y_Fair!}
```
