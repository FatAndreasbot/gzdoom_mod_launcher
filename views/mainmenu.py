import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw
from controllers.MainMenuController import MainMenuController
from views.addModWindow import AddModWindowDialiog

class MainMenu(Gtk.ApplicationWindow):

    def __init__(self, app, controller:MainMenuController):

        super(MainMenu, self).__init__(application=app)
        self.controller = controller
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
        
        removeMod_button.set_margin_end(4)
        removeMod_button.set_margin_start(4)
        removeMod_button.set_margin_bottom(4)
        removeMod_button.set_margin_top(4)
        removeModpack_button.set_margin_end(4)
        removeModpack_button.set_margin_start(8)
        removeModpack_button.set_margin_bottom(4)
        removeModpack_button.set_margin_top(4)
        
        addMod_button.set_margin_end(8)
        addMod_button.set_margin_start(4)
        addMod_button.set_margin_bottom(4)
        addMod_button.set_margin_top(4)
        addModpack_button.set_margin_end(4)
        addModpack_button.set_margin_start(4)
        addModpack_button.set_margin_bottom(4)
        addModpack_button.set_margin_top(4)
        
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
        
        modpack_renderer = Gtk.CellRendererText() 
        modpack_column = Gtk.TreeViewColumn("Name", modpack_renderer, text=0)
        mod_renderer = Gtk.CellRendererText() 
        mod_column = Gtk.TreeViewColumn("Name", mod_renderer, text=0)
        self.modpackList_listview.append_column(modpack_column)
        self.modList_listview.append_column(mod_column)
        
        modpacklist_selection = self.modpackList_listview.get_selection()
        modpacklist_selection.connect("changed", self.update_modlist)
        
        #   play button
        play_button.set_label("Play")
        play_button.connect("clicked", self.OnClick_play_button)
        play_button.set_halign(Gtk.Align.END)
        play_button.set_margin_end(8)
        play_button.set_margin_bottom(8)
        
        
                
        # putting elements in the UI
                
        #   labels
        label_box = Gtk.Box()
        label_box.append(modpackList_label)
        label_box.append(modList_label)
        label_box.set_homogeneous(True)
        
        #   listviews
        modlistviews_box = Gtk.Box()
        modlistviews_box.set_spacing(8)
        modlistviews_box.set_margin_start(8)
        modlistviews_box.set_margin_end(8)
        
        modpacklist_scrollwindow = Gtk.ScrolledWindow()
        modpacklist_scrollwindow.set_vexpand(True)
        modpacklist_scrollwindow.set_child(self.modpackList_listview)
        
        modlist_scrollwindow = Gtk.ScrolledWindow()
        modlist_scrollwindow.set_vexpand(True)
        modlist_scrollwindow.set_child(self.modList_listview)
        
        
        modlistviews_box.append(modpacklist_scrollwindow)
        modlistviews_box.append(modlist_scrollwindow)
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
        self.main_box.append(play_button)
        
        self.set_child(self.main_box)
        
    
    
    def update_modpacklist(self):
        self.modpacklist_store.clear()
        modpacks = self.controller.GetAllModpacks()
        for i, v in enumerate(modpacks):
            self.modpacklist_store.append([v, i])
            
        self.modlist_store.clear()

    
    def update_modlist(self, selection:Gtk.TreeSelection=None):
        if selection is None:
            selection = self.modpackList_listview.get_selection()
        
        model, treeiter = selection.get_selected()
        self.modlist_store.clear()
        
        if treeiter is not None:
            modpackID = model[treeiter][1]
            mods = self.controller.GetModlist(modpackID)
            for i, v in enumerate(mods):
                self.modlist_store.append([v, i])
            
    def OnClick_removeMod_button(self, button):
        model, treeiter = self.modpackList_listview.get_selection().get_selected()
        if treeiter is None:
            return
        modpackID = model[treeiter][1]
        
        model, treeiter = self.modList_listview.get_selection().get_selected()
        if treeiter is None:
            return
        modID = model[treeiter][1]
        self.controller.RemoveMod(modpackID, modID)
            
        self.update_modlist()
    
    # TODO
    # this
    def OnClick_addModPack_button(self, button):
        # self.controller.AddMod(self)
        print("not implemented")
    
    
    def OnClick_removeModPack_button(self, button):
        model, treeiter = self.modpackList_listview.get_selection().get_selected()
        if treeiter is None:
            return
        modpackID = model[treeiter][1]
        
        self.controller.DeleteModPack(modpackID)
        self.update_modpacklist()
    
    def OnClick_addMod_button(self, button):
        # self.controller.CreateModPack()
        # self.update_modpacklist()
        win = AddModWindowDialiog(self.get_application(), self.controller)
        win.show()
        
    
    
    def OnClick_play_button(self, button):
        model, treeiter = self.modpackList_listview.get_selection().get_selected()
        if treeiter is None:
            return
        modpackID = model[treeiter][1]
        self.controller.Play(modpackID)
    
        

    