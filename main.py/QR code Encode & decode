import qrcode

def generate_qr_code(data, filename):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(filename)
    print(f"QR Code generated and saved as {filename}")

if __name__ == "__main__":
    data = input("Enter the data (text or URL) to encode in the QR code: ")
    filename = input("Enter the filename to save the QR code (e.g., qrcode.png): ")
    generate_qr_code(data, filename)
