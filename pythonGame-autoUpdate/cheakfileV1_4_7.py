class cheakFile:
    from_file_path = None
    correspond_file_path = None
    from_f = ""
    correspond_f = ""
    mode = ""
    from_file_list = []
    file_list = []
    from_dir_list = []
    dir_list = []
    report = []
    def find_dir(self,from_file_path,correspond_file_path):
        """
        copy from "https://yanwei-liu.medium.com/python-os%E6%A8%A1%E7%B5%84%E4%BD%BF%E7%94%A8%E7%AD%86%E8%A8%98-90c652e917c6"
        & https://blog.gtwang.org/programming/python-threading-multithreaded-programming-tutorial/
        """
        import os
        import threading
        import time
        
        #def add_FFL(self,from_file_path):
        # 函數功能: 遞迴顯示指定路徑下的所有檔案及資料夾名稱
        for fd in os.listdir(from_file_path):
            #if fd is "":
            #   continue
            from_full_path = os.path.join(from_file_path,fd)
            if os.path.isdir(from_full_path):
                print('資料夾:',from_full_path)
                #self.find_dir(from_full_path,correspond_file_path)
                self.from_dir_list.append(from_full_path)
            else:
                print('檔案:',from_full_path)

                self.from_file_list.append(from_full_path)
        print("=-" * 20)
        """
        if from_file_path is str:
            add_FFL(from_file_path)
        if from_file_path is list:
            for ff in correspond_file_path:
                add_FFL(ff)
                """
        #def add_CFL(self,correspond_file_path):
        for fd in os.listdir(correspond_file_path):
            full_path=os.path.join(correspond_file_path,fd)
            if os.path.isdir(full_path):
                print('資料夾:',full_path)
                #self.find_dir(full_path,correspond_file_path)\
                self.dir_list.append(full_path)
            else:
                print('檔案:',full_path)

                self.file_list.append(full_path)
        """
        if correspond_file_path is str:
            add_CFL(correspond_file_path)
        elif correspond_file_path is list:
            for cf in correspond_file_path:
                add_CFl(cf)
                """
        report = self.report
        for FFL in self.from_file_list:
            CFL = ""
            for FL in self.file_list:
                CFL = FL
                #print(FFL,"\n")
                #print(CFL)
                
                r = self.setup(str(FFL),str(CFL))
                #print("r=",r)
                cf = False
                #if not r == None:
                cf = self.cheakFile()
                #print(FFL+" = "+CFL+"\t"+str(cf))
                report.append(FFL+" = "+CFL+"\t"+str(cf)+",\n")

        #"""
        print(self.from_dir_list,"\t",self.dir_list)
        from_dirList = ""
        dirList = ""
        if self.from_dir_list == []:
            from_dirList = from_file_path
        if self.dir_list == []:
            dirList = correspond_file_path
        if not self.from_dir_list == []:
            for from_dirList in self.from_dir_list:
                #from_dirList = from_dir_list
                if not self.dir_list == []:
                    for dirList in self.dir_list:
                        #dir_list = dir_list
                        print(from_dirList,dirList,"+"*10)
                        #"""
                        time.sleep(0.5)
                        t2 = threading.Thread(target = self.find_dir(from_dirList,dirList))
                        rlock2 = t2.RLock()
                        semaphore2 = t2.Semaphore(1)
                        rlock2.acquire()
                        semaphore2.acquire()
                        # 執行該子執行緒
                        t2.start()
            #"""
        elif not self.dir_list == []:
            print("self.from_dir_list is ",self.from_dir_list)
        else:
            print("self.from_dir_list&self.dir_list is ",self.from_dir_list,self.from_dir_list)
            return report
        print(from_dirList,dirList)
        if from_dirList == "" or dirList == "":
            #print(from_dirList,",",dirList,self.report)
            return report
        #"""
        time.sleep(0.5)
        t1 = threading.Thread(target = self.find_dir(from_dirList,dirList))
        rlock1 = t1.RLock()
        semaphore1 = t1.Semaphore(1)
        rlock1.acquire()
        semaphore1.acquire()
        # 執行該子執行緒
        t1.start()            
        #       """
        
        #t2 = threading.Thread(target = self.find_dir(from_dir_list,dir_list))
        """
                # 主執行緒繼續執行自己的工作
                for i in range(3):
                  print("Main thread:", i)
                  time.sleep(1)
                """
                
                
        #"""
        
                
        # 等待 t1 這個子執行緒結束
        t1.join()
        rlock1.release()
        semaphore1.release()
        # 等待 t2 這個子執行緒結束
        #"""
        t2.join()
        rlock2.release()
        semaphore2.release()
        #"""
        #"""
        
        self.report = []
        self.from_file_list = []
        self.file_list = []
        return report
    def setup(self,from_file_path,correspond_file_path):
        import os
        if not os.path.isdir(from_file_path) and not os.path.isdir(correspond_file_path):
                    
            if from_file_path is str or not from_file_path == "":
                with open(from_file_path,"rb") as Ff:
                    self.from_f = Ff.read()
            else:
                return None
            if correspond_file_path is str or not from_file_path == "":
                with open(correspond_file_path,"rb") as Cf:
                    self.correspond_f = Cf.read()
            else:
                return None
        else:
            return None
    def __init__(self,from_file_path,correspond_file_path,mode = "file"):
        """
        mode => "file" & "path" .
        return => "file" mode: string, "path" mode: list .
        
        """
        self.from_file_path,self.correspond_file_path = from_file_path,correspond_file_path
        self.mode = mode
    def main(self):
        """
        mode => "file" & "path" .
        return => "file" mode: string, "path" mode: list .
        
        """
        from_file_path = self.from_file_path
        correspond_file_path = self.correspond_file_path
        mode = self.mode
        if str(mode) == "file":
            r = self.setup(from_file_path,correspond_file_path)
            if not r == None:
               r = cheakFile(self)
               return r
        elif str(mode) == "path":
            r = self.find_dir(from_file_path,correspond_file_path)
            
            report = ""
            for rpt in r:
                report += rpt +",\n"
            
            return r, report
    def cheakFile(self):
        if self.from_f == self.correspond_f:
            #self.from_f = ""
            #self.correspond_f = ""
            return True
        else:
            #self.from_f = ""
            #self.correspond_f = ""
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
    arg = """\
    game_socket-client_2P-GUIv2.py,
    game_socket-server_2P-GUIv2.py,
    view.py

    """
    
    def __init__(self,file_source = "temp/update-data-main/pythonGame-autoUpdate/",file_destination = "./"):
        self.file_source = file_source
        self.file_destination = file_destination
    def replace_file(self,args = arg):
        pram = args
        
        
        
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
class packageFile(cheakFile):
    import os
    import threading
    import time
    
    file_source = ""
    file_destination = ""
    from_file_path = None
    correspond_file_path = None
    from_f = ""
    correspond_f = ""
    mode = ""
    from_file_list = []
    file_list = []
    from_dir_list = []
    dir_list = []
    report = []
    def find_dir(self,from_file_path,correspond_file_path):
        """
        copy from "https://yanwei-liu.medium.com/python-os%E6%A8%A1%E7%B5%84%E4%BD%BF%E7%94%A8%E7%AD%86%E8%A8%98-90c652e917c6"
        & https://blog.gtwang.org/programming/python-threading-multithreaded-programming-tutorial/
        """
        import os
        import threading
        import time
        
        #def add_FFL(self,from_file_path):
        # 函數功能: 遞迴顯示指定路徑下的所有檔案及資料夾名稱
        for fd in os.listdir(from_file_path):
            #if fd is "":
            #   continue
            from_full_path = os.path.join(from_file_path,fd)
            if os.path.isdir(from_full_path):
                print('資料夾:',from_full_path)
                #self.find_dir(from_full_path,correspond_file_path)
                self.from_dir_list.append(from_full_path)
            else:
                print('檔案:',from_full_path)

                self.from_file_list.append(from_full_path)
        print("=-" * 20)
        """
        if from_file_path is str:
            add_FFL(from_file_path)
        if from_file_path is list:
            for ff in correspond_file_path:
                add_FFL(ff)
                """
        '''
        #def add_CFL(self,correspond_file_path):
        for fd in os.listdir(correspond_file_path):
            full_path=os.path.join(correspond_file_path,fd)
            if os.path.isdir(full_path):
                print('資料夾:',full_path)
                #self.find_dir(full_path,correspond_file_path)\
                self.dir_list.append(full_path)
            else:
                print('檔案:',full_path)

                self.file_list.append(full_path)
        """
        if correspond_file_path is str:
            add_CFL(correspond_file_path)
        elif correspond_file_path is list:
            for cf in correspond_file_path:
                add_CFl(cf)
                """
        '''
        report = self.report
        for FFL in self.from_file_list:
            '''
            CFL = ""
            for FL in self.file_list:
                CFL = FL
                #print(FFL,"\n")
                #print(CFL)
                
                r = self.setup(str(FFL),str(CFL))
                #print("r=",r)
                cf = False
                #if not r == None:
                cf = self.package()
                #print(FFL+" = "+CFL+"\t"+str(cf))
                report.append(FFL+" = "+CFL+"\t"+str(cf)+",\n")
            '''
            with open(version,"r") as v:
                v = v.read()
                if ".py" in FFL:
                    Ff = FFL
                    Ff.split(".").pop()
                    self.package(str(Ff),"unicorn.ico",v)
            report.append(FFL)
        #"""
        print(self.from_dir_list,"\t",self.dir_list)
        from_dirList = ""
        dirList = ""
        if self.from_dir_list == []:
            from_dirList = from_file_path
        
        if self.dir_list == []:
            dirList = correspond_file_path
        
        if not self.from_dir_list == []:
            for from_dirList in self.from_dir_list:
                #from_dirList = from_dir_list
                '''
                if not self.dir_list == []:
                    for dirList in self.dir_list:
                        #dir_list = dir_list
                        print(from_dirList,dirList,"+"*10)
                        '''
                        #"""
                time.sleep(0.5)
                t2 = threading.Thread(target = self.find_dir(from_dirList,dirList))
                rlock2 = t2.RLock()
                semaphore2 = t2.Semaphore(1)
                rlock2.acquire()
                semaphore2.acquire()
                # 執行該子執行緒
                t2.start()
            #"""
            '''
        elif not self.dir_list == []:
            print("self.from_dir_list is ",self.from_dir_list)
            '''
        else:
            #print("self.from_dir_list&self.dir_list is ",self.from_dir_list,self.from_dir_list)
            return report
        print(from_dirList,dirList)
        if from_dirList == "" or dirList == "":
            #print(from_dirList,",",dirList,self.report)
            return report
        #"""
        time.sleep(0.5)
        t1 = threading.Thread(target = self.find_dir(from_dirList,dirList))
        rlock1 = t1.RLock()
        semaphore1 = t1.Semaphore(1)
        rlock1.acquire()
        semaphore1.acquire()
        # 執行該子執行緒
        t1.start()            
        #       """
        
        #t2 = threading.Thread(target = self.find_dir(from_dir_list,dir_list))
        """
                # 主執行緒繼續執行自己的工作
                for i in range(3):
                  print("Main thread:", i)
                  time.sleep(1)
                """
                
                
        #"""
        
                
        # 等待 t1 這個子執行緒結束
        t1.join()
        rlock1.release()
        semaphore1.release()
        # 等待 t2 這個子執行緒結束
        #"""
        t2.join()
        rlock2.release()
        semaphore2.release()
        #"""
        #"""
        
        self.report = []
        self.from_file_list = []
        self.file_list = []
        return report
    
    def __init__(self,file_source = "temp/update-data-main/pythonGame-autoUpdate/",file_destination = "./"):
        self.file_source = file_source
        self.file_destination = file_destination
        
    def package(self,fileName,icon = "unicorn",version = "0.0.0"):
        args = '''\
        pyinstaller --noconfirm --onefile --windowed --icon "%s" --debug "all" --disable-windowed-traceback --osx-bundle-identifier "%s" --target-architecture "x86_64,arm64,universal2"  "%s"
        ''',(icon,version,self.file_source+fileName+".py")
        
        os.system("pyinstaller(2.15.0).exe " + args)
        replaceFile(file_source,file_destination).replace_file(fileName+".exe")
    def main(self):
        find_dir(self.file_source,self.file_destination)

class cleanFile:
    import os
    import threading
    import time
        
    def __init__(self,file_source = "temp/update-data-main/pythonGame-autoUpdate/"):
        return os.remove(file_source)