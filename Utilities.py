from PIL import Image
from pyfiglet import figlet_format
from termcolor import colored

# Stylish heading function
def stylish_heading():
    a = figlet_format("SteganoX", font="starwars", width=1000)
    print(colored(a, "green"))

# Function to encode text into an image
def encode_image(image_path, secret_message, output_image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    
    # Convert text to binary
    binary_message = ''.join(format(ord(i), '08b') for i in secret_message) + '1111111111111110'
    
    data = list(img.getdata())
    new_data = []
    data_index = 0
    
    for pixel in data:
        if data_index < len(binary_message):
            new_pixel = list(pixel)
            for i in range(3):  # Modify R, G, B values
                if data_index < len(binary_message):
                    new_pixel[i] = new_pixel[i] & ~1 | int(binary_message[data_index])
                    data_index += 1
            new_data.append(tuple(new_pixel))
        else:
            new_data.append(pixel)
    
    img.putdata(new_data)
    img.save(output_image_path, format='PNG')
    print(f"Message encoded and saved in {output_image_path}")

# Function to decode text from an image
def decode_image(image_path):
    img = Image.open(image_path)
    data = list(img.getdata())
    
    binary_message = ""
    for pixel in data:
        for i in range(3):  # Extract bits from R, G, B values
            binary_message += str(pixel[i] & 1)
    
    # Convert binary message to text
    chars = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    message = ""
    for char in chars:
        if char == '1111111111111110':
            break
        message += chr(int(char, 2))
    
    print(f"Decoded message: {message}")
    return message
