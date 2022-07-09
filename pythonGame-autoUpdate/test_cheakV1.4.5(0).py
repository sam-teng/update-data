from cheakfileV1_4_5 import cheakFile
path = input("file from_path")
path1 =input("file correspond_path")
report = cheakFile(path,path1,mode = "path")
#r1,r2 = report.main()
r = str(report)
print("path:",r)
with open("test cheak file log.csv","w+") as f:
    f.write(r)
    f.close()