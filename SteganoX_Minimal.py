from utilities import encode_image, decode_image

def main():
    choice = input("Enter 'e' to encode or 'd' to decode: ").strip().lower()
    
    if choice == 'e':
        image_path = input("Enter image path: ")
        secret_message = input("Enter the message to hide: ")
        output_image_path = input("Enter output image path: ")
        encode_image(image_path, secret_message, output_image_path)
    elif choice == 'd':
        image_path = input("Enter image path to decode: ")
        decode_image(image_path)
    else:
        print("Invalid choice! Please enter 'e' for encode or 'd' for decode.")

if __name__ == "__main__":
    main()
