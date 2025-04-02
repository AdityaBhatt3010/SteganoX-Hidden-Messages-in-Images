import argparse
from utilities import encode_image, decode_image, stylish_heading

def main():
    stylish_heading()
    parser = argparse.ArgumentParser(description="SteganoX: Hide and Extract Messages in Images")
    parser.add_argument("-e", "--encode", nargs=3, metavar=("image_path", "secret_message", "output_image_path"),
                        help="Encode a message into an image. Usage: python SteganoX.py -e image_path secret_message output_image_path")
    parser.add_argument("-d", "--decode", metavar="image_path", help="Decode a message from an image. Usage: python SteganoX.py -d image_path")
    
    args = parser.parse_args()
    
    if args.encode:
        image_path, secret_message, output_image_path = args.encode
        encode_image(image_path, secret_message, output_image_path)
    elif args.decode:
        decode_image(args.decode)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
