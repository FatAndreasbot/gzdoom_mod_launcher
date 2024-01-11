from models.modpack import Modpack, Mod
from models.DAL_abstractClass import abstractDAL
import subprocess
import multiprocessing
import gi



class MainMenuController:
    def __init__(self, DAL:abstractDAL):
        self.dal = DAL
        
    
    def CreateModPack():
        print("CreateModPack not implemented")
        
    def DeleteModPack(self, modpackID:int):
        self.dal.RemoveModpack(modpackID)
        
    def Play(self, modpackID:int):
        modlist = self.dal.GetMods(modpackID)
        command = ["flatpak", "run", "org.zdoom.GZDoom"]
        
        for v in modlist:
            command.append("-file")
            command.append(v.file_path)
        
        def run():
            subprocess.run(command)    
        
        p1 = multiprocessing.Process(target=run)
        p1.start()
        
        
        
    def AddMod(parent):
        # addModWindowDialiog = AddModWindowDialiog(parent)
        # addModWindowDialiog.show()
        print("not implemented")
        
        
    def RemoveMod(self, modpackID:int, modID:int):
        self.dal.RemoveMod(modpackID, modID)
    
    def GetAllModpacks(self):
        modpackList = self.dal.GetAllModpacks()
        
        def getName(mp:Modpack):
            return(mp.name)
        
        return list(map(getName, modpackList))
    
    def GetModlist(self, modpackID):
        modlist = self.dal.GetMods(modpackID)
        def getName(m:Mod):
            return m.name
        
        return list(map(getName, modlist))
        