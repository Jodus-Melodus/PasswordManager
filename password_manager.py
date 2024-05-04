import json
from string import ascii_lowercase, ascii_uppercase, digits
from random import randrange

def generate_new_random_password(args: list[str]) -> str:
    password = ""
    length = int(args[0]) if args[0] != "" else 8
    lowercase_letters = False if args[1] == "F" else True
    uppercase_letters = False if args[2] == "F" else True
    numbers = False if args[3] == "F" else True
    special_characters = False if args[4] == "F" else True
    
    possible_characters = (ascii_lowercase if lowercase_letters else "") + (ascii_uppercase if uppercase_letters else "") + (digits if numbers else "") + ("~!@#$%^&*:;<>?" if special_characters else "")
    
    while len(password) < length:
        random_index = randrange(0, len(possible_characters))
        password += possible_characters[random_index]
    
    return password

def read_passwords() -> dict[str, str]:
    with open("passwords.json", "r") as f:
        passwords = json.load(f)
    
    return passwords
    
def write_passwords(passwords: dict[str, str]) -> None:
    with open("passwords.json", "w") as f:
        json.dump(passwords, f)

def main():
    password = ""
    passwords = read_passwords()
    
    while True:
        print("""
            new <length(number)> <includeuppercase(T/F)> <includelowercase(T/F)> <includedigits(T/F)> <includespecialcharacters(T/F)> -> generate a new password
            get <name> -> returns the password linked with a name
            save <name> -> save last generated password with a name
            remove <name> -> delete password linked with a name
            kill/exit/quit -> save and close
            """)
        
        arguments = input("> ").split(" ")
        cmd = arguments[0]
        
        if len(arguments) > 1:
            args = arguments[1:]
        else:
            args = []
        
        match cmd:
            case "new":
                password = generate_new_random_password(args)
                print(password)
            case "get":
                print(passwords[args[0]])
            case "save":
                passwords[args[0]] = password
                write_passwords(passwords)
                print(f"Saved '{password}' in {args[0]}")
            case "remove":
                passwords.pop(args[0])
                print(f"Successfully removed password saved under '{args[0]}'")
            case "exit" | "quit" | "kill":
                write_passwords(passwords)
                break
            case _:
                pass
            
    
if __name__ == "__main__":
    main()