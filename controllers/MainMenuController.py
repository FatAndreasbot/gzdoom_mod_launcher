from models.modpack import Modpack, Mod
from models.DAL_abstractClass import abstractDAL
import subprocess
import multiprocessing


def CreateModPack():
    print("CreateModPack not implemented")
    
def DeleteModPack(modpackID:int, dal:abstractDAL):
    
    print("DeleteModPack not implemented")
    
def Play(modpackID:int, dal:abstractDAL):
    modlist = dal.GetMods(modpackID)
    command = ["flatpak", "run", "org.zdoom.GZDoom"]
    
    for v in modlist:
        command.append("-file")
        command.append(v['file_path'])
    
    def run():
        subprocess.run(command)    
    
    p1 = multiprocessing.Process(target=run)
    p1.start()
    
    
    
def AddMod():
    print("CreateMod not implemented")
    
def RemoveMod(modpackID:int, modID:int, dal:abstractDAL):
    dal.RemoveMod(modpackID, modID)
    
