from cheakfileV1_4_6 import cheakFile
path = input("file from_path")
path1 =input("file correspond_path")
report = cheakFile(path,path1,mode = "path")
r1,r2 = report.main()
print("path:",r1,r2)
with open("test cheak file log.csv","w+") as f:
    f.write(r2)
    f.close()