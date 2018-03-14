# auto-tsum-hearts

## What is Auto Tsum Hearts?
Auto Tsum Hearts is a bot for the popular mobile game, Disney Tsum Tsums. This script automatically sends hearts (in-game lives) to everyone on your friends list. Uses the pyautogui module for image recognition and the Nox android emulator.

## How to use:
**Required:**
* pyautogui module - Python image recogination and gui controller http://pyautogui.readthedocs.io/en/latest/
* Nox Player Andriod Emulator - https://www.bignox.com/
* Disney Tsum-tsums .apk file - https://apkpure.com/line-disney-tsum-tsum/com.linecorp.LGTMTMG
* Latest Version of python


**Setup**
1. Install Nox Android Emulator
2. Change Nox settings: Advance Settings(Performance Settings:	Low, Startup Settings	800x600)
3. Install Tsum tsum apk on emulator
4. Start Tsum Tsums and goto friends page
5. Run autoTsum.py

**Script will:**
*	Locate emulator on desktop.
*	Scroll to the top of friends list.
*	Collect coordinates of all hearts visible on screen.
*	Send hearts individually to saved coordinate.
*	Scroll down to next batch of friends.
*	Repeat till bottom of friends list.



