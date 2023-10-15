import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk


class AppWindow(Gtk.ApplicationWindow):

    def __init__(self, app):

        super(AppWindow, self).__init__(application=app)

        self.init_ui()

    def init_ui(self):

        self.set_title('Check button')

        box = Gtk.Box.new(Gtk.Orientation.VERTICAL, 0)
        box.set_margin_start(5)
        box.set_margin_top(5)

        cbtn = Gtk.CheckButton.new_with_label('Show title')
        cbtn.set_active(True)
        cbtn.connect('toggled', self.on_toggle)

        box.append(cbtn)

        self.set_child(box)
        self.set_default_size(450, 350)

    def on_toggle(self, wid):

        if wid.get_active():
            self.set_title('CheckButton')
        else:
            self.set_title('')


def on_activate(app):

    win = AppWindow(app)
    win.present()


app = Gtk.Application(application_id='com.zetcode.CheckButton')
app.connect('activate', on_activate)
app.run(None)