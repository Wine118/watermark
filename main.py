import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image, ImageFont, ImageDraw
import os

# Function to open a file dialog and select an image
def select_image():
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")]
    )
    return file_path

# Function to save the watermarked image
def save_image(image):
    save_path = filedialog.asksaveasfilename(
        title="Save Image As",
        defaultextension=".jpg",
        filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("BMP files", "*.bmp")]
    )
    if save_path:
        image.save(save_path)
        messagebox.showinfo("Success", f"Watermarked image saved as '{os.path.basename(save_path)}'")

# Function to add a watermark to the selected image
def add_watermark(watermark_text):
    file_path = select_image()
    if not file_path:
        return

    # Open the original image
    image = Image.open(file_path)

    # Create a copy of the image for watermarking
    watermark_image = image.copy()

    # Create a drawing object
    draw = ImageDraw.Draw(watermark_image)

    # Get the dimensions of the image
    w, h = image.size
    x, y = int(w / 2), int(h / 2)

    # Determine the font size
    font_size = min(x, y)

    # Load the font and set the size
    font = ImageFont.truetype("arial.ttf", int(font_size / 6))

    # Add the slightly grey watermark text
    draw.text((x, y), watermark_text, fill=(200, 160, 255), font=font, anchor='ms')

    # Save the watermarked image in a user-selected folder
    save_image(watermark_image)

# Main code
if __name__ == "__main__":
    # Create the main Tkinter window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Ask the user for the watermark text
    watermark_text = simpledialog.askstring("Input", "Enter the watermark text:")

    if watermark_text:
        # Run the watermark function with the entered text
        add_watermark(watermark_text)
