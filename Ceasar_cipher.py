# Create the encryption function
def cipher_encrypt(text, offset):
    encoded_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter to encrypt it
            start = 65 if char.isupper() else 97  # ASCII for 'A' or 'a'
            encoded_char = chr((ord(char) - start + offset) % 26 + start)  # Encrypt logic
        else:
            encoded_char = char  # Non-alphabetic characters remain the same
        encoded_text += encoded_char
    return encoded_text

# Create the decryption function
def cipher_decrypt(text, offset):
    decoded_text = ""
    for char in text:
        if char.isalpha():  # Same logic as encryption but reverse the shift
            start = 65 if char.isupper() else 97
            decoded_char = chr((ord(char) - start - offset) % 26 + start)
        else:
            decoded_char = char
        decoded_text += decoded_char
    return decoded_text

# Main code to get user input and perform encryption or decryption
user_input = input("Enter the message you want to encrypt or decrypt: ")
mode = ""  # Initialize with an empty string to enter the loop

while mode != 'e' and mode != 'd':  # Loop until user chooses 'e' or 'd'
    mode = input("If you want to encrypt the message, type 'e'. If you want to decrypt it, type 'd': ")

shift_value = int(input("Enter the shift value for encryption or decryption: "))

if mode == 'e':
    print("The encrypted message is:", cipher_encrypt(user_input, shift_value))
elif mode == 'd':
    print("The decrypted message is:", cipher_decrypt(user_input, shift_value))

