#import required built-in modules
import os, keyboard, time

#import required user-defined modules
from cmdDirOperations import *

class readInput(changeDir):
    def __init__(self):
        super().__init__()
        pass

    def process_input(self):
        pass

    def read_dir_file_name(self):
        print(f"\r{self.path_modifier()}\x1b[K",end="",sep="",flush=True)
        while True:
            pressedEnter = True
            while pressedEnter:

                event = keyboard.read_event()
                time.sleep(0.03)

                if event.event_type == keyboard.KEY_DOWN:

                    if event.name == "enter":
                      pressedEnter = False

                    elif event.name == "backspace":
                        self.nwd = self.nwd[:-1]

                    elif event.name == "esc":
                        if self.nwd == "":
                            if self.cwd == "C:\\>":
                                self.cwd = self.cwd[:self.cwd.rindex(">")]
                            else:
                                self.cwd = self.cwd[:self.cwd.rindex("\\")]
                                print()
                            self.enter_dir_file()
                            pressedEnter = False
                        else:
                            self.nwd = ""
                            pressedEnter = False

                    else:
                      if len(event.name)==1 or event.name =="space":
                          if event.name == "space":
                            self.nwd += " "
                          else:
                            self.nwd += event.name
                print(f"\r{self.cwd}{self.nwd}\x1b[K",end="",sep="",flush=True)
    
            else:
                self.process_input()
    
            time.sleep(0.05)