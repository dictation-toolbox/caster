from Tkinter import Label, Entry, StringVar
import os
import sys
from threading import Timer
import tkFileDialog




if __name__ == "__main__":
#     BASE_PATH = sys.argv[0].split("MacroSystem")[0] + "MacroSystem"
    BASE_PATH = r"C:/NatLink/NatLink/MacroSystem"
    if BASE_PATH not in sys.path:
        sys.path.append(BASE_PATH)
        from lib import  settings
        from asynch.hmc.homunculus import Homunculus
else:
    from lib import  settings
    from asynch.hmc.homunculus import Homunculus


class Homunculus_Directory(Homunculus):
    
    def __init__(self, params):
        Homunculus.__init__(self, params[0])
        self.title(settings.HOMUNCULUS_VERSION + settings.HMC_TITLE_DIRECTORY)
        
        self.geometry("640x50+" + str(int(self.winfo_screenwidth() / 2 - 320)) + "+" + str(int(self.winfo_screenheight() / 2 - 25)))
        Label(self, text="Enter directory or say 'browse'", name="pathlabel").pack()
        self.content = StringVar()
        self.word_box = Entry(self, name="word_box", width=640, textvariable=self.content)
        self.word_box.pack()
        
    
    def xmlrpc_get_message(self):
        if self.completed:
            response = {"mode": "ask_dir"}
            response["path"] = self.word_box.get()
            
            Timer(1, self.xmlrpc_kill).start()
            self.after(10, self.withdraw)
            return response
        else:
            return None

    
    def xmlrpc_do_action(self, action, details=None):
        if action == "ask":
            dir_opt = {}
            dir_opt['initialdir'] = os.environ["HOME"] + '\\'
            dir_opt['mustexist'] = False
            dir_opt['parent'] = self
            dir_opt['title'] = 'Please select directory'
            result = tkFileDialog.askdirectory(**self.dir_opt)
            self.content.set(result)


