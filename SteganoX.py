from PIL import Image

# Function to encode text into an image
def encode_image(image_path, secret_message, output_image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    
    # Convert text to binary
    binary_message = ''.join(format(ord(i), '08b') for i in secret_message) + '1111111111111110'
    
    data = list(img.getdata())
    new_data = []
    data_index = 0
    bit_index = 0
    
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

if __name__ == "__main__":
    choice = input("Enter 'e' to encode or 'd' to decode: ")
    
    if choice.lower() == 'e':
        image_path = input("Enter image path: ")
        secret_message = input("Enter the message to hide: ")
        output_image_path = input("Enter output image path: ")
        encode_image(image_path, secret_message, output_image_path)
    elif choice.lower() == 'd':
        image_path = input("Enter image path to decode: ")
        decode_image(image_path)
    else:
        print("Invalid choice!")
