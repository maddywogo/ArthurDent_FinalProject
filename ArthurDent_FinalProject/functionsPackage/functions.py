# functions.py
# Name: Matthew Lisowsky, Harrison Moore, Maddy Wogomon
# email: lisowsmd@mail.uc.edu, wogomomr@mail.uc.edu, moorehc@mail.uc.edu
# Assignment Number: Arthur_Dent_FinalProject
# Due Date: 4/23/2024
# Course/Section: IS4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment:

# imports (ex: from functionPackage.functions import *)
from cryptography.fernet import Fernet

#ChatGPT used
def decrypt_location(encrypted_data_file, english_file):

    decrypted_string = ""
    with open(english_file, "r") as f:
        english_data = f.readlines()
    for index in encrypted_data_file:
        line_number = int(index)
        decrypted_string += english_data[line_number].strip() + " "
    return decrypted_string.strip()

# Example usage:
encrypted_data = [

    "39744",
    "28799",
    "27511",
    "17302",
    "5082",
    "31053",
    "22147",
    "103568",
    "21085",
    "105654",
    "23926",
    "23887",
    "940",
    "15378",
    "17514",
    "41519",
    "2756",
    "23926",
    "23887",
    "29212"] 

english_file_path = "UCEnglish.txt"
decrypted_location = decrypt_location(encrypted_data, english_file_path)
print("Decrypted location string:", decrypted_location)

def decrypt_movie():
    key = Fernet.generate_key()
    f = Fernet("2tWgZTHycJHttRAQkazCO-Qr66EBdm1mW1-QgCcSzVs=")
    token = "gAAAAABlTNM6E_sG85Z7exRFRBnvBhpDhL4rzknNKiPZGnjR_Zem2ZxvlzxwyyoyS3ixtb6Hz_REgEGhTKMWJzJkDy3Slqj49g=="
    print(token)
    decrypted_token = f.decrypt(token.encode()).decode()
    print(decrypted_token)

decrypt_movie()