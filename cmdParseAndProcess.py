#import required built-in modules
import os, keyboard, time, difflib

#import required user-defined modules
from cmdReadInput import *

class parseAndProcess(readInput):
    def __init__(self):
        super().__init__()
        pass

    def parse_input(self):
        commands = ["cd","ed"]
        parsed_path = self.nwd.split(" ",1)
        print()
        match(len(parsed_path)):
            case 1:
                if parsed_path[0] == "cd":
                    return self.cwd.rstrip(">")
                
            case 2:
                if parsed_path[0] == "cd":
                    return ((self.cwd.replace(">", "\\") + parsed_path[1]),parsed_path[1]) if self.cwd != "C:\\>" else (self.cwd.replace(">", "") + parsed_path[1],parsed_path[1])

    def dirname_corrector(self):
        self.cwd = self.cwd[:self.cwd.rfind("\\")+1]
        print("mentioned dir/file doesn't exitst. Searching for close matches...")
        time.sleep(5)
        dir_files = [dir_file.casefold() for dir_file in self.listdir_file()]
        dir_files = difflib.get_close_matches(self.nwd, dir_files, n=len(dir_files), cutoff=0.27)
        if not dir_files:
            print("no matching directories or files found, returning to parent dir...")
            print()
            return self.cwd if self.cwd == "C:\\" else self.cwd.rstrip("\\")
        print("closest matched directories and files in current directory: ")
        for i in range(len(dir_files)):
            if((i+1)%5!=0):
                print(dir_files[i],end="    ")
            else:
                print(dir_files[i])
        else:
            print()
            print("Select the directory/file you want to access..[Press 'esc' to return back to the parent dir]")
            x=0
            while True:
                print(f"\r{self.cwd}{dir_files[x]}\x1b[K",end="",flush=True)
                event = keyboard.read_event()
                time.sleep(0.03)
                if event.event_type == keyboard.KEY_DOWN:
                    if event.name == "enter":
                        return self.cwd + dir_files[x]
                    elif event.name == "esc":
                        print("returning to parent dir")
                        return self.cwd if self.cwd == "C:\\" else self.cwd.rstrip("\\")
                    elif event.name == "left":
                        x = x-1
                        if x == -1:
                            x = len(dir_files)-1
                    elif event.name == "right":
                        x = ((x+1) % len(dir_files))


    def process_input(self):
        if self.nwd == "":
            self.cwd = self.cwd.rstrip(">")
            self.enter_dir_file()
        else:
            try:
                self.cwd,self.nwd = self.parse_input()
                print(self.nwd)
                print(self.cwd)
                self.enter_dir_file()

            except FileNotFoundError:
                self.cwd = self.dirname_corrector()
                self.enter_dir_file()
                
            else:
                # self.enter_dir_file()
                pass
