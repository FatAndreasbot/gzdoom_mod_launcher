import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw
from views.mainmenu import MainMenu





if __name__ == "__main__":
    def on_activate(app):
        win = MainMenu(app)
        win.present()
    
    app = Gtk.Application(application_id='DoomModManager')
    app.connect('activate', on_activate)
    app.run(None)
