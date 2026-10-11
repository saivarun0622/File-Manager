#import other classes(.py files) into the main class(main.py)
import cmdParseAndProcess

if __name__ == '__main__':
    print("Started cmd...")
    mainobj = cmdParseAndProcess.parseAndProcess()
    mainobj.parse_user()