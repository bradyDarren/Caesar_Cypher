import string

aplha_values = string.ascii_lowercase
alpha_list = list(aplha_values)

# test line
# print(alpha_list)

def encode(message, shift_number):
    encoded_message = ""
    for letter in message:
        if letter in alpha_list: 
            encoded_index = alpha_list.index(letter) + shift_number
            if encoded_index > len(alpha_list):
                encoded_index = encoded_index - len(alpha_list)
            encoded_message += alpha_list[encoded_index]
        elif letter == " ":
            encoded_message += " "
    return encoded_message


# # test line
# print(encode("hello good sir",30))

def decode(message, shift_number):
    decoded_message = "" 
    for letter in message: 
        if letter in alpha_list: 
            decoded_index = alpha_list.index(letter) - shift_number
            decoded_message += alpha_list[decoded_index]
        elif letter == " ":
            decoded_message += " "
    return decoded_message

# test line
# print(decode("lipps kssh wmv",30))

def start():
    go_again = "yes"
    while go_again == "yes":
        user_choice = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
        if user_choice == "encode":
            user_message = input("Type your message: ")
            user_shift = int(input("Type the shift number: "))
            result = encode(user_message, user_shift)
            print(f"Here is your encoded result: {result}")
            go_again = input("Type 'yes' if you want to go agian. Otherwise type 'no'.").lower()
            if go_again != "yes" or go_again != "no":
                print("Please pick a appropriate selection")
        elif user_choice == "decode":
            user_message = input("Type your message: ")
            user_shift = int(input("Type the shift number: "))
            result = decode(user_message, user_shift)
            print(f"Here is your decoded result: {result}")
            go_again = input("Type 'yes' if you want to go agian. Otherwise type 'no'.").lower()
        else:
            print("Please pick a appropriate selection")
            continue
            
        

start()

# look into the following - what happens when a person inputs a value that exceeds the 26 letters of the alphabet? 


