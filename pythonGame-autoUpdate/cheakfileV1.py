class cheakFile:
    from_file_path = None
    correspond_file_path = None
    from_f = ""
    correspond_f = ""
    from_file_list = []
    file_list = []
    def find_dir(self,from_file_path,correspond_file_path):
        """
        copy from "https://yanwei-liu.medium.com/python-os%E6%A8%A1%E7%B5%84%E4%BD%BF%E7%94%A8%E7%AD%86%E8%A8%98-90c652e917c6"
        """
        import os
        # 函數功能: 遞迴顯示指定路徑下的所有檔案及資料夾名稱
        for fd in os.listdir(from_file_path):
            from_full_path=os.path.join(from_file_path,fd)
            if os.path.isdir(from_full_path):
                #print('資料夾:',from_full_path)
                self.find_dir(from_full_path,correspond_file_path)
            else:
                #print('檔案:',from_full_path)

                self.from_file_list.append(from_full_path)
            for fd in os.listdir(correspond_file_path):
                full_path=os.path.join(correspond_file_path,fd)
                if os.path.isdir(full_path):
                    #print('資料夾:',full_path)
                    self.find_dir(full_path,correspond_file_path)
                else:
                    #print('檔案:',full_path)

                    self.file_list.append(full_path)

        for FFL in self.from_file_list:
            CFL = ""
            for FL in self.file_list:
                CFL = FL
            self.setup(FFL,CFL)
            cheakFile(self)
        self.from_file_list = []
        self.file_list = []
    def setup(self,from_file_path,correspond_file_path):
        if from_file_path is str or from_file_path == "":
            with open(from_file_path,"rb") as Ff:
                self.from_f = Ff.read()
        else:
            return None
        if correspond_file_path is str or correspond_file_path == "":
            with open(correspond_file_path,"rb") as Cf:
                self.correspond_f = Cf.read()
        else:
            return None
    def __init__(self,from_file_path,correspond_file_path,mode = "file"):
        """
        mode => "file" & "path" 
        
        """
        if str(mode) == "file":
            self.setup(from_file_path,correspond_file_path)
            cheakFile(self)
        elif str(mode) == "path":
            self.find_dir(from_file_path,correspond_file_path)
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
