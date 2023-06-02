#################################################################################################
# Minecraft伺服器啟動器(Python)
# 這是由Python編寫的腳本
# 這個腳本帶有自動重啟伺服器功能，伺服器崩潰或停止時會在15秒後自動重啟
# 如要關閉伺服器，請先在伺服器中使用/stop停止伺服器，然後在詢問是否重啟時輸入"N"
#################################################################################################
# 請注意此腳本沒有下載功能
# 你需要自行下載伺服器檔案，並將伺服器檔案和此腳本放置在同一個資料夾
# 請先填妥下面的參數，再運行此腳本
# 此腳本由 BenShing 製作
#################################################################################################

import subprocess
import os
import logging
import datetime

##################################################

now = datetime.datetime.now()
date_time = now.strftime("%Y-%m-%d-%H-%M-%S")

propertiesFile = os.path.join("MinecraftServerLauncher", 'MinecraftServerLauncher.properties')
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
properties["launcher-version"] = "v0.0.2-alpha.1"
properties["runtime-version"] = 0
defaultRam = ["512M","1G"]
properties["server-name"] = "Minecraft Server Launcher ZH(Python) " + properties["launcher-version"]
environBackup = os.environ["Path"]

##################################################

# Functions
def cmd_choice(timeout=15, default='Y'):
    temp = os.environ["Path"]
    os.environ["Path"] = environBackup
    process = subprocess.Popen(['cmd.exe', '/c', 'choice /C YNP /N /T {} /D {}'.format(timeout, default)], stdout=subprocess.PIPE)
    output, error = process.communicate()
    os.environ["Path"] = temp
    choice = output.strip().decode('utf-8')
    if choice == 'P':
        pause()
        return 'N'
    else:
        return choice

def pause():
    input("按回車鍵繼續...")

##################################################

#logging setup
from MinecraftServerLauncher import ColorLog

if not os.path.exists(os.path.join("MinecraftServerLauncher", "logs")):
    os.mkdir(os.path.join("MinecraftServerLauncher", "logs"))

logger = logging.getLogger('main')
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

filename = f"{date_time}.log"
filenameWithDir = os.path.join("MinecraftServerLauncher", "logs", filename)
file_handler = logging.FileHandler(filenameWithDir)
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
formatterText = "%(asctime)s %(levelname)s: %(message)s"

try:
    from MinecraftServerLauncher import ColorLog
    console_handler.setFormatter(ColorLog.ColorFormatter(formatterText))
except ImportError:
    console_handler.setFormatter(formatterText)
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
    logger.critical('無法找到 properties 檔案')
    logger.critical('正在停止...')
    pause()
    exit()

##################################################

logger.info('正在初始化' + properties["server-name"])

again = True

##################################################

# Check version
logger.info('檢查啟動器版本')
if properties["runtime-version"] == 0:
    logger.error('沒有選擇啟動器版本')
    again = False
elif properties["runtime-version"] < 0 or properties["runtime-version"] > 9:
    logger.error('錯誤啟動器版本')
    again = False

# Check java & other
if again:
    logger.info('檢查Java路徑')
    java_path = None
    if properties["runtime-version"] in range(1,3,1): # version 1,2,3
        if properties["java8"] == "":
            again = False
            logger.error('沒有Java 8路徑')
        else:
            java_path = properties["java8"]
    if properties["runtime-version"] in range(4,6,1): # version 4,5,6
        if properties["java17"] == "":
            again = False
            logger.error('沒有Java 17路徑')
        else:
            java_path = properties["java17"]
    if java_path:
        os.environ["JAVA_HOME"] = java_path
        os.environ["Path"] = os.path.join(java_path, "bin")
    
    if properties["runtime-version"] in [2,5,8]:
        logger.info('檢查Forge版本')
        if properties["forge-version"] == "":
            again = False
            logger.error('沒有設定Forge版本')
            
    if properties["runtime-version"] in [3,6,9]:
        logger.info('檢查PaperMC版本')
        if properties["paper-version"] == "":
            again = False
            logger.error('沒有設定PaperMC版本')

# Check ram setting
if properties["min-ram"] == "":
    logger.info('缺少最少分配記憶體，設定成預設：{}'.format(defaultRam[0]))
    minRam = defaultRam[0]
if properties["min-ram"] == "":
    logger.info('缺少最大分配記憶體，設定成預設：{}'.format(defaultRam[1]))
    maxRam = defaultRam[1]

# Pause before exit
if not again:
    pause()

while again: # Server Loop
    again = False
    
    # Start Server
    logger.info('正在啟動伺服器')
    if properties["runtime-version"] in [1,4,7]: # version 1,4,7
        serverfile = "server.jar"
        if os.path.isfile(serverfile):
            subprocess.run(["java", "-Xms" + minRam, "-Xmx" + maxRam, "-jar", "server.jar", "--bonusChest"])
        else:
            logger.critical('無法找到伺服器檔案：' + serverfile)
            logger.critical('正在停止...')
            pause()
            exit()
    elif properties["runtime-version"] in [2,5,8]: # version 2,5,8
        if properties["forge-version"].split("-")[0] in ["1.7","1.8","1.9","1.10","1.11","1.12","1.13","1.14","1.15","1.16"]:
            serverfile = "forge-" + properties["forge-version"] + ".jar"
            if os.path.isfile(serverfile):
                subprocess.run(["java", "-Xms" + minRam, "-Xmx" + maxRam, "-jar", "forge-" + properties["forge-version"] + ".jar", "--bonusChest"])
            else:
                logger.critical('無法找到伺服器檔案：' + serverfile)
                logger.critical('正在停止...')
                pause()
                exit()
        else:
            serverfile = os.path.join("libraries", "net", "minecraftforge", "forge", properties["forge-version"], properties["forge-version"] + "-server.jar")
            if os.path.isfile(serverfile):
                subprocess.run(["java", "-Xms" + minRam, "-Xmx" + maxRam, "@libraries/net/minecraftforge/forge/" + properties["forge-version"] + "/win_args.txt", "--bonusChest"])
            else:
                logger.critical('無法找到伺服器檔案：' + serverfile)
                logger.critical('正在停止...')
                pause()
                exit()
    elif properties["runtime-version"] in [3,6,9]:
        serverfile = "paper-" + properties["paper-version"] + ".jar"
        if os.path.isfile(serverfile):
            subprocess.run(["java", "-Xms" + minRam, "-Xmx" + maxRam, "-jar", "paper-" + properties["paper-version"] + ".jar"])
        else:
            logger.critical('無法找到伺服器檔案：' + serverfile)
            logger.critical('正在停止...')
            pause()
            exit()
    else:
        logger.error('版本錯誤，你有可能遇到Bug')
    # Server Stopped
    logger.info('伺服器已停止')
    # Ask for run again
    again = True
    logger.info("是否再次啟動伺服器？(Y/N)：")
    answer = cmd_choice()
    if answer == 'N':
        again = False
    if again:
        logger.info('即將重新啟動伺服器')

# Stopping Script
logger.info('正在停止' + properties["server-name"])
exit()