class cheakFile:
    from_file_path = None
    correspond_file_path = None
    cheak = None
    from_f = ""
    correspond_f = ""
    mode = ""
    from_file_list = []
    file_list = []
    from_dir_list = []
    dir_list = []
    report = []
    t, rlock, semaphore = [], [], []
    def find_dir(self,from_file_path,correspond_file_path,tc = 0,ti = 0):
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
            from_full_path = os.path.join(from_file_path,fd).replace("\\","/")
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
            full_path = os.path.join(correspond_file_path,fd).replace("\\","/")
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
                
                thr = threading.Thread(target = self._setup,
                                args = [
                                    str(FFL),
                                    str(CFL)
                                ]
                            )
                Rl = threading.RLock()
                Sem = threading.Semaphore(3)
                thr.start()
                Rl.acquire()
                Sem.acquire()
                #del r
                #print("r=",r)
                #cf = False
                #if not r == None:
                cf = self.cheak#self.cheakFile()
                #print(FFL+" = "+CFL+"\t"+str(cf))
                report.append(FFL+" = "+CFL+"\t"+str(cf)+",\n")
                thr.join()
                Rl.release()
                Sem.release()
        #"""
        print(self.from_dir_list,"\t",self.dir_list)
        from_dirList = ""
        dirList = ""
        if self.from_dir_list == []:
            from_dirList = from_file_path
            
        if self.dir_list == []:
            dirList = correspond_file_path
        
        #t2, rlock2, semaphore2 = None, None, None
        #t, rlock, semaphore = self.t, self.rlock, self.semaphore
        c, i = 0, 0    
        th, rl, sem = 0, 0, 0
        try:
            print(self.from_dir_list[tc])
        except:
            pass
        try:
            print(self.dir_list[ti])
        except:
            pass
        
        state = False
        if not self.from_dir_list == []:
            for from_dirList in self.from_dir_list:
                #from_dirList = from_dir_list
                if c < tc:
                    continue
                if not self.dir_list == []:
                    state = True
                    for dirList in self.dir_list:
                        #dir_list = dir_list
                        if i < ti:
                            continue
                        print(from_dirList,dirList,"+"*10)
                        time.sleep(0.005)
                        self.t.append(
                            threading.Thread(target = self.find_dir,
                                args = [
                                    from_dirList,
                                    dirList,
                                    len(self.from_dir_list),
                                    len(self.dir_list)
                                ]
                            )
                        )
                        self.rlock.append(threading.RLock())
                        self.semaphore.append(threading.Semaphore(2))
                        th, rl, sem = len(self.t)-1, len(self.rlock)-1, len(self.semaphore)-1
                        self.rlock[rl].acquire()
                        self.semaphore[sem].acquire()
                        #self.t, self.rlock, self.semaphore = t, rlock, semaphore
                        # 執行該子執行緒
                        self.t[th].start()
                        
                        """
                        time.sleep(0.005)
                        t2 = threading.Thread(target = self.find_dir(from_dirList,dirList))
                        rlock2 = threading.RLock()
                        semaphore2 = threading.Semaphore(2)
                        rlock2.acquire()
                        semaphore2.acquire()
                        # 執行該子執行緒
                        t2.start()
                        """
                        
                        self.dir_list.remove(dirList)
                        
                        i += 1
                
                self.from_dir_list.remove(from_dirList)
                     
                
                c += 1
        elif not self.dir_list == []:
            print("self.from_dir_list is ",self.from_dir_list)
        else:
            print("self.from_dir_list&self.dir_list is ",self.from_dir_list,self.from_dir_list)
            return report
        print(from_dirList,dirList)
        if from_dirList == "" or dirList == "":
            #print(from_dirList,",",dirList,self.report)
            return report
        """
        time.sleep(0.5)
        t1 = threading.Thread(target = self.find_dir(from_dirList,dirList))
        rlock1 = threading.RLock()
        semaphore1 = threading.Semaphore(1)
        rlock1.acquire()
        semaphore1.acquire()
        # 執行該子執行緒
        t1.start()            
               """
        
        #t2 = threading.Thread(target = self.find_dir(from_dir_list,dir_list))
        """
                # 主執行緒繼續執行自己的工作
                for i in range(3):
                  print("Main thread:", i)
                  time.sleep(1)
                """
                
                
        """
        
                
        # 等待 t1 這個子執行緒結束
        t1.join()
        rlock1.release()
        semaphore1.release()
        # 等待 t2 這個子執行緒結束
        """
        """
        t2.join()
        rlock2.release()
        semaphore2.release()
        
        """
        if state:
            self.t[th].join()
            self.rlock[rl].release()
            self.semaphore[sem].release()
        
        self.report = []
        self.from_file_list = []
        self.file_list = []
        return report
    
    def _setup(self,from_file_path : str,correspond_file_path : str) -> None:
        import os
        #import time
        
        if not os.path.isdir(from_file_path) and not os.path.isdir(correspond_file_path):
                    
            if not from_file_path == "" and not correspond_file_path == "":

                file_size = os.path.getsize(from_file_path) 
                
                file_size1 = os.path.getsize(correspond_file_path) 
                
                
                if not file_size == file_size1:
                    return False
                elif file_size + file_size1 == 0:
                    return None
                #print('File Size(1):', file_size, 'bytes.')
                #print('File Size(2):', file_size1, 'bytes.')
                
                #time.sleep(0.0001)
                
                with open(from_file_path,"rb") as Ff:
                    #self.from_f = Ff.read()
                    
                    
                    
                    file_start_size = (file_size//100)*100
                    #file_end_size = file_size-file_start_size
                
                    with open(correspond_file_path,"rb") as Cf:
                        #self.correspond_f = Cf.read()
                        
                        
                        
                        file_start_size1 = (file_size1//100)*100
                        #file_end_size1 = file_size1-file_start_size1
                        
                        i, i1 = 0, 0
                        
                        for i in range(0,file_start_size,100):
                            self.from_f = Ff.read()[i+0:i+100]
                            for i1 in range(0,file_start_size1,100):
                                
                                self.correspond_f = Cf.read()[i1+0:i1+100]
                                #print(self.from_f,self.correspond_f,sep="\t")
                                state = self.cheakFile()
                                if not state:
                                    #del Ff, Cf
                                    return False
                                if not i == i1:
                                    continue
                                #del Ff.read()[i1+0:i1+100], Cf.read()[i1+0:i1+100]
                        #ii, ii1 = i, i1
                        #for i in range(ii,file_size,file_end_size):
                        self.from_f = Ff.read()[i+0:file_size]
                        #    for i1 in range(ii1,file_end_size1):
                        self.correspond_f = Cf.read()[i1+0:file_size1]
                        
                        if not self.cheakFile():
                            #del Ff, Cf
                            return False
                                
            else:
                return None
            
        else:
            return None
        #del Ff, Cf
        return True
        
    def __init__(self,from_file_path : str,correspond_file_path : str,mode = "file"):
        """
        mode => "file" & "path" .
        return => "file" mode: string, "path" mode: list .
        
        """
        self.from_file_path,self.correspond_file_path = from_file_path,correspond_file_path
        self.mode = mode
        
        from_file_path = self.from_file_path
        correspond_file_path = self.correspond_file_path
        mode = self.mode
        if str(mode) == "file":
            r = self._setup(from_file_path,correspond_file_path)
            """
            if not r == None:
               r = cheakFile(self)
                """
            return# r
        elif str(mode) == "path":
            r = self.find_dir(from_file_path,correspond_file_path)
            
            report = ""
            for rpt in r:
                report += rpt +",\n"
            
            return# report
        
    def main(self):
        """
        mode => "file" & "path" .
        return => "file" mode: string, "path" mode: list .
        
        """
        from_file_path = self.from_file_path
        correspond_file_path = self.correspond_file_path
        mode = self.mode
        if str(mode) == "file":
            r = self._setup(from_file_path,correspond_file_path)
            """
            if not r == None:
               r = cheakFile(self)
               """
            return r   
        elif str(mode) == "path":
            r = self.find_dir(from_file_path,correspond_file_path)
            
            report = ""
            for rpt in r:
                report += rpt +",\n"
            
            return r, report
        
    def cheakFile(self):
        if self.from_f == self.correspond_f:
            self.from_f = ""
            self.correspond_f = ""
            self.cheak = True
            return True
        else:
            self.from_f = ""
            self.correspond_f = ""
            self.cheak = False
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

class cleanFile:
    import os
    import threading
    import time
        
    def __init__(self,file_source = "temp/update-data-main/"):
        with open("info", "r") as inf:
            inf = inf.read()
            file_source = file_source+inf+"/"
        return os.remove(file_source)

class replaceFile:
    """
    from tkinter import *
    from tkinter.ttk import *
    """
    import tkinter.messagebox
    import os
    
    count = 1
    arg = """\
    game_socket-client_2P-GUIv2.py,
    game_socket-server_2P-GUIv2.py,
    view.py

    """
    
    def __init__(self,file_source = "temp/update-data-main/",file_destination = "./",show_windows = True):
        """
        show_windows => True & False .
        return => None .
        
        """
        
        self.file_source = file_source
        self.file_destination = file_destination
        self.show_windows = show_windows
        if not file_source == "temp/update-data-main/":
            return
        with open("info", "r") as inf:
            inf = inf.read()
            self.file_source = file_source+inf+"/"
            
    def replace_file(self,args = arg):
        pram = args
        
        import os
        import tkinter.messagebox
        
        i = 1
        for arg in pram.split(","):
            cheak = False
            if self.file_source == "temp/update-data-main/":
                cheak = cheakFile(arg,self.file_source+arg)
            if not cheak:
                if i == len(pram.split(",")):
                    if self.show_windows:
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
                    if self.show_windows:
                        tkinter.messagebox.showinfo("showinfo", "完成")
                    
                    
            i += 1
            
class packageFile:
    import os
    import threading
    import time
    
    version = "0.0.0"
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
    t, rlock, semaphore = [], [], []
    def find_dir(self,from_file_path,correspond_file_path,tc = 0,ti = 0):
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
            from_full_path = os.path.join(from_file_path,fd).replace("\\","/")
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
        """
        for fd in os.listdir(correspond_file_path):
            full_path = os.path.join(correspond_file_path,fd).replace("\\","/")
            if os.path.isdir(full_path):
                print('資料夾:',full_path)
                #self.find_dir(full_path,correspond_file_path)\
                self.dir_list.append(full_path)
            else:
                print('檔案:',full_path)

                self.file_list.append(full_path)
                """
        """
        if correspond_file_path is str:
            add_CFL(correspond_file_path)
        elif correspond_file_path is list:
            for cf in correspond_file_path:
                add_CFl(cf)
                """
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
            try:
                with open("version","r") as v:
                    v = v.read()
                    if ".py" in FFL:
                        Ff = FFL
                        thr = threading.Thread(target = self.package,
                            args = [
                                str(Ff),
                                "unicorn.ico",
                                v
                            ]
                        )
                        Rl = threading.RLock()
                        Sem = threading.Semaphore(3)
                        thr.start()
                        Rl.acquire()
                        Sem.acquire()
                        #Ff.split(".").pop()
                        #self.package(str(Ff),"unicorn.ico",v)
                        #print(Ff,"has been packaged.")
                        thr.join()
                        Rl.release()
                        Sem.release()
            except:
                try:
                    with open(from_file_path+"version","r") as v:
                        v = v.read()
                        if ".py" in FFL:
                            Ff = FFL
                            #Ff.split(".").pop()
                            thr = threading.Thread(target = self.package,
                                args = [
                                    str(Ff),
                                    "unicorn.ico",
                                    v
                                ]
                            )
                            Rl = threading.RLock()
                            Sem = threading.Semaphore(3)
                            thr.start()
                            Rl.acquire()
                            Sem.acquire()
                            #self.package(str(Ff),"unicorn.ico",v)
                            #print(Ff,"has been packaged.")
                            thr.join()
                            Rl.release()
                            Sem.release()
                except:
                    with open("version","w") as v:
                        v = v.write(self.version)
                        if ".py" in FFL:
                            Ff = FFL
                            #Ff.split(".").pop()
                            thr = threading.Thread(target = self.package,
                                args = [
                                    str(Ff),
                                    "unicorn.ico",
                                    v
                                ]
                            )
                            Rl = threading.RLock()
                            Sem = threading.Semaphore(3)
                            thr.start()
                            Rl.acquire()
                            Sem.acquire()
                            #self.package(str(Ff),"unicorn.ico",v)
                            #print(Ff,"has been packaged.")
                            thr.join()
                            Rl.release()
                            Sem.release()
            report.append(FFL)
        if self.show_windows:
            tkinter.messagebox.showinfo("showinfo", "完成")

        #"""
        print(self.from_dir_list,"\t",self.dir_list)
        from_dirList = ""
        dirList = ""
        if self.from_dir_list == []:
            from_dirList = from_file_path
            
        if self.dir_list == []:
            dirList = correspond_file_path
        
        #t2, rlock2, semaphore2 = None, None, None
        #t, rlock, semaphore = self.t, self.rlock, self.semaphore
        c, i = 0, 0    
        th, rl, sem = 0, 0, 0
        
        try:
            print(self.from_dir_list[tc])
        except:
            pass
        try:
            pass#print(self.dir_list[ti])
        except:
            pass
        
        state = False
        if not self.from_dir_list == []:
            state = True
            for from_dirList in self.from_dir_list:
                #from_dirList = from_dir_list
                if c < tc:
                    continue
                """
                if not self.dir_list == []:
                    for dirList in self.dir_list:
                        #dir_list = dir_list
                        if i < ti:
                            continue
                            """
                print(from_dirList,dirList,"+"*10)
                time.sleep(0.005)
                self.t.append(
                    threading.Thread(target = self.find_dir,args = [
                            from_dirList,
                            dirList,
                            len(self.from_dir_list)-1,
                            len(self.dir_list)-1
                        ]
                    )
                )
                self.rlock.append(threading.RLock())
                self.semaphore.append(threading.Semaphore(2))
                th, rl, sem = len(self.t)-1, len(self.rlock)-1, len(self.semaphore)-1
                self.rlock[rl].acquire()
                self.semaphore[sem].acquire()
                #self.t, self.rlock, self.semaphore = t, rlock, semaphore
                # 執行該子執行緒
                self.t[th].start()
                
                """
                        time.sleep(0.005)
                        t2 = threading.Thread(target = self.find_dir(from_dirList,dirList))
                        rlock2 = threading.RLock()
                        semaphore2 = threading.Semaphore(2)
                        rlock2.acquire()
                        semaphore2.acquire()
                        # 執行該子執行緒
                        t2.start()
                        """
                """
                        self.dir_list.remove(dirList)
                        """
                        #i += 1
                
                self.from_dir_list.remove(from_dirList)
                     
                
                c += 1
        elif not self.dir_list == []:
            print("self.from_dir_list is ",self.from_dir_list)
        else:
            print("self.from_dir_list&self.dir_list is ",self.from_dir_list,self.from_dir_list)
            return report
        print(from_dirList,dirList)
        if from_dirList == "" or dirList == "":
            #print(from_dirList,",",dirList,self.report)
            return report
        """
        time.sleep(0.5)
        t1 = threading.Thread(target = self.find_dir(from_dirList,dirList))
        rlock1 = threading.RLock()
        semaphore1 = threading.Semaphore(1)
        rlock1.acquire()
        semaphore1.acquire()
        # 執行該子執行緒
        t1.start()            
               """
        
        #t2 = threading.Thread(target = self.find_dir(from_dir_list,dir_list))
        """
                # 主執行緒繼續執行自己的工作
                for i in range(3):
                  print("Main thread:", i)
                  time.sleep(1)
                """
                
                
        """
        
                
        # 等待 t1 這個子執行緒結束
        t1.join()
        rlock1.release()
        semaphore1.release()
        # 等待 t2 這個子執行緒結束
        """
        """
        t2.join()
        rlock2.release()
        semaphore2.release()
        
        """
        if state:
            self.t[th].join()
            self.rlock[rl].release()
            self.semaphore[sem].release()
        
        self.report = []
        self.from_file_list = []
        self.file_list = []
        return report
    
    def __init__(self,file_source = "temp/update-data-main/",file_destination = "./",version = "0.0.0",mode = "file"):
        """
        mode => "file" & "path" .
        return => None .
        
        """
        
        self.file_source = file_source
        self.file_destination = file_destination
        self.version = version
        if mode == "file":
            self.show_windows = True
        elif mode == "path":
            self.show_windows = False
        
        with open("info", "r") as inf:
            inf = inf.read()
            self.file_source = file_source+inf+"/"
        
    def package(self,fileName,icon = "unicorn.ico",version = "0.0.0"):
        import os
        import time
        
        file_name = fileName.split("/").pop()
        
        
        i = 0
        with open(self.file_source+"config","r") as config:
            config = config.read()
            #print("config:",config)
            for c in config.split(",\n"):
                #print(file_name,type(file_name),c,type(c))
                print("[",file_name,"<=>",c,"]")
                i += 1
                if file_name in c and c in file_name:
                    continue
                i -= 1
        print("i:",i)
        
        if not i == 1:
            return
        
        print(fileName,"has been packaged.")
        
        s = -1
        
        try:
            args = '''\
            --noconfirm --onefile --windowed --icon \"%s\" --debug \"all\" --disable-windowed-traceback --osx-bundle-identifier \"%s\" --target-architecture \"x86_64,arm64,universal2\"  \"%s\"
            '''%(icon,version,os.path.abspath(fileName).replace("\\","/"))
            
            print(args)
            
            s = os.system("pyinstaller.exe " + args)
        except:
            args = '''\
            --noconfirm --onefile --windowed --icon \"%s\" --debug \"all\" --disable-windowed-traceback --osx-bundle-identifier \"%s\" --target-architecture \"x86_64,arm64,universal2\"  \"%s\"
            '''%(icon,version,fileName)
            
            print(args)
            
            s = os.system("pyinstaller.exe " + args)
        print(s)
        if not s:
            start, end = int(time.time()), int(time.time())
            #time.sleep(30)
            while not end-start >= 30:
                end = time.time()
            print(start,end)
            file_name = file_name.split(".",-1)
            file_name.pop()
            file_name = ".".join(file_name)
            print(file_name)
            os.remove(file_name+".spec")
            #cleanFile(file_name+".spec")
            replaceFile("dist/",self.file_destination,self.show_windows).replace_file(file_name+".exe")
    def main(self):
        self.find_dir(self.file_source,self.file_destination)
