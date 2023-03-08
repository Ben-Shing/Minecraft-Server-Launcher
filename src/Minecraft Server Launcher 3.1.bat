@echo off
REM===================================
::Minecraft Server Launcher 3.1
::This is a script that start a minecraft server
::The script will automatically restart the server when server stoped
::To shutdown the server, use /stop in the server and type "N" when asking "Start again? (Y/N)"
::<!>Please notice that it won't download any file itself<!>
::<!>You should download and install the server on your own<!>
::<!>You should also complete the variable below unless you see (Optional)<!>
::This script is created by BenShing
REM===================================
::Server name here(Optional)
set server_name=
REM===================================
::version=1 --> Minecraft 1.12-1.16
::version=2 --> Minecraft 1.12-1.16 (Forge)
::version=3 --> Minecraft 1.12-1.16 (PaperMC)
::version=4 --> Minecraft 1.18+
::version=5 --> Minecraft 1.18+ (Forge)
::version=6 --> Minecraft 1.18+ (PaperMC)
::version=7 --> Using Default Java
::version=8 --> Using Default Java (Forge)
::version=9 --> Using Default Java (PaperMC)
set version=
REM===================================
::For (Forge) version ONLY (MinecraftVersion-ForgeVersion)
set Forge_version=
REM===================================
::For (PaperMC) version ONLY (MinecraftVersion-PaperMCVersion)
set Paper_version=
REM===================================
::Minimum ram
set min_ram=
::Maximum ram
set max_ram=
::Example : 512M / 8G
::<!> M=Megabyte ; G=Gigabyte<!>
REM===================================
::Set Java Directory Here (Use a full directory like this: "C:\Program Files\Java\jre1.8.0_291")
::Java usually inside "C:\Program Files\Java\..."
::Java 8 Directory (For version 1/2)
set java8=
::Java 17 Directory (For version 3/4)
set java17=
REM===================================

::<!>The code below will run the server, nothing need to be edited after this line<!>

title Minecraft Server Launcher 3.1
set input=
set pathBackup=%path%

for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do rem"') do set ESC=%%b

:restart
title Minecraft Server %server_name%
echo ^<System^> %ESC%[32mPreparing Minecraft Server......%ESC%[0m
if "%version%"=="1" goto version1
if "%version%"=="2" goto version2
if "%version%"=="3" goto version3
if "%version%"=="4" goto version4
if "%version%"=="5" goto version5
if "%version%"=="6" goto version6

:version1
echo ^<System^> %ESC%[36mChanging to Java 8%ESC%[0m
set JAVA_HOME=%java8%
set Path=%JAVA_HOME%\bin
echo ^<System^> %ESC%[32mStarting Version 1 Server Launcher......%ESC%[0m
java -Xms%min_ram% -Xmx%max_ram% -jar server.jar --bonusChest
goto stoped

:version2
echo ^<System^> %ESC%[36mChanging to Java 8%ESC%[0m
set JAVA_HOME=%java8%
set Path=%JAVA_HOME%\bin
echo ^<System^> %ESC%[32mStarting Version 2 Server Launcher......%ESC%[0m
java -Xms%min_ram% -Xmx%max_ram% -jar forge-%Forge_version%.jar --bonusChest
goto stoped

:version3
echo ^<System^> %ESC%[36mChanging to Java 8%ESC%[0m
set JAVA_HOME=%java8%
set Path=%JAVA_HOME%\bin
echo ^<System^> %ESC%[32mStarting Version 3 Server Launcher......%ESC%[0m
java -Xms%min_ram% -Xmx%max_ram% -jar paper-%Paper_version%.jar
goto stoped

:version4
echo ^<System^> %ESC%[36mChanging to Java 17%ESC%[0m
set JAVA_HOME=%java17%
set Path=%JAVA_HOME%\bin
echo ^<System^> %ESC%[32mStarting Version 4 Server Launcher......%ESC%[0m
java -Xms%min_ram% -Xmx%max_ram% -jar server.jar --bonusChest
goto stoped

:version5
echo ^<System^> %ESC%[36mChanging to Java 17%ESC%[0m
set JAVA_HOME=%java17%
set Path=%JAVA_HOME%\bin
echo ^<System^> %ESC%[32mStarting Version 5 Server Launcher......%ESC%[0m
java -Xms%min_ram% -Xmx%max_ram% @libraries/net/minecraftforge/forge/%Forge_version%/win_args.txt --bonusChest 
goto stoped

:version6
echo ^<System^> %ESC%[36mChanging to Java 17%ESC%[0m
set JAVA_HOME=%java17%
set Path=%JAVA_HOME%\bin
echo ^<System^> %ESC%[32mStarting Version 6 Server Launcher......%ESC%[0m
java -Xms%min_ram% -Xmx%max_ram% -jar paper-%Paper_version%.jar
goto stoped

:version7
echo ^<System^> %ESC%[36mUsing default java%ESC%[0m
echo ^<System^> %ESC%[32mStarting Version 7 Server Launcher......%ESC%[0m
java -Xms%min_ram% -Xmx%max_ram% -jar server.jar --bonusChest
goto stoped

:version8
echo ^<System^> %ESC%[36mUsing default Java%ESC%[0m
echo ^<System^> %ESC%[32mStarting Version 8 Server Launcher......%ESC%[0m
java -Xms%min_ram% -Xmx%max_ram% @libraries/net/minecraftforge/forge/%Forge_version%/win_args.txt --bonusChest 
goto stoped

:version9
echo ^<System^> %ESC%[36mUsing default java%ESC%[0m
echo ^<System^> %ESC%[32mStarting Version 9 Server Launcher......%ESC%[0m
java -Xms%min_ram% -Xmx%max_ram% -jar paper-%Paper_version%.jar
goto stoped

:stoped
echo ^<System^> %ESC%[36mServer Stoped%ESC%[0m
set Path=%pathBackup%

:repeat
echo ^<System^> %ESC%[33mStart again? (Y/N) Y in 15s%ESC%[0m
choice /C YNP /N /T 15 /D Y
if /i "%errorlevel%"=="1" goto restart
if /i "%errorlevel%"=="2" goto ending
if /i "%errorlevel%"=="3" goto preending
echo %ESC%[1m^<System^> %ESC%[31mERROR:Unknow input%ESC%[0m
goto repeat
:preending
pause
:ending
