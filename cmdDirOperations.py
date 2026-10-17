#import required built-in modules
import os, shutil, msvcrt, keyboard, time, webbrowser, subprocess

class changeDir:
    def __init__(self):
        os.chdir("/")
        self.cwd = os.getcwd()
        self.nwd = ""

    def path_modifier(self):
        if self.cwd.endswith(" "):
            self.cwd = self.cwd.rstrip(" ")
        if not(self.cwd.endswith(">")):
            if self.cwd == "C:":
                self.cwd = self.cwd + "\\>"
                while msvcrt.kbhit():
                    msvcrt.getch()
                return self.cwd
            self.cwd = self.cwd + ">"
            while msvcrt.kbhit():
                msvcrt.getch()
            return self.cwd
        while msvcrt.kbhit():
            msvcrt.getch()
        return self.cwd
    
    def enter_dir(self):
        opening_options = {"VS Code":"C:/Users/saiva/AppData/Local/Programs/Microsoft VS Code/Code.exe",
                            "Net Beans":"C:/Program Files/netbeans-31-bin/netbeans/bin/netbeans64.exe",
                            "Git Bash":"C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Git/Git Bash",
                            "StarUML":"C:/Program Files/StarUML/StarUML.exe"}
        try:
            if type(self.nwd) != list:
                if self.nwd == "odw":
                    x = 0
                    while True:
                        print(f"\rOpen with - {list(opening_options.keys())[x]}\x1b[K",end="",flush=True)
                        event = keyboard.read_event()
                        time.sleep(0.03)
                        if event.event_type == keyboard.KEY_DOWN:
                            if event.name == "enter":
                                print("Opening with:",list(opening_options.keys())[x])
                                subprocess.Popen([list(opening_options.values())[x],self.cwd])
                                self.cwd = self.cwd.replace(">","")
                                self.nwd = ""
                                time.sleep(0.0375)
                                while msvcrt.kbhit():
                                    msvcrt.getch()
                                break
                            elif event.name == "esc":
                                self.cwd = self.cwd[:self.cwd.rfind("\\")+1]
                                self.nwd = ""
                                break
                            elif event.name == "left":
                                x = x-1
                                if x<0:
                                    x = len(opening_options)-1
                            elif event.name == "right":
                                x = ((x+1)%len(opening_options))
                        time.sleep(0.0375)

                    os.chdir(self.cwd)
                    self.nwd = ""
                    print(f"\r{self.path_modifier()}\x1b[K",end="",sep="",flush=True)

                else:
                    if self.cwd.endswith(">"):
                        self.cwd = self.cwd.rstrip(">")
                    os.chdir(self.cwd)
                    self.nwd = ""
                    print(f"\r{self.path_modifier()}\x1b[K",end="",sep="",flush=True)

            elif type(self.nwd) == list:
                if self.nwd[0] == "odw":
                    for x in list(opening_options.keys()):
                        if self.nwd[1].casefold() == x.casefold():
                            print("Opening with:",x)
                            subprocess.Popen([opening_options[x],self.cwd])
                            time.sleep(0.0375)
                            while msvcrt.kbhit():
                                msvcrt.getch()
                            break
                    else:
                        print("didn't find specified option to open the directory with...")

                os.chdir(self.cwd)
                self.nwd = ""
                while msvcrt.kbhit():
                    msvcrt.getch()
                print(f"\r{self.path_modifier()}\x1b[K",end="",sep="",flush=True)

        except NotADirectoryError:
            self.enter_file() 
    
    def listdir_file(self):
        return os.listdir(self.cwd)

    def enter_file(self):
        opening_options = {"Default":"",
                           "VS Code":"C:/Users/saiva/AppData/Local/Programs/Microsoft VS Code/Code.exe",
                           "Net Beans":"C:/Program Files/netbeans-31-bin/netbeans/bin/netbeans64.exe"}

        if (self.cwd.endswith(".html") or self.cwd.endswith(".java") or self.cwd.endswith(".txt") or self.cwd.endswith(".c") or self.cwd.endswith(".cpp") or self.cwd.endswith(".js") or self.cwd.endswith(".py")):
            x = 0
            while True:
                print(f"\rOpen with - {list(opening_options.keys())[x]}\x1b[K",end="",flush=True)
                event = keyboard.read_event()
                time.sleep(0.04)
                if event.event_type == keyboard.KEY_DOWN:
                    if event.name == "enter":
                        if list(opening_options.keys())[x].casefold() == "default".casefold():
                            webbrowser.open(self.cwd)
                        else:
                            subprocess.Popen([list(opening_options.values())[x],self.cwd])
                        break
                    elif event.name == "esc":
                        break
                    elif event.name == "left":
                        x = x-1
                        if x<0:
                            x = len(opening_options)-1
                    elif event.name == "right":
                        x = ((x+1)%len(opening_options))
        else:
            webbrowser.open(self.cwd)

        self.cwd = self.cwd[:self.cwd.rfind("\\")]
        self.nwd = ""
        while msvcrt.kbhit():
             msvcrt.getch()
        self.enter_dir()
        time.sleep(0.04)

    def enter_dir_file(self):
        if '.' not in self.nwd:
            self.enter_dir()
        else:
            self.enter_file()

    def del_file(self):
        while msvcrt.kbhit():
            msvcrt.getch()
        try:
            os.remove(self.cwd)
            print("file removed successfully...")
            self.cwd = self.cwd[:self.cwd.rfind("\\")] if self.cwd != "C:\\" else self.cwd.replace(">","")
            while msvcrt.kbhit():
                msvcrt.getch()

        except FileNotFoundError:
            print("file does not exist to remove...")
            self.cwd = self.cwd[:self.cwd.rfind("\\")] if self.cwd != "C:\\" else self.cwd.replace(">","")
            while msvcrt.kbhit():
                msvcrt.getch()

    def del_dir(self):
        try:
            os.rmdir(self.cwd)
            print("directory removed successfully...")
            self.cwd = self.cwd[:self.cwd.rfind("\\")] if self.cwd != "C:\\" else self.cwd.replace(">","")
            while msvcrt.kbhit():
                msvcrt.getch()
        except FileNotFoundError:
            if "." in self.cwd[self.cwd.rfind("\\"):]:
                self.del_file()
            else:
                print("directory does not exist to remove...")
                self.cwd = self.cwd[:self.cwd.rfind("\\")] if self.cwd != "C:\\" else self.cwd.replace(">","")
            while msvcrt.kbhit():
                msvcrt.getch()
        except OSError:
            while msvcrt.kbhit():
                msvcrt.getch()
            print("the directory you are trying to remove is not empty, ",end="",sep="",flush=True)
            choice = input(f"do you want to remove {self.nwd[1]}? [('Y'|'y')/('N'|'n')]: ")
            choices = ["Y","y","N","n"]
            while choice not in choices:
                print("please provide proper input...")
                choice = input(f"do you want to remove {self.nwd[1]}? [('Y'|'y')/('N'|'n')]: ")
            else:
                if choice == "Y" or choice == "y":
                    shutil.rmtree(self.cwd)
                    print("directory deleted successfully...")
                    self.cwd = self.cwd[:self.cwd.rfind("\\")] if self.cwd != "C:\\" else self.cwd.replace(">","")
                elif choice == "N" or choice == "n":
                    print("Cancelling deleting operation...")


    def clear_screen(self):
        if os.name == "nt":
            subprocess.run(["cls"],shell=True)
        else:
            subprocess.run(["clear"])
