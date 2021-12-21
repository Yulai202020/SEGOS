import os,socket,requests,shifr,glob,sys
import settings.settdata as sd

help = """"cd          //cmd
echo/print  //cmd print
osprojects  //os projects
verinfo     //os version
license     //print license
password    //set password
run         //run apps
sudo        //install/delete apps"""

user = "Admin";nameos = "SEGOS";__version__ = "v1.0.0";userlist=[]
apin = "App is downloaded !!!";gain = "Game is downloaded !!!";pwdcorrect=""
host = "https://localhost:1000";port = 1000

class passwords:

    def pwddel(self):
        with open("../../Users/"+user+"password.key","w") as f:
            pwdcorrect = "";f.write("")

    def pwd(self):
        try:
            user = input("Input name user # ")
            with open("../../Users/"+user+"/password.key","r") as f:
                pwdcorrect=shifr.decrypt(f.read())
            if pwdcorrect == "":return
            password = input("Input password # ")
            while password != pwdcorrect:
                with open("../../Users/"+user+"/password.key","r") as f:
                    pwdcorrect=shifr.decrypt(f.read())
                print("Incorrect password !")
                password = input("Input password # ")
        except FileNotFoundError as err :
            with open(sd.Logs["perflogserropyth"]+"/notfound.log","a") as file :
                file.write("Error 404\n\tError  : User not found !!!\n")
                print("User not found !!!")
        except KeyboardInterrupt as err :
            with open(sd.Logs["perflogsinfopyth"]+"/exit.log","a") as file :
                file.write("Code 200\n\tExiting ...\n")
            print();sys.exit(0)

    def setpwd(self,pwd):
        with open("../../Users/"+user+"/password.key","w") as f:
            f.write(shifr.encrypt(pwd))

class conn:

    def is_connected(self):
        try:socket.create_connection((host, port))
        except OSError:print("File server not connected !\n\tFor install apps and games .\n\tError 404 .");exit(0)

    def delin(self,oper="del",name="calculatorapp"):
        comp = "Complited !!!"
        if oper == "del":self.deleter('../../Programs Files/'+name+'.exe');print(comp)
        elif oper == "in" :self.downloadFile("http://localhost:1000/files/"+name,"../../Programs Files/",name);print(comp)

    def downloadFile(self,URL=None,pyth="../Programs Files/apps",ver="0"):
        req = requests.get(URL)
        f = open(pyth+ver+".exe", 'wb')
        f.write(bytes(req.text,encoding=''))
        f.close()

    def deleter(pyth):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), pyth)
        os.remove(path)

def init():
    userlist = glob.glob('../../Users/*')
    a = userlist;userlist=[]
    for i in a:userlist.append(i[12:])
    with open("../data/setup.sys","r") as f:
        print(f.read())

pwdbox = passwords()
connec = conn()