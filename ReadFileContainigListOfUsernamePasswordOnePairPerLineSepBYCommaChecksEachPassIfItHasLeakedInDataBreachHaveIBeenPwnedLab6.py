#Program NO 6
#write a python program that reads a file containing a list of usernames andpasswords.One pair per line(seperatized by a comma).it checks each password tosee if it has been leaked in a databreach.you can use the "Have I Been Pwned"API (https://haveibeenpwned.com)/API/v3) to check if a password has been leaked

import requests
import hashlib

with open('passwords.txt', 'r') as f:
    for line in f:
        username, password = line.strip().split(',')

        password_hash = hashlib.sha1(password.encode('utf8')).hexdigest().upper()

        response = requests.get(f"https://api.pwnedpasswords.com/range/{password_hash[:5]}")

        if response.status_code == 200:
            hashes = [line.split(':') for line in response.text.splitlines()]
            for h, count in hashes:
                if password_hash[5:] == h:
                    print(f"Password for user {username} has been leaked {count} times.")
                    break
            else:
                print(f"Password for user {username} has not been found in the breach database.")
        else:
            print(f"Could not check password for user {username}.")

