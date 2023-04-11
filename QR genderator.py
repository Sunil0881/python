import qrcode

# Create QR code instance.
qr = qrcode.QRCode(
    version=1,  # QR code version.
    box_size=10,  # Size of each box in the QR code.
    border=5  # Number of boxes to use for the border.
)

# Data to encode in the QR code
data = "https://www.example.com"

# Add data to QR code
qr.add_data(data)

# Generate QR code as an image
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
img.save("example_qr_code.png")
