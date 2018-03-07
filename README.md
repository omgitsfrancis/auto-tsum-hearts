# auto-tsum-hearts

Automatically sends hearts (in-game lives) to everyone on your friends list. Uses the pyautogui module for image recognition and the Nox android emulator.

Required:
* pyautogui module - Python image recogination and gui controller
* Nox Andriod Emulator
* Disney Tsum-tsums .apk file

Script will:
*	Locate emulator on desktop.
*	Scroll to the top of friends list.
*	Collect coordinates of all hearts visible on screen.
*	Send hearts individually to saved coordinate.
*	Scroll down to next batch of friends.
*	Repeat till bottom of friends list.


Nox settings:

Advance Settings

- Performance Settings:	Low
- Startup Settings	800x600

Interface Settings

- Window Size and...:	Fixed window size
