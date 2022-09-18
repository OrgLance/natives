# MGM_SetGangNestSaveGameString
```c
// 0x00642480
void MGM_SetGangNestSaveGameString(string saveGameString)
```
## Description

If you want to know more about it look **[here](MGM_GetGangNestSaveGameString.md)**.

But if you want to destroy all Gang Nests at once:
```php
$saveGameString = "ffffffffffffffffffffffffffffffffffffffffffffffff";
MGM_GetGangNestSaveGameString($saveGameString);
```