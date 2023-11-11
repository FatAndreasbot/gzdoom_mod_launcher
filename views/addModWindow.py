import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw


class AddModWindowDialiog(Gtk.Window):
    def __init__(self, parent):
        super.__init__()
        self.set_title("Add mod")
        
        
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
            
        
        
    def onClick_add_button(self, button):
        print("not implemented")
    
    def onClick_chooseFile_button(self, button):
        print("not implemented")