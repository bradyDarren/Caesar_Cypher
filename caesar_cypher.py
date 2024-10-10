import string

aplha_values = string.ascii_lowercase
alpha_list = list(aplha_values)

# test line
# print(alpha_list)
print(alpha_list[0])
print(alpha_list[1])

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
# print(encode("hello good sir",5))

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
# print(decode("mjqqt ltti xnw",5))

def start(): 
    user_choice = input("Would you like to encode or decode a message? : ").lower()
    if user_choice == "encode":
        user_message = input("Type your message: ")
        user_shift = int(input("Type the shift number: "))
        result = encode(user_message, user_shift)
        return print(f"Here is your encoded result: {result}")
        
start()

