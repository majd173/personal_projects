def enc(msg, alphabet, shuffled):
    ciphertext = ""
    for char in msg:
        if char in alphabet:
            index = alphabet.index(char)
            char_new = shuffled[index]
            ciphertext = ciphertext + char_new
        else:
            ciphertext = ciphertext + char  # Preserve spaces and any non-alphabet characters
    return ciphertext


def dec(cipher, alphabet, shuffled):
    original = enc(cipher, shuffled, alphabet)
    return original


cipher = ""
alphabet = "abcdefghijklmnopqrstuvwxyz"
shuffled = "vyjkzutsrqbahmlxwingfedcpo"

while True:
    try:
        # Input ciphered message
        ciphered_message = input("ENTER YOUR CIPHERED MESSAGE HERE USING -small- ENGLISH LETTERS: ")
        print(".")
        print(".")
        print(".")
        print("YOUR ORIGINAL MESSAGE IS:", dec(ciphered_message, alphabet, shuffled))
        print(".")
        print(".")
        print(".")
    except Exception as e:
        print("An error occurred:", e)

    # Prompt the user to see if they want to continue or exit
    continue_program = input("DO YOU WANT TO DECRYPT ANOTHER MESSAGE? (yes/no) ->-> use small english letters: ").strip().lower()
    if continue_program != "yes":
        break

# Wait for user input before closing
input("Press Enter to close the program...")