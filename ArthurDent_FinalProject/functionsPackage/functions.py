# functions.py
# Name: Matthew Lisowsky, Harrison Moore, Maddy Wogomon
# email: lisowsmd@mail.uc.edu, wogomomr@mail.uc.edu, moorehc@mail.uc.edu
# Assignment Number: Arthur_Dent_FinalProject
# Due Date: 4/23/2024
# Course/Section: IS4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment: decodes the location of our picture and decodes our movie

# imports (ex: from functionPackage.functions import *)
from cryptography.fernet import Fernet
from PIL import Image
import os

def decrypt_location():
    # Define the required variables within the function
    
    '''
    This function decodes the location of our picture and decodes our movie
    :Parameter: decrypted_location
    :Return: location
    '''
   
    encrypted_data_file = [
        "39744", "28799", "27511", "17302", "5082", "31053", "22147", 
        "103568", "21085", "105654", "23926", "23887", "940", "15378", 
        "17514", "41519", "2756", "23926", "23887", "29212"
    ] 
    english_file = "../functionsPackage/UCEnglish.txt"

    # Perform decryption
    decrypted_string = ""
    with open(english_file, "r") as f:
        english_data = f.readlines()
    for index in encrypted_data_file:
        line_number = int(index)
        decrypted_string += english_data[line_number].strip() + " "
    decrypted_location = decrypted_string.strip()
    
    # Return the decrypted location
    return decrypted_location

def decrypt_movie():
    key = Fernet.generate_key()
    f = Fernet("2tWgZTHycJHttRAQkazCO-Qr66EBdm1mW1-QgCcSzVs=")
    token = "gAAAAABlTNM6E_sG85Z7exRFRBnvBhpDhL4rzknNKiPZGnjR_Zem2ZxvlzxwyyoyS3ixtb6Hz_REgEGhTKMWJzJkDy3Slqj49g=="
    print("Provided Token: ", token)
    decrypted_token = f.decrypt(token.encode()).decode()
    print("Decrypted Token: ", decrypted_token)

def open_image(image_filename):
    try:
        image_path = "../functionsPackage/ArthurDentImage.jpg"  # Change this to the path of your image file
        
        # Open image
        if not os.path.exists(image_path):
            print("Error: Image path does not exist.")
            return
        image = Image.open(image_path)
        rotated_image = image.rotate(-90, expand=True)
        rotated_image.show()
    except Exception as e:
        print("Error:", e)