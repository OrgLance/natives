# TODObject
## Functions
| Function | Note |
|----------|------|
|[EnableRain](EnableRain.md)| |
|[EnableTODUpdate](EnableTODUpdate.md)| |
|[GetTimeHour](GetTimeHour.md)| |
|[GetTimeMinute](GetTimeMinute.md)| |
|[IsRaining](IsRaining.md)| |
|[IsUpdating](IsUpdating.md)| |
|[SetTime](SetTime.md)| |
## Description
```
The TODObject aka. TimeOfDay Object manages Weather and Time.
It's very useful to create a dark atmosphere.
```
## Example

An Example how to get the current Time:
```php
$tod = FindObject("TODObject");
$currentHour = tod.GetTimeHour();
$currentMinute = tod.GetTimeMinute();

// We can log DebugMsg
DebugMsg("TOD", "Current Hour: " @ %currentHour);
DebugMsg("TOD", "Current Minute: " @ %currentMinute);
```

An Example how to set the current Time:
```php
$tod = FindObject("TODObject");

// Setting the Time to 12:12:12
tod.SetTime(12, 12, 12);
```