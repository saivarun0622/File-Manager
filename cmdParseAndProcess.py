#import required built-in modules
import os, keyboard, time, difflib, sys

#import required user-defined modules
from cmdReadInput import *

class parseAndProcess(readInput):
    def __init__(self):
        super().__init__()
        self.user = ""
        self.__psswd = "1857"
        pass

    def check_passwd(self):
        psswd = ""
        attempt =1
        total_attempts = 5 
        status_msg = ""
        if self.user == "sudo":
            while True:
                sys.stdout.write(f"\rEnter Password:{'*'*len(psswd)}\x1b[K\n")
                sys.stdout.write(f"\r{status_msg}\x1b[K\n")
                sys.stdout.write(f"\rPress esc to go back to user selection")
                sys.stdout.write("\x1b[2A\r")
                sys.stdout.flush()
                event = keyboard.read_event()
                if event.event_type == keyboard.KEY_DOWN:
                    if event.name == "esc":
                        sys.stdout.write("\n\n\r\x1b[K\x1b[A\r\x1b[K\x1b[A\r\x1b[K")
                        sys.stdout.flush()
                        return False
                    elif event.name == "enter":
                        sys.stdout.flush()
                        if psswd == self.__psswd:
                            sys.stdout.write("\n\n\r\x1b[K\x1b[A\r\x1b[K\x1b[A\r\x1b[KPermission Granted\n")
                            sys.stdout.flush()
                            return True
                        else:
                            if attempt >= total_attempts:
                                sys.stdout.write("\n\n\r\x1b[K\x1b[A\r\x1b[K\x1b[A\r\x1b[K")
                                print("Max attempts reached... Access Denied for 'sudo' user. Switching to 'user'.")
                                self.user = "user"
                                time.sleep(.075)
                                return False
                            if attempt >= 2:
                                status_msg = f"Incorrect password... You have {total_attempts - attempt} attempts left."
                            else:
                                status_msg = "Incorrect password..."

                            attempt += 1
                            psswd = ""
                            continue
                    elif event.name == "backspace":
                        psswd = psswd[:-1]
                    elif len(event.name)==1:
                        psswd += event.name


        elif self.user == "user":
            while True:
                sys.stdout.write(f"\rEnter Password:{'*'*len(psswd)}\x1b[K\n")
                sys.stdout.write(f"\r{status_msg}\x1b[K\n")
                sys.stdout.write(f"\rPress esc to go back")
                sys.stdout.write("\x1b[2A\r")
                sys.stdout.flush()
                event = keyboard.read_event()
                if event.event_type == keyboard.KEY_DOWN:
                    if event.name == "esc":
                        sys.stdout.write("\n\n\r\x1b[K\x1b[A\r\x1b[K\x1b[A\r\x1b[K")
                        sys.stdout.flush()
                        return False
                    elif event.name == "enter":
                        sys.stdout.flush()
                        if psswd == self.__psswd:
                            sys.stdout.write("\n\n\r\x1b[K\x1b[A\r\x1b[K\x1b[A\r\x1b[KPermission Granted\n")
                            sys.stdout.flush()
                            return True
                        else:
                            if attempt >= total_attempts:
                                sys.stdout.write("\n\n\r\x1b[K\x1b[A\r\x1b[K\x1b[A\r\x1b[K")
                                print("Max attempts reached... Access Denied.")
                                self.user = "user"
                                time.sleep(0.075)
                                return False
                            if attempt >= 2:
                                status_msg = f"Incorrect password... You have {total_attempts - attempt} attempts left."
                            else:
                                status_msg = "Incorrect password..."

                            attempt += 1
                            psswd = ""
                            continue
                    elif event.name == "backspace":
                        psswd = psswd[:-1]
                    elif len(event.name)==1:
                        psswd += event.name

    def parse_user(self):
        users = ["sudo","user"]
        x=0
        while True:
            print(f"\rSelect User: {users[x]}\x1b[K",end="",flush=True)
            event = keyboard.read_event()
            time.sleep(0.03)
            if event.event_type == keyboard.KEY_DOWN:
                if event.name == "enter":
                    if users[x] == "sudo":
                        self.user = "sudo"
                        if(self.check_passwd()):
                            break
                        else:
                            if self.user == "user":
                                break
                            self.user = ""
                            continue
                    elif users[x] == "user":
                        self.user = "user"
                        break
                if event.name == "right":
                    x = (x+1) % len(users)
                elif event.name == "left":
                    x -= 1
                    if x < 0:
                        x = len(users)-1

        self.read_dir_file_name()
            
    def parse_input(self):
        commands = ["cd", "ed", "ldf", "odw", "--help",]
        parsed_path = self.nwd.split(" ",1)
        print()
        match(len(parsed_path)):
            case 1:
                match(parsed_path[0]):
                    case "cd":
                        return self.cwd.rstrip(">"), ""
                    case "ed":
                        return (self.cwd[:self.cwd.rfind("\\")], "") if self.cwd != "C:\\>" else (self.cwd.rstrip(">"), "")
                    case "ldf":
                        return self.cwd.rstrip(">"), parsed_path[0]
                    case "odw":
                        return (self.cwd.replace(">", ""),parsed_path[0])
                    case "--help":
                        for i in commands:
                            match(i):
                                case "cd":
                                    print("'cd <dir_name>' - Used to change to the child directory of the current directory\n")
                                case "ed":
                                    print("'ed' - Used to change to the parent/previous directory of the current directory\n")
                                case "ldf":
                                    print("'ldf' - Used to list the directories and files present in current directory\n")
                                case "odw":
                                    print("'odw <option>' - Used to open current directory with selected option\n")
                                case "--help":
                                    print("'--help' - Used to help with commands\n")
                        else:
                            return self.cwd.rstrip(">"), ""
                    case _:
                        if '.' in parsed_path[0]:
                            return (self.cwd.replace(">", "\\") + parsed_path[0],parsed_path[0]) if self.cwd != "C:\\>" else (self.cwd.replace(">", "") + parsed_path[0],parsed_path[0])
                        print("please provide proper input... [type '--help' for details on differnt commands]")
                        return self.cwd.rstrip(">"), ""
                                    
            case 2:
                match parsed_path[0]:
                    case "cd":
                        return (self.cwd.replace(">", "\\") + parsed_path[1],parsed_path[1]) if self.cwd != "C:\\>" else (self.cwd.replace(">", "") + parsed_path[1],parsed_path[1])
                    case "ed":
                        return (self.cwd.replace(">", "\\") + parsed_path[1],parsed_path[1]) if self.cwd != "C:\\>" else (self.cwd.replace(">", "") + parsed_path[1],parsed_path[1])


    def dirname_corrector(self):
        self.cwd = self.cwd[:self.cwd.rfind("\\")+1]
        for _ in range(3):
            print("\rmentioned dir/file doesn't exitst. Searching for close matches   ",end="",flush=True)
            time.sleep(0.275)
            print("\rmentioned dir/file doesn't exitst. Searching for close matches.  ",end="",flush=True)
            time.sleep(0.275)
            print("\rmentioned dir/file doesn't exitst. Searching for close matches.. ",end="",flush=True)
            time.sleep(0.275)
            print("\rmentioned dir/file doesn't exitst. Searching for close matches...",end="",flush=True)
            time.sleep(1.275)
        print()
        dir_files = [dir_file.casefold() for dir_file in self.listdir_file()]
        dir_files = difflib.get_close_matches(self.nwd, dir_files, n=len(dir_files), cutoff=0.27)
        if not dir_files:
            print("no matching directories or files found, returning to parent dir...")
            print()
            return self.cwd if self.cwd == "C:\\" else self.cwd.rstrip("\\")
        spacing = len(max(dir_files,key=len))
        print("closest matched directories and files in current directory: ")
        for i in range(len(dir_files)):
            row = dir_files[i:i+5]
            for item in row:
                print(item + (" "*(spacing-len(item))),end="")
            print()
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
                        print()
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
                if self.nwd == "ldf":
                    if self.user == "sudo":
                        dir_files = self.listdir_file()
                    elif self.user == "user":
                        print("trying to access directories/files... please provide password")
                        if(self.check_passwd()):
                            dir_files = self.listdir_file()
                            spacing = len(max(dir_files,key=len))
                            for i in range(0,len(dir_files),5):
                                row = dir_files[i:i+5]
                                for item in row:
                                    print(item + (" "*(spacing-len(item))),end="")
                                print()
                        else:
                            print("'ldf' cmd terminated")
                self.enter_dir_file()

            except FileNotFoundError:
                self.cwd = self.dirname_corrector()
                self.enter_dir_file()