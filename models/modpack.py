from models.modfile import Mod

# # TODO
# # implement ID generation
# class Mod:
#     def __init__(self, path:str, name:str):
#         self.file_path = path
#         self.name = name
#         self.id = 0


# TODO
# implement ID generation
class Modpack:
    def __init__(self, name:str, description:str=""):
        self.name = name
        self.description = description
        self.modlist:list[Mod] = []
        self.id = 0
        
    def AddMod(self, mod:Mod):
        self.modlist.append(mod)
    
    def __str__(self):
        return self.name
    
        