import os
from time import sleep
import sys
from datetime import datetime

PZserver_serverlog="C:/Users/Testing/Zomboid/Logs" # <Your location>/Zomboid/Logs
server_ip="127.0.0.1" # Use local IP example: 127.0.0.1
rcon_port="27015" # Check in servertest.ini for the RCONPort
rcon_password="123456789" # Check in servertest.ini for the RCONPassword
time=10 # Amount of time before restarting server. IN SECONDS !!
loop_time=20 # time loop of the update. IN SECONDS !! Recommend 10 minutes = 600 seconds

#-------------Check OS-------------
OS=sys.platform
if (OS == "win32"):
    #-------Windows Config-------
    rcon_path="C:/Users/Testing/Downloads/rcon-0.10.3-win64/rcon-0.10.3-win64/rcon.exe" # The location where rcon.exe located (Change base on your system)
    startserver_path="""C:/Users/Testing/Downloads/steamcmd/steamapps/common/PZserver/StartServer64.bat""" # Location of StartServer.bat (Change base on your system)
    rcon_command=f"{rcon_path} -a {server_ip}:{rcon_port} -p {rcon_password} -T 100s"
    command_restart=f"""start cmd /k {startserver_path}"""
    #-----------------------------
elif (OS == "linux"):
    #-------Linux Config-------
    startserver_path="/opt/pzserver/'Project Zomboid Dedicated Server'/start_server.sh" # Location of start_server.sh (Change base on your system)
    rcon_command=f"rcon -a {server_ip}:{rcon_port} -p {rcon_password}"
    command_restart="""bash {startserver_path} """
    #--------------------------
else:
    print("Error: can't detect OS")
    exit()
#------------------------------------


#--------Rcon Command-------- (Don't change anything !!) 
command_checkupdate=f"{rcon_command} checkModsNeedUpdate"
command_servermsg=f"""{rcon_command} "servermsg \"New_workshop_update._Server_will_restart_in_{time}_seconds\""  """
command_quit=f"{rcon_command} quit"
#----------------------------

def check_log(content: str):
    dir_log=os.listdir(PZserver_serverlog)
    for i in dir_log:
        if "DebugLog-server.txt" in i:
            debuglog_file=i
    checkupdate_log=[]
    with open(f"{PZserver_serverlog}/{debuglog_file}",'r') as file:
        content_lines=file.readlines()
        for i in content_lines:
            if (content in i):
                checkupdate_log.append(i)
    return checkupdate_log

def update_server(time: int):
    os.system(command_servermsg)
    sleep(time)
    os.system(command_quit)
    while True:
        check_state=check_log("ZNet: Shutting down Steam Game Server")
        if (check_state): 
            os.system(command_restart)
            print("(*) Reseting Server")
            break
        sleep(2)
    # Wait until PZ server is back again
    while True:
        check_state=check_log("*** SERVER START *****")
        if (check_state): break
        sleep(5)

if __name__ == '__main__' :
    while True:
        os.system(command_checkupdate) # Check mods need update
        sleep(3)
        #Find the path way to DebugLog-server
        dir_log=os.listdir(PZserver_serverlog)
        for i in dir_log:
            if "DebugLog-server.txt" in i:
                debuglog_file=i

        #Find CheckModsNeedUpdate log
        while True:
            checkupdate_log=[]
            with open(f"{PZserver_serverlog}/{debuglog_file}",'r') as file:
                content_lines=file.readlines()
                #print(content_lines)
                for i in content_lines:
                    if ("CheckModsNeedUpdate" in i):
                        checkupdate_log.append(i)
            #print(checkupdate_log)
            if  "CheckModsNeedUpdate: Checking" in checkupdate_log[len(checkupdate_log)-1]: 
                sleep(5)
                current_datetime = datetime.now()
                print(f"(#){current_datetime}: checking")
            elif "CheckModsNeedUpdate: Mods updated" in checkupdate_log[len(checkupdate_log)-1]: 
                current_datetime = datetime.now()
                print(f"(#){current_datetime}: There is no new update")
                break
            elif "CheckModsNeedUpdate: Mods need update" in checkupdate_log[len(checkupdate_log)-1]: 
                current_datetime = datetime.now()
                print(f"(#){current_datetime}: Updating Mod")
                update_server(time)
                break
        sleep(loop_time)

