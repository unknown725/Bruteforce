import time
import argparse
import os

def brute_force_password(wordlist, target_username):
    attempts = 0

    for password in wordlist:
        password = password.strip()  # Remove any trailing newline characters
        print(f'Testing password: \033[1;33m{password}\033[0m')  # Print password in bold yellow

        # Simulating a guess attempt
        time.sleep(0.1)  # To slow down the attempts (optional)

        # Check against the target username
        if password == target_username: 
            print(f'Password found: \033[1;33m{password}\033[0m after {attempts} attempts!')  # Print found password in bold yellow
            return

        attempts += 1

    print(f'Password not found in the wordlist: {target_username}.')

if __name__ == "__main__":  # Corrected to use double underscores
    # Command line argument parser
    parser = argparse.ArgumentParser(description='Brute force password guessing tool.')
    parser.add_argument('target_username', help='The target username to guess the password for')  # Changed to target_username
    parser.add_argument('--wordlist', default='default_wordlist.txt', help='Path to the wordlist file (default: default_wordlist.txt)')
    
    args = parser.parse_args()
    
    # Check if the specified wordlist file exists
    if not os.path.isfile(args.wordlist):
        print(f"Error: The file {args.wordlist} was not found. Please provide a valid wordlist.")
    else:
        # Load the wordlist from the specified file
        with open(args.wordlist, 'r') as file:
            wordlist = file.readlines()
        
        print(f"\nUsing wordlist: {args.wordlist}")
        brute_force_password(wordlist, args.target_username)  # Changed to use target_username
