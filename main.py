import gi
gi.require_version('Gtk', '4.0')
# gi.require_version('Adw', '1')
from gi.repository import Gtk
from gi.repository import Adw
from views.mainmenu import MainMenu
from models.dataMock import DataAcessMock
from controllers.MainMenuController import MainMenuController


if __name__ == "__main__":
    app = Gtk.Application(application_id='DoomModManager')
    appController = MainMenuController(DataAcessMock())
    
    def on_activate(app):
        win = MainMenu(app, appController)
        win.present()
    
    app.connect('activate', on_activate)
    app.run(None)
