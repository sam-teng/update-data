class cheakFile:
    from_file_path = None
    correspond_file_path = None
    from_f = ""
    correspond_f = ""
    def __init__(self,from_file_path,correspond_file_path):
        """
        """
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
    def cheakFile(self):
        if self.from_f == self.correspond_f:
            return True
        else:
            return False