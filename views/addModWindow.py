import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw
from controllers.MainMenuController import MainMenuController


class AddModWindowDialiog(Gtk.Window):
    def __init__(self, parent_app, controller:MainMenuController):
        super(AddModWindowDialiog, self).__init__(application=parent_app)
        self.set_title("Add mod")
        self.init_ui()
        
        
    def init_ui(self):
        # elements
        #   boxes
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        name_box = Gtk.Box()
        path_box = Gtk.Box()
        
        #   labels
        name_label = Gtk.Label()
        path_label = Gtk.Label()
        
        #   buttons
        add_button = Gtk.Button()
        chooseFile_button = Gtk.Button()
        
        #   text inputs
        nameField_text = Gtk.Text()
        pathField_text = Gtk.Text()
        
        # set up elements
        #   labels
        name_label.set_label("Mod name")
        path_label.set_label("Mod file")
        
        #   buttons
        add_button.connect("clicked", self.onClick_add_button)
        chooseFile_button.connect("clicked", self.onClick_chooseFile_button)
        
        # putting elements into the ui
        name_box.append(name_label)
        name_box.append(nameField_text)
        
        path_box.append(path_label)
        path_box.append(pathField_text)
        path_box.append(chooseFile_button)
        
        main_box.append(name_box)
        main_box.append(path_box)
        main_box.append(add_button)
        
        self.set_child(main_box)
            
        
        
    def onClick_add_button(self, button):
        print("not implemented")
    
    def onClick_chooseFile_button(self, button):
        print("not implemented")