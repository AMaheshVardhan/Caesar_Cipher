Caesar Cipher Encryption and Decryption
This code demonstrates a basic implementation of the Caesar cipher algorithm for encrypting and decrypting text messages. The Caesar cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of positions down or up the alphabet.

Usage
Clone the repository or download the code files.

Open the file containing the code in a Python editor or IDE.

Uncomment either line 2 or line 3, depending on whether you want to encode or decode a message. You can uncomment one line at a time.

Run the code.

Enter your message when prompted and press Enter.

Enter the shift number (the number of positions to shift the letters) when prompted and press Enter.

The encoded or decoded message will be displayed on the screen.

Code Explanation
The code starts by defining the alphabet as a list of lowercase letters.

The user is prompted to enter their message.

The user is prompted to enter the shift number.

The encrypt function takes the plain text and shift amount as inputs. It iterates over each letter in the plain text, finds its position in the alphabet, calculates the new position by adding the shift amount, and retrieves the new letter from the alphabet. The new letter is then added to the cipher text. Finally, the encoded text is displayed on the screen.

The decrypt function is similar to the encrypt function, but it subtracts the shift amount from the position to retrieve the original letter.

The user is prompted to choose whether to encode or decode the message.

If the user chooses to encode, the encrypt function is called with the provided text and shift number.

If the user chooses to decode, the decrypt function is called with the provided text and shift number.

Note
Make sure to comment out one of the lines (#direction=input("Hey,Type 'encode' to encrypt") or #direction=input("decode' to decrypt")) depending on whether you want to encode or decode a message. Uncommenting both lines will result in a syntax error.

Feel free to modify and enhance the code according to your requirements!
