#################################################################################################
# 加載功能
# 無需編輯
import subprocess
import os
import time
import logging
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=logging.INFO)
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=logging.ERROR)
version = 0
#################################################################################################
# Minecraft伺服器啟動器(Python) 0.1
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
serverName = "Minecraft伺服器啟動器(Python) 0.1"
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

logging.info('正在初始化' + serverName)

os.environ["JAVA_HOME"] = ""
os.environ["Path"] = os.environ["JAVA_HOME"] + "\\bin"

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

# Check java
if again:
    logging.info('Checking Java Directory')
    if version in range(1,3,1): # version 1,2,3
        if java8 == "":
            again = False
            logging.error('No Java Directory Found')
    if version in range(4,6,1): # version 4,5,6
        if java17 == "":
            again = False
            logging.error('No Java Directory Found')
    if version in [2,5,8]:
        logging.info('Checking Forge Version')
        if forgeVersion == "":
            again = False
            logging.error('No Forge Version Found')
    if version in [3,6,9]:
        logging.info('Checking Paper Version')
        if paperVersion == "":
            again = False
            logging.error('No Paper Version Found')


while again: # Server Loop
    again = False
    
    # Start Server
    logging.info('正在啟動伺服器')
    subprocess.run(["java", "-Xms" + minRam, "-Xmx" + maxRam, "-jar", "server.jar", "--bonusChest"])
    # Server Stopped
    logging.info('伺服器已停止')
    # Ask for run again
    again = True
    answer = input("是否再次啟動伺服器？(Y/N)：")
    for i in range(15):
        time.sleep(1)
        if answer.lower() == "n" or answer.lower() == "no":
            again = False
            break
    if again:
        logging.info('即將重新啟動伺服器')

# Stopping Script
logging.info('正在停止' + serverName)
exit()