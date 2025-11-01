"""
Hands-On Assignment 2: AI QR Code Generator
Course: MSCS-633-B01 - Advanced Artificial Intelligence
Author: Ian A.
Date: 11/02/2025

Description:
This program generates a QR code from a user-provided URL using Python's qrcode library.
It displays and saves the generated QR code image.
"""

import qrcode

def generate_qr(url):
    """Generates and saves a QR code for the given URL."""
    # Create a QR Code object
    qr = qrcode.QRCode(
        version=1,  # controls the size (1 = smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # 7% error correction
        box_size=10,  # pixel size of each box
        border=4,  # thickness of the border (default = 4)
    )

    # Add data (the URL)
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR Code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save and display
    img.save("generated_qr.png")
    img.show()
    print("✅ QR Code generated successfully and saved as 'generated_qr.png'")

if __name__ == "__main__":
    print("=== AI QR Code Generator ===")
    user_url = input("Enter the URL to generate QR code: ").strip()
    if user_url:
        generate_qr(user_url)
    else:
        print("⚠️ No URL entered. Exiting...")
