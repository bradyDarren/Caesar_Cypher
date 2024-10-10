import string

# user_message = input("Would you like to encode or decode a message? : ")

aplha_values = string.ascii_lowercase
alpha_list = list(aplha_values)

print(alpha_list)


def encode(message, shift_number):
    encoded_message = ""
    for letter in message:
        if letter in alpha_list: 
            encoded_index = alpha_list.index(letter) + shift_number
            encoded_message += alpha_list[encoded_index]
        elif letter == " ":
            encoded_message += " "
    return encoded_message

# test line
print(encode("hello good sir",5))

def decode(message, shift_number):
    decoded_message = "" 
    for letter in message: 
        if letter in alpha_list: 
            decoded_index = alpha_list.index(letter) - shift_number
            decoded_message += alpha_list[decoded_index]
        elif letter == " ":
            decoded_message += " "
    return decoded_message

print(decode("mjqqt ltti xnw",5))
