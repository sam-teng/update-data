with open("config", "r") as f:
    for fn in f.split(",\n").pop():
        exec(open(fn, "rb"))
    f.close()
