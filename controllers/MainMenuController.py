from models.modpack import Modpack, Mod
from models.DAL_abstractClass import abstractDAL
import subprocess
import multiprocessing


class MainMenuController:
    def __init__(self, DAL: abstractDAL):
        """Init app controller."""
        self.dal = DAL
        
    
    def CreateModPack():
        print("CreateModPack not implemented")
        
    def DeleteModPack(self, modpackID:int):
        self.dal.RemoveModpack(modpackID)
        
    def Play(self, modpackID:int):
        modlist = self.dal.GetMods(modpackID)
        # command = ["flatpak", "run", "org.zdoom.GZDoom"]
        command = ["/usr/bin/gzdoom"]
        
        for v in modlist:
            command.append("-file")
            command.append(v.file_path)
        
        def run():
            subprocess.run(command)    
        
        p1 = multiprocessing.Process(target=run)
        p1.start()
        
        
        
    def AddMod(self, path, name, modpackID):
        # addModWindowDialiog = AddModWindowDialiog(parent)
        # addModWindowDialiog.show()
        mod = Mod(path, name)
        self.dal.AddMod(modpackID, mod)
        
        
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

        
