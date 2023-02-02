import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import json
import locale
import utils

class Handler:
    timeF = 0
    costF = 0.00
    t_index = '0'
    pwrs = {'0': 0, '1': 0, '2': 0}
    iron = utils.iron(0)
    TV = utils.TV(0)
    washer = utils.washer(0)
    things = {'0': iron, '1': TV, '2': washer}

    def __init__(self):
        try:
            with open('settings.json') as f:
                self.pwrs = json.load(f)
                self.iron.pwr = self.pwrs['0']
                self.TV.pwr = self.pwrs['1']
                self.washer.pwr = self.pwrs['2']
        except:
            self.iron.pwr = self.pwrs['0']
            self.TV.pwr = self.pwrs['1']
            self.washer.pwr = self.self.pwrs['2']
            with open('settings.json', 'w') as settings:
                settings.write(json.dumps(self.pwrs))
                settings.close()
        
    def on_main_window_destroy(self, *args):
         Gtk.main_quit()


    def time_box_changed_cb(self, object):
        buffer = object.get_text()
        try:
            self.timeF = int(buffer)
            #print(self.timeF)
        except:
            pass
        resF = builder.get_object('result_filed')
        resF.set_text(self.things[self.t_index].calculate_to_text(self.timeF, self.costF))

    def cost_box_changed_cb(self, object):
        buffer = object.get_text()
        try:
            self.costF = locale.atof(buffer)
            #print(self.costF)
        except:
            pass
        resF = builder.get_object('result_filed')
        resF.set_text(self.things[self.t_index].calculate_to_text(self.timeF, self.costF))

    def chooser_changed_cb(self, object):
        tree_iter = object.get_active_iter()
        if tree_iter is not None:
            model = object.get_model()
            self.name = model[tree_iter][0]
            self.t_index = str(model[tree_iter][1])
        #print(self.name, ':', self.t_index)
        resF = builder.get_object('result_filed')
        resF.set_text(self.things[self.t_index].calculate_to_text(self.timeF, self.costF))
    
    def settings_btn_clicked_cb(self, object):
            self.dialog = builder.get_object("pwr_dialog")
            self.dialog.show()

    def iron_pwr_changed_cb(self, object):
        buffer = object.get_text()
        try:
            self.pwrs['0'] = locale.atof(buffer)
            #print(self.iron_pwr)
        except:
            pass

    def tv_pwr_changed_cb(self, object):
        buffer = object.get_text()
        try:
            self.pwrs['1'] = locale.atof(buffer)
            #print(self.tv_pwr)
        except:
            pass
    
    def washer_pwr_changed_cb(self, object):
        buffer = object.get_text()
        try:
            self.pwrs['2'] = locale.atof(buffer)
            #print(self.washer_pwr)
        except:
            pass

    def docx_btn_clicked_cb(self, object):
        #print(self.timeF, self.costF, self.pwrs)
        utils.docx_saver.save_to_docx(self.things[self.t_index].calculate_to_text(self.timeF, self.costF))

    def xlsx_btn_clicked_cb(self, object):
        utils.xlsx_saver.save_to_xlsx(self.t_index, self.things[self.t_index].calculate(self.timeF, self.costF))
    
    def cancel_btn_clicked_cb(self, object):
        self.dialog.hide()
        return True
    
    def save_pwr_btn_clicked_cb(self, object):
        # self.iron.pwr = self.pwrs['0']
        # self.TV.pwr = self.pwrs['1']
        # self.washer.pwr = self.self.pwrs['2']
        with open('settings.json', 'w') as settings:
            settings.write(json.dumps(self.pwrs))
            settings.close()
        self.dialog.hide()
        return True

    
    


    



locale.atof('123,456')        
gladefile = "interface.glade"
builder = Gtk.Builder()
builder.add_from_file(gladefile)
builder.connect_signals(Handler())

window = builder.get_object("main_window")
window.show_all()
Gtk.main()
