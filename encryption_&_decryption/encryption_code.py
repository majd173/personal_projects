def subencryption(plaintext, alphabet, shuffled):
    ciphertext = ""
    for char in plaintext:
        if char in alphabet:
            position = alphabet.index(char)
            newposition = shuffled[position]
            ciphertext = ciphertext + newposition
        else:
            ciphertext = ciphertext + char
    return ciphertext


alphabet = "abcdefghijklmnopqrstuvwxyz"
shuffled = "vyjkzutsrqbahmlxwingfedcpo"

while True:
    try:
        # Input plaintext message
        plaintext_message = input("ENTER YOUR MESSAGE HERE USING -small- ENGLISH LETTERS: ")
        print(".")
        print(".")
        print(".")
        print("YOUR CIPHERED MESSAGE IS:", subencryption(plaintext_message, alphabet, shuffled))
        print(".")
        print(".")
        print(".")
    except Exception as e:
        print("An error occurred:", e)

    # Prompt the user to see if they want to continue or exit
    continue_program = input(
        "DO YO WANT TO ENCRYPT ANOTHER MESSAGE? (yes/no) ->-> use small english letters: ").strip().lower()
    if continue_program != "yes":
        break

# Wait for user input before closing
input("Press Enter to close the program...")
