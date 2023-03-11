#################################################################################################
# Minecraft Server Launcher(Python) 0.1
# This is a Python script
# The script will automatically restart the server when server stoped
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
#version=1 #--> Minecraft 1.12-1.16
#version=2 #--> Minecraft 1.12-1.16 (Forge)
#version=3 #--> Minecraft 1.12-1.16 (PaperMC)
#version=4 #--> Minecraft 1.18+
#version=5 #--> Minecraft 1.18+ (Forge)
#version=6 #--> Minecraft 1.18+ (PaperMC)
#version=7 #--> Using Default Java
#version=8 #--> Using Default Java (Forge)
#version=9 #--> Using Default Java (PaperMC)
##################################################
# Forge Server Only (MinecraftVersion-ForgeVersion)
Forge_version = ""
##################################################
# PaperMC Server Only (MinecraftVersion-PaperMCVersion)
Paper_version = ""
##################################################
# Minimum Ram
min_ram = ""
# Maximum Ram
max_ram = ""
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

import subprocess
import os
import time
import logging

logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=logging.INFO)

##################################################

logging.info('Initializing ' + serverName)


os.environ["JAVA_HOME"] = ""
os.environ["Path"] = os.environ["JAVA_HOME"] + "\\bin"

again = True
##################################################

while again:

    logging.info('Starting Server')
    subprocess.run(["java", "-Xms" + min_ram, "-Xmx" + max_ram, "-jar", "server.jar", "--bonusChest"])

    logging.info('Server Stoped')
    again = True
    answer = input("Start again?(Y/N): ")
    for i in range(15):
        time.sleep(1)
        if answer.lower() == "n" or answer.lower() == "no":
            again = False
            break
    if again:
        logging.info('Restarting Server')

logging.info('Stoping ' + serverName)
exit()