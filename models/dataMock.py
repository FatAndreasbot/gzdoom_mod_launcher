from models.modfile import Mod
from models.modpack import Modpack


class dataAcessMock:
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
                }
                    
            ],
        }
    
    def GetAllModpacks(self):
        modpacks:list = self.data["Modpacks"]
        formatted_return = []
        for i, v in enumerate(modpacks):
            formatted_return.append(v["name"])
        return formatted_return
    
    def GetMods(self, modpack_id:int):
        modpack = self.data["Modpacks"][modpack_id]
        return modpack["modlist"]
    
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
        
    def __convert_modClassInstance_to_dict(mod:Mod):
        mod_dict = {
            "name":mod.name,
            "file_path":mod.file_path
        }
        return mod_dict