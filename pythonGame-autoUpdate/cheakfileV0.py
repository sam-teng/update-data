class cheakFile:
    from_file_path = None
    correspond_file_path = None
    from_f = ""
    correspond_f = ""
    def setup(self,from_file_path,correspond_file_path):
        if from_file_path is str:
            with open(from_file_path,"rb") as Ff:
                self.from_f = Ff.read()
        else:
            return None
        if correspond_file_path is str:
            with open(correspond_file_path,"rb") as Cf:
                self.correspond_f = Cf.read()
        else:
            return None
    def __init__(self):
        """
        """
        self.setup()
    def cheakFile(self):
        if self.from_f == self.correspond_f:
            return True
        else:
            return False
    def repeat(self,count,from_file_path,correspond_file_path):
        if not i == 0 or not int:
            pass
        else:
            if from_file_path is list and correspond_file_path is list:
                for i in range(count):
                    for Cf in from_file_path:
                        for Ff in correspond_file_path:
                            setup(self,from_file_path,correspond_file_path)
                            cheakFile(self)
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox
class replaceFile:
    count = 1
    
    def __init__(self,file_source = "temp/update-data-main/pythonGame-autoUpdate/",file_destination = "./"):
        self.file_source = file_source
        self.file_destination = file_destination
    def replace_file(self):
        pram = """
        game_socket-client_2P-GUIv2.py,
        game_socket-server_2P-GUIv2.py,
        view.py

        """
        
        
        i = 1
        for arg in pram.split(","):
            if not cheakFile(arg,self.file_source+arg):
                if i == len(pram.split(",")):
                    tkinter.messagebox.showinfo("showinfo", "更新中請耐心等候")
                #更新目前檔案
                
                 
                get_files = os.listdir(self.file_source)
                 
                for g in get_files:
                    os.replace(self.file_source + g, self.file_destination + g)
                    print(g)
                """    
                count += 1
                return count
                """
            else:
                if i == len(pram.split(",")):
                    tkinter.messagebox.showinfo("showinfo", "完成")
                    
                    
            i += 1
