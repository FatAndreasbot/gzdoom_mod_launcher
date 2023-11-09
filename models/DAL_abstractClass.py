from abc import ABC, abstractmethod
from models.modfile import Mod
from models.modpack import Modpack


class abstractDAL(ABC):
    
    
    @abstractmethod
    def __init__(self):
        pass
    
    
    @abstractmethod
    def GetAllModpacks(self):
        pass
    
    @abstractmethod
    def GetMods(self, modpackID: int):
        pass
    
    @abstractmethod
    def AddModpack(self,modpack:Modpack):
        pass
    
    @abstractmethod
    def RemoveModpack(self, modpackId:int):
        pass
    
    @abstractmethod
    def AddMod(self, modpackID:int, mod:Mod):
        pass
    
    @abstractmethod
    def RemoveMod(self, modpackID:int, modID:int):
        pass
    
    @abstractmethod
    def EditModpack(self, modpackID:int, editedModpack:Modpack):
        pass
    
    @abstractmethod
    def EditMod(self, modpackID:int, modID:int, editedMod:Mod):
        pass