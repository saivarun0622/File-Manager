#import required built-in modules
import os, keyboard, time

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

    def enter_dir_file(self):
        os.chdir(self.cwd)
        self.nwd = ""
        print(f"\r{self.path_modifier()}\x1b[K",end="",sep="",flush=True)

    def listdir_file(self):
        return os.listdir(self.cwd)