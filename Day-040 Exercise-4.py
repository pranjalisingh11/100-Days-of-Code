import random
import string

def generate_random_chars(n=3):
    return ''.join(random.choices(string.ascii_letters, k=n))  # only letters

def encode_word(word):
    if len(word) >= 3:
        # Step 1: remove first letter and put it at end
        new_word = word[1:] + word[0]
        # Step 2: add 3 random chars at start and end
        prefix = generate_random_chars(3)
        suffix = generate_random_chars(3)
        return prefix + new_word + suffix
    else:
        # reverse if word length < 3
        return word[::-1]

def decode_word(word):
    if len(word) < 3:
        # reverse if less than 3 chars
        return word[::-1]
    else:
        # Step 1: remove 3 chars from start and end
        core = word[3:-3]
        # Step 2: take last letter and move it to front
        return core[-1] + core[:-1]

def encode_message(msg):
    return ' '.join(encode_word(word) for word in msg.split())

def decode_message(msg):
    return ' '.join(decode_word(word) for word in msg.split())

# Main program
choice = input("Do you want to 'code' or 'decode'? ").strip().lower()

if choice == "code":
    message = input("Enter your message: ")
    print("Encoded message:", encode_message(message))

elif choice == "decode":
    message = input("Enter your secret message: ")
    print("Decoded message:", decode_message(message))

else:
    print("Invalid choice!")

