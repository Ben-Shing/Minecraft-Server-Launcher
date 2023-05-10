#################################################################################################
# Minecraft Server Launcher(Python)
# This is a Python script
# The script will automatically restart the server when server stoped
# To shutdown the server, use /stop in the server and type "N" when asking "Start again? (Y/N)"N"
#################################################################################################
# Please notice that this script has no download function
# You should download and install the server on your own
# You should also complete the variable below before running this script
# This script is created by BenShing
#################################################################################################

import subprocess
import os
import logging
import datetime

##################################################

now = datetime.datetime.now()
date_time = now.strftime("%Y-%m-%d-%H-%M-%S")

propertiesFile = 'MinecraftServerLauncher.properties'
properties = {
    "server-name": "",
    "launcher-version": "",
    "runtime-version": "",
    "forge-version": "",
    "paper-version": "",
    "min-ram": "",
    "max-ram": "",
    "java8": "",
    "java17": ""
    }
properties["launcher-version"] = "v0.0.2-alpha"
properties["runtime-version"] = 0
defaultRam = ["512M","1G"]
properties["server-name"] = "Minecraft Server Launcher(Python) " + properties["launcher-version"]

##################################################

# Functions
def cmd_choice(timeout=15, default='Y'):
    process = subprocess.Popen(['cmd.exe', '/c', 'choice /C YNP /N /T {} /D {}'.format(timeout, default)], stdout=subprocess.PIPE)
    output, error = process.communicate()
    choice = output.strip().decode('utf-8')
    if choice == 'P':
        pause()
        return 'N'
    else:
        return choice

def pause():
    input("Press Enter to continue...")

##################################################

#logging setup
if not os.path.exists("log"):
    os.mkdir("log")

logger = logging.getLogger('main')
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

filename = f"{date_time}.log"
filenameWithDir = os.path.join("log", filename)
file_handler = logging.FileHandler(filenameWithDir)
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

##################################################

if os.path.isfile(propertiesFile):
    with open(propertiesFile, 'r') as propertiesFile:
        for line in propertiesFile:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            key, value = line.split('=', 1)
            key = key.strip()
            value = value.strip()
            if not value:
                continue
            else:
                properties[key] = value
    try:
        properties["runtime-version"] = int(properties["runtime-version"])
    except:
        properties["runtime-version"] = -1
else:
    logger.critical('Could not find properties file')
    logger.critical('Exiting...')
    pause()
    exit()

##################################################

logger.info('Initializing ' + properties["server-name"])

again = True

##################################################

# Check version
logger.info('Checking Launcher Version')
if properties["runtime-version"] == 0:
    logger.error('No Runtime Version Selected')
    again = False
elif properties["runtime-version"] < 0 or properties["runtime-version"] > 9:
    logger.error('Uncorrect Runtime Version Selected')
    again = False

# Check java & others
if again:
    logger.info('Checking Java Directory')
    java_path = None
    if properties["runtime-version"] in range(1,3,1): # version 1,2,3
        if properties["java8"] == "":
            again = False
            logger.error('No Java 8 Directory Found')
        else:
            java_path = properties["java8"]
    if properties["runtime-version"] in range(4,6,1): # version 4,5,6
        if properties["java17"] == "":
            again = False
            logger.error('No Java 17 Directory Found')
        else:
            java_path = properties["java17"]
    if java_path:
        os.environ["JAVA_HOME"] = java_path
        os.environ["Path"] = os.path.join(java_path, "\\bin")

    if properties["runtime-version"] in [2,5,8]: # version 2,5,8
        logger.info('Checking Forge Version')
        if properties["forge-version"] == "":
            again = False
            logger.error('No Forge Version Found')
    
    if properties["runtime-version"] in [3,6,9]: # version 3,6,9
        logger.info('Checking PaperMC Version')
        if properties["paper-version"] == "":
            again = False
            logger.error('No PaperMC Version Found')

# Check ram setting
if properties["min-ram"] == "":
    logger.info('Missing minRam value, setting minRam to {}'.format(defaultRam[0]))
    minRam = defaultRam[0]
if properties["max-ram"] == "":
    logger.info('Missing maxRam value, setting maxRam to {}'.format(defaultRam[1]))
    maxRam = defaultRam[1]

# Pause before exit
if not again:
    pause()

while again: # Server Loop
    again = False

    # Start Server
    logger.info('Starting Server')
    if properties["runtime-version"] in [1,4,7]: # version 1,4,7
        serverfile = "server.jar"
        if os.path.isfile(serverfile):
            subprocess.run(["java", "-Xms" + minRam, "-Xmx" + maxRam, "-jar", "server.jar", "--bonusChest"])
        else:
            logger.critical('Could not find server file: ' + serverfile)
            logger.critical('Exiting...')
            pause()
            exit()
    elif properties["runtime-version"] in [2,5,8]: # version 2,5,8
        if properties["forge-version"].split("-")[0] in ["1.7","1.8","1.9","1.10","1.11","1.12","1.13","1.14","1.15","1.16"]:
            serverfile = "forge-" + properties["forge-version"] + ".jar"
            if os.path.isfile(serverfile):
                subprocess.run(["java", "-Xms" + minRam, "-Xmx" + maxRam, "-jar", "forge-" + properties["forge-version"] + ".jar", "--bonusChest"])
            else:
                logger.critical('Could not find server file: ' + serverfile)
                logger.critical('Exiting...')
                pause()
                exit()
        else:
            serverfile = os.path.join("libraries", "net", "minecraftforge", "forge", properties["forge-version"], properties["forge-version"] + "-server.jar")
            if os.path.isfile(serverfile):
                subprocess.run(["java", "-Xms" + minRam, "-Xmx" + maxRam, "@libraries/net/minecraftforge/forge/" + properties["forge-version"] + "/win_args.txt", "--bonusChest"])
            else:
                logger.critical('Could not find server file: ' + serverfile)
                logger.critical('Exiting...')
                pause()
                exit()
    elif properties["runtime-version"] in [3,6,9]: # version 3,6,9
        serverfile = "paper-" + properties["paper-version"] + ".jar"
        if os.path.isfile(serverfile):
            subprocess.run(["java", "-Xms" + minRam, "-Xmx" + maxRam, "-jar", "paper-" + properties["paper-version"] + ".jar"])
        else:
            logger.critical('Could not find server file: ' + serverfile)
            logger.critical('Exiting...')
            pause()
            exit()
    else:
        logger.error('Version Error, this should be a bug')
    # Server Stopped
    logger.info('Server Stopped')
    # Ask for run again
    again = True
    logger.info("Start again?(Y/N): ")
    answer = cmd_choice()
    if answer == 'N':
        again = False
    if again:
        logger.info('Restarting Server')

# Stopping Script
logger.info('Stopping ' + properties["server-name"])
exit()