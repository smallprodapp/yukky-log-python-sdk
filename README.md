# Yukky Log Python SDk

Easy to use SDK to send log to Yukky Log !

For more informations visit https://log.yukkyapp.com/doc

## Installation

Download the Python file named **yukkylog.py** and put it in your project.

You might need to download the Python package **requests**

```
pip install requests
```

**That's it !**

## Initialisation

Somewhere in your code you should add this :

```
from yukkylog import YukkyLog
YukkyLog.init('<appkey>', '<appsecret>')
```

This will initialize the SDK.

You can add a third parameter to specify if you want the debug mode.

## Send some logs

### Error

To send an error log simply add this line :

```
YukkyLog.error({'name': 'Python Test', 'tags': ['Python', 'Test'], 'desc': '', 'infos': ''})
```

### Warning

To send a warning log simply add this line :

```
YukkyLog.warning({'name': 'Python Test', 'tags': ['Python', 'Test'], 'desc': '', 'infos': ''})
```

### Info

To send an info log simply add this line :

```
YukkyLog.info({'name': 'Python Test', 'tags': ['Python', 'Test'], 'desc': '', 'infos': ''})
```

### Custom

To send a custom log simply add this line :

```
YukkyLog.error({'name': 'Python Test', 'tags': ['Python', 'Test'], 'desc': '', 'infos': '', 'type', 'custom type'})
```
