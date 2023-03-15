#################################################################################################
# Importing dependents
# No need to edit
import subprocess
import os
import logging
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=logging.INFO)
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=logging.ERROR)
version = 0
#################################################################################################
# Minecraft Server Launcher(Python) 0.1
# This is a Python script
# The script will automatically restart the server when server stoped (Currently not done)
# To shutdown the server, use /stop in the server and type "N" when asking "Start again? (Y/N)"N"
#################################################################################################
# Please notice that this script has no download function
# You should download and install the server on your own
# You should also complete the variable below before running this script
# This script is created by BenShing
#################################################################################################

##################################################
# Server Name(Optional)
serverName = "Minecraft Server Launcher(Python) 0.1"
##################################################
# Uncomment the version you needed
#version = 1 #--> Minecraft 1.12-1.16
#version = 2 #--> Minecraft 1.12-1.16 (Forge)
#version = 3 #--> Minecraft 1.12-1.16 (PaperMC)
#version = 4 #--> Minecraft 1.18+
#version = 5 #--> Minecraft 1.18+ (Forge)
#version = 6 #--> Minecraft 1.18+ (PaperMC)
#version = 7 #--> Using Default Java
#version = 8 #--> Using Default Java (Forge)
#version = 9 #--> Using Default Java (PaperMC)
##################################################
# Forge Server Only (MinecraftVersion-ForgeVersion)
forgeVersion = ""
##################################################
# PaperMC Server Only (MinecraftVersion-PaperMCVersion)
paperVersion = ""
##################################################
# Minimum Ram
minRam = ""
# Maximum Ram
maxRam = ""
# Example: 512M / 8G
# M=Megabyte
# G=Gigabyte
##################################################
# Specify Java Directory (No need to specify if you want to use the default Java)
# 1.16 or below -> Java 8 | 1.18 or above -> Java 17
# Java 8 Directory
java8 = ""
# Java 17 Directory
java17 = ""
##################################################
#
#The code below will run the server, nothing need to be edited
#

##################################################

logging.info('Initializing ' + serverName)

again = True

##################################################

# Check version
logging.info('Checking Launcher Version')
if version == 0:
    logging.error('No Server Version Selected')
    again = False
elif version < 0 or version > 9: 
    logging.error('Uncorrect Version Selected')
    again = False

# Check java & others
if again:
    logging.info('Checking Java Directory')
    if version in range(1,3,1): # version 1,2,3
        if java8 == "":
            again = False
            logging.error('No Java 8 Directory Found')
        else:
            os.environ["JAVA_HOME"] = java8
            os.environ["Path"] = os.environ["JAVA_HOME"] + "\\bin"
    if version in range(4,6,1): # version 4,5,6
        if java17 == "":
            again = False
            logging.error('No Java 17 Directory Found')
        else:
            os.environ["JAVA_HOME"] = java17
            os.environ["Path"] = os.environ["JAVA_HOME"] + "\\bin"
    if version in [2,5,8]: # version 2,5,8
        logging.info('Checking Forge Version')
        if forgeVersion == "":
            again = False
            logging.error('No Forge Version Found')
    if version in [3,6,9]: # version 3,6,9
        logging.info('Checking PaperMC Version')
        if paperVersion == "":
            again = False
            logging.error('No PaperMC Version Found')

if not again:
    pause = input("Click enter to continue")

while again: # Server Loop
    again = False
    
    # Start Server
    logging.info('Starting Server')
    subprocess.run(["java", "-Xms" + minRam, "-Xmx" + maxRam, "-jar", "server.jar", "--bonusChest"])
    # Server Stopped
    logging.info('Server Stopped')
    # Ask for run again
    again = True
    answer = input("Start again?(Y/N): ")
    if answer.lower() == "n" or answer.lower() == "no":
        again = False
    if again:
        logging.info('Restarting Server')

# Stopping Script
logging.info('Stopping ' + serverName)
exit()