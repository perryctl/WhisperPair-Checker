# Whisper Pair Checker

This repository can simply determine if you have any bluetooth devices that are vulnerable to WhisperPair. For more details, see: https://whisperpair.eu/ and https://www.cve.org/CVERecord?id=CVE-2025-36911

## How to run this script
- You must have a bluetooth chip on the computer you will be running this script on.
- You must have python 3 installed.
- You must install the third party python package - [bleak](https://pypi.org/project/bleak/). You can do this via - ```pip install bleak```
- You can then run the script via - ```python whisperPair.py```

## Notes
- Make sure you're holding your bluetooth device quite close to your bluetooth chip on your computer.
- Do not use this script as a one stop shop for determining if you are safe.

## What to do now?
- Check for firmware updates from your manufacturer, normally using the headphones companion app, and updating your phone if you're on Android!
