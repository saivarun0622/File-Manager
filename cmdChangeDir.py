#import required built-in modules
import os, keyboard, time, webbrowser, subprocess

class changeDir:
    def __init__(self):
        os.chdir("/")
        self.cwd = os.getcwd()
        self.nwd = ""

    def path_modifier(self):
        if not(self.cwd.endswith(">")):
            if self.cwd == "C:":
                self.cwd = self.cwd + "\\>"
                return self.cwd
            self.cwd = self.cwd + ">"
            return self.cwd
        return self.cwd
    
    def enter_dir(self):
        opening_options = {"VS Code":"C:/Users/saiva/AppData/Local/Programs/Microsoft VS Code/Code.exe",
                            "Net Beans":"C:/Program Files/netbeans-31-bin/netbeans/bin/netbeans64.exe",
                            "Git Bash":"C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Git/Git Bash"}
        try:
            if self.nwd == "odw":
                x = 0
                while True:
                    print(f"\rOpen with - {list(opening_options.keys())[x]}\x1b[K",end="",flush=True)
                    event = keyboard.read_event()
                    time.sleep(0.03)
                    if event.event_type == keyboard.KEY_DOWN:
                        if event.name == "enter":
                            print(list(opening_options.values())[x])
                            subprocess.Popen([list(opening_options.values())[x],self.cwd])
                            self.cwd = self.cwd[:self.cwd.rfind("\\")+1]
                            self.nwd = ""
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

                os.chdir(self.cwd)
                self.nwd = ""
                print(f"\r{self.path_modifier()}\x1b[K",end="",sep="",flush=True)

            else:
                os.chdir(self.cwd)
                self.nwd = ""
                print(f"\r{self.path_modifier()}\x1b[K",end="",sep="",flush=True)

        except NotADirectoryError:
            self.enter_file()
        
    
    def listdir_file(self):
        return os.listdir(self.cwd)

    def enter_file(self):
        opening_options = {"Default":"",
                           "VS Code":"C:/Users/saiva/AppData/Local/Programs/Microsoft VS Code/Code.exe",
                           "Net Beans":"C:/Program Files/netbeans-31-bin/netbeans/bin/netbeans64.exe"}

        if (self.cwd.endswith(".html") or self.cwd.endswith(".java") or self.cwd.endswith(".txt")):
            x = 0
            while True:
                print(f"\rOpen with - {list(opening_options.keys())[x]}",end="",flush=True)
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
                            x = len(opening_options)
                    elif event.name == "right":
                        x = ((x+1)%len(opening_options))

            self.cwd = self.cwd[:self.cwd.rfind("\\")]
            self.nwd = ""
            self.enter_dir()
            time.sleep(0.04)

    def enter_dir_file(self):
        if '.' not in self.nwd:
            self.enter_dir()
        else:
            self.enter_file()