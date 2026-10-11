import getpass

pssd = "1857"

psswd =""
while psswd != pssd:
    psswd = getpass.getpass(f"\rEnter your password: [press 'esc' to go back to user selection]\x1b[K", echo_char="*")
    print(psswd)