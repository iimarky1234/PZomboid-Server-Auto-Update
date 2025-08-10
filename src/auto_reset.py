import os
from time import sleep
from datetime import datetime
from rcon.source import Client
import yaml

class PZ_autoupdate:
    def __init__(self, SERVER_LOG, SERVER_IP, RCON_PORT, RCON_PASSWORD, TIME_BEFORE_RESTART, LOOP_TIME):
        self.SERVER_LOG = SERVER_LOG
        self.SERVER_IP = SERVER_IP
        self.RCON_PORT= RCON_PORT
        self.RCON_PASSWORD = RCON_PASSWORD
        self.TIME_BEFORE_RESTART = TIME_BEFORE_RESTART
        self.LOOP_TIME = LOOP_TIME

    def rcon_command(self,command: str):
        with Client(self.SERVER_IP, self.RCON_PORT, passwd = self.RCON_PASSWORD) as client:
            response = client.run(command)
        return response

    def check_log(self,content: str):
        dir_log=os.listdir(self.SERVER_LOG)
        for i in dir_log:
            if "DebugLog-server.txt" in i:
                debuglog_file=i
        log=[]
        with open(f"{self.SERVER_LOG}/{debuglog_file}",'r') as file:
            content_lines=file.readlines()
            for i in content_lines:
                if (content in i):
                    log.append(i)
        return log
    
    def update_server(self):
        self.rcon_command(f"servermsg \"New workshop update. Server will restart in {self.TIME_BEFORE_RESTART} seconds\"")
        sleep(self.TIME_BEFORE_RESTART)
        self.rcon_command("quit")
        while True:
            check_state=self.check_log("ZNet: Shutting down Steam Game Server")
            if (check_state): 
                self.rcon_command("quit")
                print("(*) Reseting Server")
                break
            sleep(2)
        while True:
            check_state=self.check_log("*** SERVER START *****")
            if (check_state): break
            sleep(5)
    

if __name__ == '__main__' :
    # Load the config
    with open('config.yaml') as data: config=yaml.load("config.json",Loader=yaml.FullLoader)
    
    PZ=PZ_autoupdate(**config)
    
    while True:
        PZ.rcon_command("checkModsNeedUpdate")
        sleep(3)
        checkupdate_log=PZ.check_log("CheckModsNeedUpdate")
        if  "CheckModsNeedUpdate: Checking" in checkupdate_log[-1]: 
            sleep(5)
            current_datetime = datetime.now()
            print(f"(#){current_datetime}: checking")
        elif "CheckModsNeedUpdate: Mods updated" in checkupdate_log[-1]: 
            current_datetime = datetime.now()
            print(f"(#){current_datetime}: There is no new update")
            break
        elif "CheckModsNeedUpdate: Mods need update" in checkupdate_log[-1]: 
            current_datetime = datetime.now()
            print(f"(#){current_datetime}: Updating Mod")
            PZ.update_server()
            break
        sleep(PZ.LOOP_TIME)

