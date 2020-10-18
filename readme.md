# Service Now Instance Waker


Service Now Instance Waker is simple Python script which uses Selenium library to automatically wakeup ServiceNow Developer Instance.


## Why?


ServiceNow Personal Developer instances will go in hibernate state every 6 hours of inactivity. 😴

In Addition to that if your instance is inactive for 10 days you will lose instance with all of its data. ☠

If you have 4-5 instances to Wakeup everyday it becomes boring 💤

## Features


   -  Checks every 5 Min if instance is Online.
   -  Checks 5 Times for each Instance.
   -  Will Notify Using Sound when all instance are online or if any one failed. 
   -  Can be scheduled Using Windows Task Scheduler to wake up instances every day. 
   -  Uses Python Multithread Library


## Requirements and Setup
### Requirements


- [Firefox](https://www.mozilla.org/en-US/firefox/new/ "Firefox") 
- Correct version of [geckodriver](https://github.com/mozilla/geckodriver/releases "GitHub geckodriver") (Download Version Supported by firefox installed on your PC)

### Setup 
 - Download correct version of geckodriver and Replace one in project.
 - Enter Instance Details in InstanceCreads.JSON 
 - Run main.py eg.` python main.py `
