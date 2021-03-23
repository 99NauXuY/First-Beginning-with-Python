should_end = True
while should_end:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
    def encrypt(text, shift):
        #Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
        encryptWord = ""
        for buchstabe in text:
            neu = alphabet.index(buchstabe) + shift
            while neu>25:
                neu -= 26
            encryptWord += alphabet[neu]
        print(f'The encoded text is {encryptWord}')

    #Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
    def decrypt(text, shift):
        #Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
        decryptWord = ""
        for buchstabe in text:
            neu = alphabet.index(buchstabe) - shift
            while neu<0:
                neu += 26
            decryptWord += alphabet[neu]
        print(f'The decoded text is {decryptWord}')

    if choice == "encode":
        encrypt(text, shift)
    elif choice == "decode":
        decrypt(text, shift)
    else:
        print("Falsche Eingabe bei 1.Wahl")
    #neuer Versuch
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = False
        print("Goodbye")