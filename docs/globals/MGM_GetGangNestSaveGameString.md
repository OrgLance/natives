# MGM_GetGangNestSaveGameString
```c
// 0x00642490
string MGM_GetGangNestSaveGameString()
```
## Description
The Return value consits of 6 * 4 bytes.<br>
One Part is one Zone.

### Example Script
```php
$outputBinary = MGM_GetGangNestSaveGameString();
DebugMsg("Save Game", $outputBinary);
```

### Example Output
```json
000080000000000000000000000000000000000000000000
```
