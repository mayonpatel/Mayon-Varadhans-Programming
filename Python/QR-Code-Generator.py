# QR Code Generator
# Programmed by Mayon & Varadhan
# GitHub: https://github.com/mayonpatel/Mayon-Varadhans-Programming
# You may need to download the qrcode library to use this.
# You may also need to download Pillow.

import qrcode

# Prompt user
domain = input("What URL would you like to use in the QR code?: ")
filename = input("What should the file name for the QR code be?")

def make_qr(data, filename="qrcode.png"):
    """Generates a QR code image from the given data."""
    # Configure the QR code parameters
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # Add your data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create the image using Pillow
    img = qr.make_image(fill_color="black", back_color="white")
    # Save the generated image to a file
    img.save(filename)

# Generate the QR code using the user's input
make_qr(domain, f"{filename}.png")
print(f"QR code generated with URL: {domain} and saved as {filename}.png")
input("Press enter to close terminal.")
