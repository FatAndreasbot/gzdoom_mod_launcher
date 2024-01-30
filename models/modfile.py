
# TODO
# implement ID generation
class Mod:
    def __init__(self, path:str, name:str):
        self.file_path = path
        self.name = name
        self.id = 0
    
    def __str__(self):
        return self.name
    
    def to_dict(self) -> dict:
        mod_dict = {
            "name":self.name,
            "file_path":mod.file_path
        }
        return mod_dict
        