#################################################################################################
# Minecraft Server Launcher(Python)
# This is a Python script
# The script will automatically restart the server when server stopped
# To shutdown the server, use /stop in the server and type "N" when asking "Start again? (Y/N)"N"
#################################################################################################
# Please notice that this script has no download function
# You should download and install the server on your own
# This script is created by BenShing
#################################################################################################

# import subprocess
# import os
# import logging
# import datetime

# ##################################################

# # Functions
# def cmd_choice(timeout=15, default='Y', environBackup=os.environ["Path"]):
#     temp = os.environ["Path"]
#     os.environ["Path"] = environBackup
#     process = subprocess.Popen(['cmd.exe', '/c', 'choice /C YNP /N /T {} /D {}'.format(timeout, default)], stdout=subprocess.PIPE)
#     output, error = process.communicate()
#     os.environ["Path"] = temp
#     choice = output.strip().decode('utf-8')
#     if choice == 'P':
#         pause()
#         return 'N'
#     else:
#         return choice

# def pause():
#     input("Press Enter to continue...")


# def old_code():
#     now = datetime.datetime.now()
#     date_time = now.strftime("%Y-%m-%d-%H-%M-%S")

#     propertiesFile = os.path.join("MinecraftServerLauncher", 'MinecraftServerLauncher.properties')
#     properties = {
#         "server-name": "",
#         "launcher-version": "",
#         "runtime-version": "",
#         "forge-version": "",
#         "paper-version": "",
#         "min-ram": "",
#         "max-ram": "",
#         "java8": "",
#         "java17": ""
#     }
#     properties["launcher-version"] = "v0.0.2-alpha.1"
#     properties["runtime-version"] = 0
#     defaultRam = ["512M","1G"]
#     properties["server-name"] = "Minecraft Server Launcher EN(Python) " + properties["launcher-version"]
#     environBackup = os.environ["Path"]

#     ##################################################

#     #logging setup
#     if not os.path.exists(os.path.join("MinecraftServerLauncher", "logs")):
#         os.mkdir(os.path.join("MinecraftServerLauncher", "logs"))

#     logger = logging.getLogger('main')
#     logger.setLevel(logging.INFO)

#     console_handler = logging.StreamHandler()
#     console_handler.setLevel(logging.INFO)

#     filename = f"{date_time}.log"
#     filenameWithDir = os.path.join("MinecraftServerLauncher", "logs", filename)
#     file_handler = logging.FileHandler(filenameWithDir)
#     file_handler.setLevel(logging.INFO)

#     formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
#     formatterText = "%(asctime)s %(levelname)s: %(message)s"

#     try:
#         from MinecraftServerLauncher import ColorLog
#         console_handler.setFormatter(ColorLog.ColorFormatter(formatterText))
#     except ImportError:
#         console_handler.setFormatter(formatterText)
#     file_handler.setFormatter(formatter)

#     logger.addHandler(console_handler)
#     logger.addHandler(file_handler)

#     ##################################################

#     if os.path.isfile(propertiesFile):
#         with open(propertiesFile, 'r') as propertiesFile:
#             for line in propertiesFile:
#                 line = line.strip()
#                 if not line or line.startswith('#'):
#                     continue
#                 key, value = line.split('=', 1)
#                 key = key.strip()
#                 value = value.strip()
#                 if not value:
#                     continue
#                 else:
#                     properties[key] = value
#         try:
#             properties["runtime-version"] = int(properties["runtime-version"])
#         except:
#             properties["runtime-version"] = -1
#     else:
#         logger.critical('Could not find properties file')
#         logger.critical('Stopping...')
#         pause()
#         exit()

#     ##################################################

#     logger.info('Initializing ' + properties["server-name"])

#     again = True

#     ##################################################

#     # Check version
#     logger.info('Checking Launcher Version')
#     if properties["runtime-version"] == 0:
#         logger.error('No Runtime Version Selected')
#         again = False
#     elif properties["runtime-version"] < 0 or properties["runtime-version"] > 12:
#         logger.error('Incorrect Runtime Version Selected')
#         again = False

#     # Check java & others
#     if again:
#         logger.info('Checking Java Directory')
#         java_path = None
#         if properties["runtime-version"] in range(1,3,1): # version 1,2,3
#             if properties["java8"] == "":
#                 again = False
#                 logger.error('No Java 8 Directory Found')
#             else:
#                 java_path = properties["java8"]
#         if properties["runtime-version"] in range(4,6,1): # version 4,5,6
#             if properties["java16"] == "":
#                 again = False
#                 logger.error('No Java 16 Directory Found')
#             else:
#                 java_path = properties["java16"]
#         if properties["runtime-version"] in range(7,9,1): # version 7,8,9
#             if properties["java17"] == "":
#                 again = False
#                 logger.error('No Java 17 Directory Found')
#             else:
#                 java_path = properties["java17"]
#         if java_path:
#             os.environ["JAVA_HOME"] = java_path
#             os.environ["Path"] = os.path.join(java_path, "bin")

#         if properties["runtime-version"] in [2,5,8,11]: # version 2,5,8,11
#             logger.info('Checking Forge Version')
#             if properties["forge-version"] == "":
#                 again = False
#                 logger.error('No Forge Version Found')

#         if properties["runtime-version"] in [3,6,9,12]: # version 3,6,9,12
#             logger.info('Checking PaperMC Version')
#             if properties["paper-version"] == "":
#                 again = False
#                 logger.error('No PaperMC Version Found')

#     # Check ram setting
#     if properties["min-ram"] == "":
#         logger.info('Missing minRam value, setting minRam to {}'.format(defaultRam[0]))
#         minRam = defaultRam[0]
#     if properties["max-ram"] == "":
#         logger.info('Missing maxRam value, setting maxRam to {}'.format(defaultRam[1]))
#         maxRam = defaultRam[1]

#     # Pause before exit
#     if not again:
#         pause()

#     while again: # Server Loop
#         again = False

#         # Start Server
#         logger.info('Starting Server')
#         if properties["runtime-version"] in [1,4,7,10]: # version 1,4,7,10
#             serverfile = "server.jar"
#             if os.path.isfile(serverfile):
#                 subprocess.run(["java", "-Xms" + minRam, "-Xmx" + maxRam, "-jar", "server.jar", "--bonusChest"])
#             else:
#                 logger.critical('Could not find server file: ' + serverfile)
#                 logger.critical('Stopping...')
#                 pause()
#                 exit()
#         elif properties["runtime-version"] in [2,5,8,11]: # version 2,5,8,11
#             if properties["forge-version"].split("-")[0] in ["1.7","1.8","1.9","1.10","1.11","1.12","1.13","1.14","1.15","1.16"]:
#                 serverfile = "forge-" + properties["forge-version"] + ".jar"
#                 if os.path.isfile(serverfile):
#                     subprocess.run(["java", "-Xms" + minRam, "-Xmx" + maxRam, "-jar", "forge-" + properties["forge-version"] + ".jar", "--bonusChest"])
#                 else:
#                     logger.critical('Could not find server file: ' + serverfile)
#                     logger.critical('Stopping...')
#                     pause()
#                     exit()
#             else:
#                 serverfile = os.path.join("libraries", "net", "minecraftforge", "forge", properties["forge-version"], properties["forge-version"] + "-server.jar")
#                 if os.path.isfile(serverfile):
#                     subprocess.run(["java", "-Xms" + minRam, "-Xmx" + maxRam, "@libraries/net/minecraftforge/forge/" + properties["forge-version"] + "/win_args.txt", "--bonusChest"])
#                 else:
#                     logger.critical('Could not find server file: ' + serverfile)
#                     logger.critical('Stopping...')
#                     pause()
#                     exit()
#         elif properties["runtime-version"] in [3,6,9,12]: # version 3,6,9,12
#             serverfile = "paper-" + properties["paper-version"] + ".jar"
#             if os.path.isfile(serverfile):
#                 subprocess.run(["java", "-Xms" + minRam, "-Xmx" + maxRam, "-jar", "paper-" + properties["paper-version"] + ".jar"])
#             else:
#                 logger.critical('Could not find server file: ' + serverfile)
#                 logger.critical('Stopping...')
#                 pause()
#                 exit()
#         else:
#             logger.error('Version Error, this should be a bug')
#         # Server Stopped
#         logger.info('Server Stopped')
#         # Ask for run again
#         again = True
#         logger.info("Start again?(Y/N): ")
#         answer = cmd_choice()
#         if answer == 'N':
#             again = False
#         if again:
#             logger.info('Restarting Server')

#     # Stopping Script
#     logger.info('Stopping ' + properties["server-name"])
#     exit()

##################################################

def main():
    # Import modules
    error_modules = []
    try:
        from custom import actions
        from custom import files
        from custom import logger
        from custom import progressBar
    except ImportError as e:
        print(f'Error: {e}')
        print('Seems that you are missing some files')
        print('Please check your installation')
        print('Stopping...')
        return       


    # ColorLog setup
    import logging
    logger = logger.ColorLog('main', level = logging.DEBUG)


    # ProgressBar setup
    logger.debug('Initializing Progress Bar...')
    handler_progress_bar = progressBar.RichBar()
    properties_progress_bar = progressBar.RichBar()
    logger.info('Progress Bar initialized')

    handler_progress_bar.create('Initializing Handlers',total=3)

    # import time
    # time.sleep(0.9)


    # UserHandler setup
    logger.debug('Initializing User Action Handler...')
    user_handler = actions.UserHandler()
    logger.info('User Action Handler initialized')
    handler_progress_bar.update(1)

    # time.sleep(0.5)


    # ServerHandler setup
    logger.debug('Initializing Server Action Handler...')
    server_handler = files.ServerHandler()
    logger.info('Server Action Handler initialized')
    handler_progress_bar.update(2)

    # time.sleep(0.7)


    # PropertiesHandler setup
    logger.debug('Initializing Properties Handler...')
    properties_handler = files.PropertiesHandler()
    logger.info('Properties Handler initialized')
    handler_progress_bar.update(3)
    # time.sleep(0.5)
    handler_progress_bar.complete()
    # time.sleep(1)

    logger.debug(f'Finding properties file in {properties_handler.propertiesPath()}')
    if not properties_handler.checkFileExist():  # No properties file found, create new
        logger.warning('Could not find properties file')
        logger.info('Creating properties file...')
        if properties_handler.createPropertiesFile():
            logger.info('Properties file created, you should edit the file before running again')
        else:
            logger.critical('Could not create properties file')
        logger.info('Stopping...')
        return
    
    logger.info('Found properties file, reading...')
    server_properties = properties_handler.readPropertiesFile()


    # Adding Fixed properties
    server_properties["launcher-version"] = "v0.0.3-alpha"


    # Check properties
    stop = False
    logger.debug('Checking properties...')
    properties_progress_bar.create('Checking properties', total=6)
    # time.sleep(0.5)
    if server_properties['server-name'] == '':
        logger.warning(f'Server name is not set, setting to default name: Minecraft Server Launcher - {server_properties["launcher-version"]}')
        server_properties['server-name'] = f'Minecraft Server Launcher - {server_properties["launcher-version"]}'
    properties_progress_bar.update(1)
    # time.sleep(0.5)

    if server_properties['min-ram'] == '':
        logger.warning('Missing minRam value, setting minRam to 512M')
        server_properties['min-ram'] = '512M'
    properties_progress_bar.update(2)
    # time.sleep(0.5)
    
    if server_properties['max-ram'] == '':
        logger.warning('Missing maxRam value, setting maxRam to 1G')
        server_properties['max-ram'] = '1G'
    properties_progress_bar.update(3)
    # time.sleep(0.5)

    if server_properties['custom-jdk'] == '':
        logger.info('Custom JDK not set, using default JDK')
    properties_progress_bar.update(4)
    # time.sleep(0.5)

    if server_properties['auto-restart'] == '':
        logger.warning('Auto-restart not set, default to False (Server will not restart automatically)')
        server_properties['auto-restart'] = 'False'
    properties_progress_bar.update(5)
    # time.sleep(0.5)

    if server_properties['auto-restart'].lower() not in ['true', 'false']:
        logger.error('Auto-restart value is not valid, Expected: True or False')
        stop = True
    properties_progress_bar.update(6)
    # time.sleep(0.5)
    
    if stop:
        logger.critical('Got invalid properties, stopping...')
        return
    
    properties_progress_bar.complete()
    logger.info('Properties checking complete')


    # Server auto-restart initialization
    if server_properties['auto-restart'].lower() == 'true':
        logger.info('Initializing server auto-restart...')
        auto_restart = True
    else:
        logger.debug('Skipping server auto-restart initialization')
        auto_restart = False


    # Start server
    while True:
        logger.info('Starting server...')

        ###########################
        # TODO: Start server Here #
        ###########################

        try:
            server_location = server_handler.locateServer()
            logger.info(f'Found server: {server_location}')
        except FileNotFoundError as e:
            logger.critical(e)
            logger.critical('Stopping...')
            return
        
        logger.info('Starting server...')
        server_handler.startServer(min_ram=server_properties['min-ram'], max_ram=server_properties['max-ram'], args=[])
        

        ###########################

        # Server Stopped
        logger.info('Server Stopped')
        if not auto_restart: # Auto-restart is disabled
            break

        # Ask for run again
        logger.info('Auto-restart is enabled')
        logger.info(f'Start again?\nY: Yes\nN: No\nP: Pause')
        answer = user_handler.cmdChoice()
        if answer == 'N':
            break


    # Ending
    logger.debug('Program ended')
    logger.info('Stopping...')
    return

##################################################

if __name__ == "__main__":
    main()
