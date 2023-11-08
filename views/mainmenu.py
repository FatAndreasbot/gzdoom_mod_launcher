import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw
from controllers import MainMenuController

class MainMenu(Gtk.ApplicationWindow):

    def __init__(self, app):

        super(MainMenu, self).__init__(application=app)
        self.init_ui()

    def init_ui(self):

        self.set_title('Doom mod manager')
        self.set_default_size(800, 600)
        
        # elements
        self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        modpackListControl_box = Gtk.Box()
        modListControl_box =  Gtk.Box()
        self.modpackList_treeview = Gtk.TreeView()
        self.modList_treeview = Gtk.TreeView()
        play_button = Gtk.Button()
        addModpack_button = Gtk.Button()
        addMod_button = Gtk.Button()
        removeModpack_button = Gtk.Button()
        removeMod_button = Gtk.Button()
        modpackList_label = Gtk.Label()
        modList_label = Gtk.Label()
        
        # set up elements 
        #   buttons
        removeMod_button.set_label("-")
        removeModpack_button.set_label("-")
        addMod_button.set_label("+")
        addModpack_button.set_label("+")
        
        removeMod_button.connect("clicked", self.OnClick_removeMod_button)
        addMod_button.connect("clicked", self.OnClick_addMod_button)
        
        #   labels
        modpackList_label.set_text("Modpacks")
        modList_label.set_text("Mods")
        
        # button boxes
        modpackListControl_box.append(removeModpack_button)
        modpackListControl_box.append(addModpack_button)
        
        modListControl_box.append(removeMod_button)
        modListControl_box.append(addMod_button)
        
        
        # put elements in the UI
        labelbox = Gtk.Box()
        labelbox.append(modpackList_label)
        labelbox.append(modList_label)
        labelbox.set_homogeneous(True)
        
        self.main_box.append(labelbox)
        
        self.set_child(self.main_box)
        
    
    def OnClick_removeMod_button(self, button):
        #Todo pass in modID
        MainMenuController.RemoveMod(0)
    
    def OnClick_addMod_button(self, button):
        MainMenuController.AddMod()

    def OnClick_removeModPack_button(self, button):
        #Todo pass in modpackID
        MainMenuController.DeleteModPack(0)
    
    def OnClick_addModPack_button(self, button):
        MainMenuController.CreateModPack()

    
        

    