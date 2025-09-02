def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypts or decrypts text using the Caesar Cipher algorithm.

    Parameters:
    text (str): The input text to process
    shift (int): The number of positions to shift each character
    mode (str): 'encrypt' or 'decrypt'

    Returns:
    str: The encrypted or decrypted text
    """
    result = ""

    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            # Determine the appropriate base (uppercase or lowercase)
            base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around the alphabet
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            result += shifted_char
        else:
            # Non-alphabetic characters remain unchanged
            result += char

    return result


def main():
    print("Caesar Cipher Program")
    print("=====================")

    while True:
        # Get mode from user
        mode = input("\nDo you want to (e)ncrypt or (d)ecrypt? (q to quit): ").lower()

        if mode == 'q':
            print("Goodbye!")
            break
        elif mode not in ['e', 'd']:
            print("Please enter 'e' for encrypt or 'd' for decrypt.")
            continue

        # Get message from user
        message = input("Enter your message: ")

        # Get shift value from user
        while True:
            try:
                shift = int(input("Enter the shift value (1-25): "))
                if 1 <= shift <= 25:
                    break
                else:
                    print("Shift value must be between 1 and 25.")
            except ValueError:
                print("Please enter a valid number.")

        # Process the message
        if mode == 'e':
            result = caesar_cipher(message, shift, 'encrypt')
            print(f"\nEncrypted message: {result}")
        else:
            result = caesar_cipher(message, shift, 'decrypt')
            print(f"\nDecrypted message: {result}")


if __name__ == "__main__":
    main()