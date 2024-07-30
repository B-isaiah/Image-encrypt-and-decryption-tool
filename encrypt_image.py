import os
from cryptography.fernet import Fernet

def encrypt_images(file_paths, fernet):
    for file_path in file_paths:
        try:
            with open(file_path, 'rb') as f:
                data = f.read()
            encrypted_data = fernet.encrypt(data)
            encrypted_file_path = os.path.join(os.path.dirname(file_path), f"locked_{os.path.basename(file_path)}")
            with open(encrypted_file_path, 'wb') as encrypted_file:
                encrypted_file.write(encrypted_data)
            print(f"File has been encrypted and saved")
        except Exception as e:
            print(f"Error encrypting '{file_path}': {e}")

def decrypt_images(file_paths, fernet):
    for file_path in file_paths:
        try:
            with open(file_path, 'rb') as f:
                encrypted_data = f.read()
            decrypted_data = fernet.decrypt(encrypted_data)
            decrypted_file_path = os.path.join(os.path.dirname(file_path), f"unlocked_{os.path.basename(file_path)}")
            with open(decrypted_file_path, 'wb') as decrypted_file:
                decrypted_file.write(decrypted_data)
            print(f"File has been decrypted and saved")
        except Exception as e:
            print(f"Error decrypting '{file_path}': {e}")

def main():
    try:
        # Load the key from the file
        with open('key.key', 'rb') as f:
            key = f.read()

        # Create a Fernet object with the key
        fernet = Fernet(key)

        # Get the list of files to encrypt
        file_paths = input("Enter the paths of the images to encrypt, separated by commas: ").split(',')

        # Strip whitespace from file paths
        file_paths = [file_path.strip() for file_path in file_paths]

        # Encrypt the files
        encrypt_images(file_paths, fernet)

        # Decrypt the files
        encrypted_file_paths = [os.path.join(os.path.dirname(file_path), f"locked_{os.path.basename(file_path)}") for file_path in file_paths]
        decrypt_images(encrypted_file_paths, fernet)

    except Exception as e:
        print(f"Error caught: {e}")

# Ask the user if they want to run the program again or exit
rerun_response = ['yes', 'no']

# Automate the program to continue or end
rerun = True
while rerun:
    main()

    rerun_input = input('\nHello! Do you want to use this program again? Enter "yes" to continue or "no" to exit\n').lower()

    while rerun_input not in rerun_response:
        rerun_input = input('\nPlease enter the correct keyword❗, Enter "yes" to continue or "no" to exit\n').lower()
    
    if rerun_input == 'no':
        print('Thank you for using the Image manipulation Program developed by Cyberbzee. Have a nice day!\n')
        rerun = False
