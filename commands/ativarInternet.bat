@echo off
title Cyber Manager
color 3f
wmic path win32_networkadapter where index=1 call enable

pause
