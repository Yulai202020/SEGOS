import sys,karnel
import settings.settdata as sd
import data.datads as dt

def biossafemode():
    try:
        while True:
            print("Safe mode it's bios settings ...")
            asplit = input("IZ > ").lower().split()
            if asplit[1] == "help":
                print("./#SystemRoot#/ this is system root")
            elif asplit[0] == "echo":print(asplit[1])
            elif asplit[0] == "print":print(asplit[1])
    except KeyboardInterrupt as err :
        with open(sd.Logs["perflogsinfopyth"]+"/exit.log","a") as file :
            file.write("Code 200\n\tExiting ...\n")
        print();sys.exit(0)

def ui():
    while True:
        try:
            uiinput = input(f"OS.Users.{dt.user}: {karnel.cwd}$ ")
            uiinputsmale = uiinput.lower().split();uiinputbig = uiinput.split()
            karnel.karnel(uiinputsmale,uiinputbig)
        except KeyboardInterrupt as err :
            with open(sd.Logs["perflogsinfopyth"]+"/exit.log","a") as file :
                file.write("Code 200\n\tExiting ...\n")
            print();sys.exit(0)
        except FileNotFoundError as err :
            with open(sd.Logs["perflogserropyth"]+"/notfound.log","a") as file :
                file.write("Error 404\n\tError  : File not found !!!\n")

def run():
    print("Run in -sm it's standart mode ...")
    print("Run in -ssm it's standart safe mode ...")
    if sys.argv[1] == "-sm" : dt.pwdbox.pwd();dt.init();ui()
    elif sys.argv[1] == "-ssm" : biossafemode()
    else :
        print("1. Safe mode")
        print("2. Normal mode")
        mode = input("->")
        if mode == "1" : biossafemode()
        elif mode == "2" : dt.pwdbox.pwd();dt.init();ui()
        else : print("Unknow , exiting ...");sys.exit()

if __name__ == "__main__" : run()