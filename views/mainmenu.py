import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw
from controllers import MainMenuController
from models.modfile import Mod
from models.modpack import Modpack

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
        self.modpackList_listview = Gtk.TreeView()
        self.modList_listview = Gtk.TreeView()
        play_button = Gtk.Button()
        addModpack_button = Gtk.Button()
        addMod_button = Gtk.Button()
        removeModpack_button = Gtk.Button()
        removeMod_button = Gtk.Button()
        modpackList_label = Gtk.Label()
        modList_label = Gtk.Label()
        
        #listview crap
        self.modpacklist_store = Gtk.ListStore(str, int) # name, id
        self.modlist_store = Gtk.ListStore(str, int)     # name, id
        
        
        
        # set up elements 
        #   buttons
        removeMod_button.set_label("-")
        removeModpack_button.set_label("-")
        addMod_button.set_label("+")
        addModpack_button.set_label("+")
        
        removeModpack_button.connect("clicked", self.OnClick_removeModPack_button)
        addModpack_button.connect("clicked", self.OnClick_addModPack_button)
        
        removeMod_button.connect("clicked", self.OnClick_removeMod_button)
        addMod_button.connect("clicked", self.OnClick_addMod_button)
        
        #   labels
        modpackList_label.set_text("Modpacks")
        modList_label.set_text("Mods")
        
        #   modpacklist and modlist
        self.update_modpacklist()
        
        self.modpackList_listview.set_model(self.modpacklist_store)
        self.modList_listview.set_model(self.modlist_store)
        renderer = Gtk.CellRendererText() 
        column = Gtk.TreeViewColumn(title="Name", cell_renderer=renderer)
        self.modpackList_listview.append_column(column)
        
        
        
                
        # putting elements in the UI
                
        #   labels
        label_box = Gtk.Box()
        label_box.append(modpackList_label)
        label_box.append(modList_label)
        label_box.set_homogeneous(True)
        
        #   listviews
        modlistviews_box = Gtk.Box()
        modlistviews_box.append(self.modpackList_listview)
        modlistviews_box.append(self.modList_listview)
        modlistviews_box.set_homogeneous(True)
        
        #   button boxes
        modpackListControl_box.append(removeModpack_button)
        modpackListControl_box.append(addModpack_button)
        modpackListControl_box.set_homogeneous(True)
        
        modListControl_box.append(removeMod_button)
        modListControl_box.append(addMod_button)
        modListControl_box.set_homogeneous(True)
        
        controlbox_box = Gtk.Box()
        controlbox_box.set_homogeneous(True)
        controlbox_box.append(modpackListControl_box)
        controlbox_box.append(modListControl_box)
        
        
        
        #   putting into the main UI box
        self.main_box.append(label_box)
        self.main_box.append(modlistviews_box)
        self.main_box.append(controlbox_box)
        
        self.set_child(self.main_box)
        
    
    
    #TODO
    # write an implemetation 
    # right now it's just a mock
    def update_modpacklist(self):
        self.modpacklist_store.append(["Vanilla Doom", 0])
    
    
    
    #TODO
    # pass in modID
    def OnClick_removeMod_button(self, button):
        MainMenuController.RemoveMod(0)
    
    def OnClick_addMod_button(self, button):
        MainMenuController.AddMod()
    
    #TODO
    # pass in modpackID
    def OnClick_removeModPack_button(self, button):
        
        MainMenuController.DeleteModPack(0)
        self.update_modpacklist()
    
    def OnClick_addModPack_button(self, button):
        MainMenuController.CreateModPack()
        self.update_modpacklist()
        

    
        

    