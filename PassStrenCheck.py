import re
import argparse

print("----------------Password Strength Checker ~by JUDE----------------------",end='\n')

def is_strong_password(password):
    if len(password) < 8:
        return False
        
    if not re.search(r'[a-z]', password) or not re.search(r'[A-Z]', password):
        return False

    if not re.search(r'\d', password):
        return False

    if not re.search(r'[!@#$%^&*()-_+=]', password):
        return False

    common_words = ["password", "123456", "qwerty", "admin"]
    if any(word in password.lower() for word in common_words):
        return False

    return True

def main():
    parser = argparse.ArgumentParser(description="Password Strength Checker -by JUDE")
    parser.add_argument("-p", "--password", help="Password to check")
    args = parser.parse_args()

    if args.password:
        if is_strong_password(args.password):
            print("Password is strong!")
        else:
            print("Password is weak. Please consider making it stronger.")
    else:
        print("Password not provided. Use 'python pass.py -p [password]' to check a password.")

print("*** For more details and Tools visit our GitHub page 'CyberMystic-Jude' ***",end='\n\n')

if __name__ == "__main__":
    main()
