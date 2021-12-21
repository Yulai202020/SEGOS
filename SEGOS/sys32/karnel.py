import os
import utilits.osproperties as proj
import settings.settdata as sd
import data.datads as dt

cwd = os.getcwd()+"/"

def karnel(userinput,userinput2):
    try :
        global cwd
        insplit = userinput ; insplitbig = userinput2
        # help
        if insplit[0] == "help" : print(dt.help)
        # cmd
        elif insplit[0] == "cd" :
            if insplit[1] != ".." :
                if os.path.exists(cwd+insplitbig[1]+"/") : cwd += insplit[1]+"/"
            else : cwd = "/".join(cwd.split("/")[:-2])+"/"
        elif insplit[0] == "echo" : print(insplit[1])
        elif insplit[0] == "print" : print(insplit[1])
        # utilites
        elif insplit[0] == "osprojects" : proj.init()
        elif insplit[0] == "verinfo" : print(dt.__version__)
        elif insplit[0] == "license" :
            if os.path.isfile("LICENSE") :
                print("LICENSE")
                with open("LICENSE") as f :
                    print(f.read())
            else  : print()
        elif insplit[0] == "password" :
            if insplit[1] == "del" : dt.pwdbox.pwddel()
            elif insplit[1] == "set" :
                newpass = input("Input new password : ")
                dt.pwdbox.setpwd(newpass)
        # open apps
        elif insplit[0] == "run" : os.system("cd ../.. ; python3 \"Programs Files/"+insplit[1]+".py\"")
        # sudo
        elif insplit[0] == "sudo":
            # delete
            if insplit[1] == "delete" : dt.connec.delin("del",insplit[2])
            # install
            elif insplit[1] == "install" : dt.connec.delin("in",insplit[2])

    # excepts
    except IndexError as err : pass

    except FileNotFoundError as err :
        with open(sd.Logs["perflogserropyth"]+"/notfound.log","a") as file :
            file.write("Error 404\n\tError  : File not found !!!\n")
        raise FileNotFoundError("Error  : File not found !!!")

    except ModuleNotFoundError as err :
        with open(sd.Logs["perflogserrorpyth"]+"/notfound.log","a") as file :
            file.write("Error 500\n\tError  : Module not found !!!\n")
        raise ModuleNotFoundError("Error  : Module not found !!!")

    except :
        with open(sd.Logs["perflogserrorpyth"]+"/UNError.log","a") as file :
            file.write("Error 556\n\tError  : Unknow error !!!\n")
        raise SyntaxError("Error  : Unknow error !!!")