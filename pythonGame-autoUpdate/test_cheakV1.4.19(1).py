from cheakfileV1_4_19 import cheakFile
path = input("file from_path")
path1 = input("file correspond_path")
p = cheakFile(path,path1,mode = "path")
print("path:",p)
print("path:",str(p))
print("path:",p.main())
