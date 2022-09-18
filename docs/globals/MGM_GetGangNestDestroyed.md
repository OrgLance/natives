# MGM_GetGangNestDestroyed
```c
// 0x006424e0
bool MGM_GetGangNestDestroyed(int gangNestId)
```
## Description
```c
Just does what it says.

bool MGM_GetGangNestDestroyed(int gangNestId)
{
  return ((1 << (a1 % 32)) & gGangNestsDestroyed[a1 / 32]) != 0;
}
```
