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
Forge_version = ""
##################################################
# PaperMC伺服器專用 (Minecraft版本-PaperMC版本)
Paper_version = ""
##################################################
# 最少記憶體
min_ram = ""
# 最大記憶體
max_ram = ""
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

import subprocess
import os
import time
import logging

logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=logging.INFO)

##################################################

logging.info('正在初始化' + serverName)


os.environ["JAVA_HOME"] = ""
os.environ["Path"] = os.environ["JAVA_HOME"] + "\\bin"

again = True
##################################################

while again:

    logging.info('正在啟動伺服器')
    subprocess.run(["java", "-Xms" + min_ram, "-Xmx" + max_ram, "-jar", "server.jar", "--bonusChest"])

    logging.info('伺服器已停止')
    again = True
    answer = input("是否再次啟動伺服器？(Y/N)：")
    for i in range(15):
        time.sleep(1)
        if answer.lower() == "n" or answer.lower() == "no":
            again = False
            break
    if again:
        logging.info('即將重新啟動伺服器')

logging.info('正在停止' + serverName)
exit()