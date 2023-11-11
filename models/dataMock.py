from models.modfile import Mod
from models.modpack import Modpack
from models.DAL_abstractClass import abstractDAL



class DataAcessMock(abstractDAL):
    def __init__(self):
        self.data = {
            "Modpacks":[
                {
                    "name":"Vanilla Doom",
                    "description":"Doom with no mods",
                    "modlist":[]
                },
                {
                    "name":"Ashes 2063",
                    "description":"A post-apok total conversion",
                    "modlist":[
                        {
                            "name":"Ashes 2063",
                            "file_path":"/home/andreasbot/.config/gzdoom/Mods and maps/Ashes2063Enriched2_23.pk3"
                        }
                    ]
                },
                {
                    "name":"Brutal doom 1monster",
                    "description":"",
                    "modlist":[
                        {
                            "name":"Brutal doom",
                            "file_path":"/home/andreasbot/Games/Doom mods/brutalv21/brutalv21.pk3",
                        },
                        {
                            "name":"1monster map pack",
                            "file_path":"/home/andreasbot/Games/Doom mods/1monster/1monster.wad",
                        }
                    ]
                }
                    
            ],
        }
    
    def GetAllModpacks(self)->list[Modpack]:
        modpacks:list = self.data["Modpacks"]
        formatted_return:list[Modpack] = []
        for v in modpacks:
            currentModPack:Modpack = Modpack(v["name"], v["description"])
            
            for m in v["modlist"]:
                currMod:Mod = Mod(m["file_path"], m["name"])
                currentModPack.AddMod(currMod)
            
            formatted_return.append(currentModPack)
        return formatted_return
    
    def GetMods(self, modpackID:int)->list[Mod]:
        modlist = self.data["Modpacks"][modpackID]["modlist"]
        mods:list[Modpack] = []
        for m in modlist:
            mod = Mod(m["file_path"], m["name"])
            mods.append(mod)
        
        return mods
    
    def AddModpack(self,modpack:Modpack):
        
        
        modpack_dict = {
            "name": modpack.name,
            "description":modpack.description,
            "modlist":list(map(modpack.modlist, self.__convert_modClassInstance_to_dict))
        }
        
        self.data["Modpacks"].append(modpack_dict)
    
    def RemoveModpack(self, modpackId:int):
        self.data["Modpacks"].pop(modpackId)
        
    def AddMod(self, modpackID:int, mod:Mod):
        mod_dict = self.__convert_modClassInstance_to_dict(mod)
        self.data["Modpacks"][modpackID]["modlist"].append(mod_dict)
        
    def RemoveMod(self, modpackID:int, modID:int):
        self.data["Modpacks"][modpackID]["modlist"].pop(modID)
        
    def EditMod(self, modpackID: int, modID: int, editedMod: Mod):
        return super().EditMod(modpackID, modID, editedMod)
    
    def EditModpack(self, modpackID: int, editedModpack: Modpack):
        return super().EditModpack(modpackID, editedModpack)    
    
        
    def __convert_modClassInstance_to_dict(mod:Mod):
        mod_dict = {
            "name":mod.name,
            "file_path":mod.file_path
        }
        return mod_dict