#################################################################################################
# 加載功能
# 無需編輯
import subprocess
import os
import logging
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=logging.INFO)
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=logging.ERROR)
version = 0
defaultRam = ["512M","1G"]
#################################################################################################

#################################################################################################
# Minecraft伺服器啟動器(Python) 1.0
# 這是由Python編寫的腳本
# 這個腳本帶有自動重啟伺服器功能，伺服器崩潰或停止時會在15秒後自動重啟
# 如要關閉伺服器，請先在伺服器中使用/stop停止伺服器，然後在詢問是否重啟時輸入"N"
#################################################################################################
# 請注意此腳本沒有下載功能
# 你需要自行下載伺服器檔案，並將伺服器檔案和此腳本放置在同一個資料夾
# 請先填妥下面的參數，再運行此腳本
# 此腳本由 BenShing 製作
#################################################################################################

##################################################
# 伺服器名稱(選填)
serverName = "Minecraft伺服器啟動器(Python) 1.0"
##################################################
# 根據情況選擇版本，取消註解即可
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
# Forge伺服器專用 (Minecraft版本-Forge版本)
forgeVersion = ""
##################################################
# PaperMC伺服器專用 (Minecraft版本-PaperMC版本)
paperVersion = ""
##################################################
# 最少記憶體
minRam = ""
# 最大記憶體
maxRam = ""
# 例子: 512M / 8G
# M=Megabyte
# G=Gigabyte
##################################################
# 設定Java路徑
# 根據情況選填，如使用預設Java則不需填寫
# Java 8 路徑
java8 = ""
# Java 17 路徑
java17 = ""
##################################################
#
#下面的程式碼會執行伺服器代碼，你不會需要修改下面的東西
#

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
    input("按回車鍵繼續...")

##################################################

logging.info('正在初始化' + serverName)

again = True

##################################################

# Check version
logging.info('檢查啟動器版本')
if version == 0:
    logging.error('沒有選擇啟動器版本')
    again = False
elif version < 0 or version > 9: 
    logging.error('錯誤啟動器版本')
    again = False

# Check java & other
if again:
    logging.info('檢查Java路徑')
    if version in range(1,3,1): # version 1,2,3
        if java8 == "":
            again = False
            logging.error('沒有Java 8路徑')
        else:
            os.environ["JAVA_HOME"] = java8
            os.environ["Path"] = os.environ["JAVA_HOME"] + "\\bin"
    if version in range(4,6,1): # version 4,5,6
        if java17 == "":
            again = False
            logging.error('沒有Java 17路徑')
        else:
            os.environ["JAVA_HOME"] = java17
            os.environ["Path"] = os.environ["JAVA_HOME"] + "\\bin"
    if version in [2,5,8]:
        logging.info('檢查Forge版本')
        if forgeVersion == "":
            again = False
            logging.error('沒有設定Forge版本')
    if version in [3,6,9]:
        logging.info('檢查PaperMC版本')
        if paperVersion == "":
            again = False
            logging.error('沒有設定PaperMC版本')

# Check ram setting
if minRam == "":
    logging.info('缺少最少分配記憶體，設定成預設：' + defaultRam[0])
    minRam = defaultRam[0]
if maxRam == "":
    logging.info('缺少最大分配記憶體，設定成預設：' + defaultRam[1])
    maxRam = defaultRam[1]

# Pause before exit
if not again:
    pause()

while again: # Server Loop
    again = False
    
    # Start Server
    logging.info('正在啟動伺服器')
    if version in [1,4,7]: # version 1,4,7
        subprocess.run(["java", "-Xms" + minRam, "-Xmx" + maxRam, "-jar", "server.jar", "--bonusChest"])
    elif version in [2,5,8]: # version 2,5,8
        if forgeVersion.split("-")[0] in ["1.7","1.8","1.9","1.10","1.11","1.12","1.13","1.14","1.15","1.16"]:
            subprocess.run(["java", "-Xms" + minRam, "-Xmx" + maxRam, "-jar", "forge-" + forgeVersion + ".jar", "--bonusChest"])
        else:
            subprocess.run(["java", "-Xms" + minRam, "-Xmx" + maxRam, "@libraries/net/minecraftforge/forge/" + forgeVersion + "/win_args.txt", "--bonusChest"])
    elif version in [3,6,9]:
        subprocess.run(["java", "-Xms" + minRam, "-Xmx" + maxRam, "-jar", "paper-" + paperVersion + ".jar"])
    else:
        logging.error('版本錯誤，你有可能遇到Bug')
    # Server Stopped
    logging.info('伺服器已停止')
    # Ask for run again
    again = True
    logging.info("是否再次啟動伺服器？(Y/N)：")
    answer = cmd_choice()
    if answer == 'N':
        again = False
    if again:
        logging.info('即將重新啟動伺服器')

# Stopping Script
logging.info('正在停止' + serverName)
exit()