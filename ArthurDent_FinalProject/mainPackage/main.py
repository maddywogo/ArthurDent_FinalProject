# main.py.py
# Name: Matthew Lisowsky, Harrison Moore, Maddy Wogomon
# email: lisowsmd@mail.uc.edu, wogomomr@mail.uc.edu, moorehc@mail.uc.edu
# Assignment Number: Arthur_Dent_FinalProject
# Due Date: 4/23/2024
# Course/Section: IS4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment: displays picture at statue, movie decryption 

# import statement
from functionsPackage.functions import *


#Entry point
if __name__ == "__main__":
    #Call the functions individually
    decrypt_movie()
    decrypted_location = decrypt_location()
    print("Decrypted location string:", decrypted_location)
    open_image("ArthurDentImage.jpg")