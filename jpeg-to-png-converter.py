import os
from PIL import Image

def convert_jpeg_to_png(input_path, output_path):
    try:
        # Open the JPEG image
        with Image.open(input_path) as img:
            # Save the image in PNG format
            img.save(output_path, 'PNG')
        print(f"Successfully converted {input_path} to {output_path}")
        return True
    except Exception as e:
        print(f"Error during conversion: {str(e)}")
        return False

def troubleshoot_conversion(input_path):
    print("Troubleshooting conversion...")
    try:
        # Attempt to open the image to check if it's a valid JPEG
        with Image.open(input_path) as img:
            print(f"Image format: {img.format}")
            print(f"Image mode: {img.mode}")
            print(f"Image size: {img.size}")
        print("The image appears to be valid. The issue may be with writing the output file.")
    except Exception as e:
        print(f"Error opening the image: {str(e)}")
        print("The input file may be corrupted or not a valid JPEG image.")

def main():
    print("JPEG to PNG Converter")
    
    # Get input file path
    input_path = input("Enter the path to the JPEG file: ")
    
    # Check if file exists
    if not os.path.exists(input_path):
        print("Error: The specified file does not exist.")
        return
    
    # Get output file path
    output_path = input("Enter the path for the output PNG file: ")
    
    # Perform conversion
    success = convert_jpeg_to_png(input_path, output_path)
    
    if not success:
        troubleshoot_conversion(input_path)
    else:
        print("Conversion completed successfully.")

if __name__ == "__main__":
    main()
