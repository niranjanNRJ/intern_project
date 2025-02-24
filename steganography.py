import cv2
import base64
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image, ImageTk

# Function to encrypt and encode the message using Base64
def encrypt_message(msg, password):
    encrypted = "".join(chr(ord(c) ^ ord(password[i % len(password)])) for i, c in enumerate(msg))
    return base64.b64encode(encrypted.encode()).decode()  # Base64 encoding

# Function to decode and decrypt the message
def decrypt_message(encrypted_msg, password):
    try:
        decoded = base64.b64decode(encrypted_msg.encode()).decode()
        decrypted = "".join(chr(ord(c) ^ ord(password[i % len(password)])) for i, c in enumerate(decoded))

        # Check if decryption is successful by verifying the "$END$" marker
        if decrypted.endswith("$END$"):
            return decrypted.replace("$END$", "")  # Return message without "$END$"
        else:
            return None  # Return None if the password is incorrect
    except Exception:
        return None  # Return None if decryption fails



# Function to encode the message into an image
def encode_message():
    global img_path
    if not img_path:
        messagebox.showerror("Error", "Please select an image first.")
        return

    msg = simpledialog.askstring("Input", "Enter secret message:")
    password = simpledialog.askstring("Input", "Enter passcode:", show="*")

    if not msg or not password:
        messagebox.showerror("Error", "Message and password cannot be empty!")
        return

    encrypted_msg = encrypt_message(msg + "$END$", password)  # Append termination marker

    img = cv2.imread(img_path)
    n, m = 0, 0

    for char in encrypted_msg:
        img[n, m, 0] = ord(char)  # Store in Blue channel only
        m += 1
        if m >= img.shape[1]:  
            m = 0
            n += 1

    encoded_path = "encoded_image.png"
    cv2.imwrite(encoded_path, img)
    messagebox.showinfo("Success", f"Message hidden in {encoded_path}")

# Function to decode the message from an image
def decode_message():
    global img_path
    if not img_path:
        messagebox.showerror("Error", "Please select an encrypted image.")
        return

    password = simpledialog.askstring("Input", "Enter passcode:", show="*")

    if not password:
        messagebox.showerror("Error", "Passcode cannot be empty!")
        return

    img = cv2.imread(img_path)
    n, m = 0, 0
    extracted_encrypted_msg = ""

    while True:
        char_val = img[n, m, 0]
        if char_val == 0:
            break  # Stop at empty pixel

        extracted_encrypted_msg += chr(char_val)
        m += 1
        if m >= img.shape[1]:  
            m = 0
            n += 1

        if extracted_encrypted_msg.endswith("$END$"):  # Stop at termination marker
            extracted_encrypted_msg = extracted_encrypted_msg.replace("$END$", "")
            break

    decrypted_msg = decrypt_message(extracted_encrypted_msg, password)

    if decrypted_msg:
        messagebox.showinfo("Decryption Successful", f"Hidden Message: {decrypted_msg}")
    else:
        messagebox.showerror("Error", "Incorrect passcode! Decryption failed.")

# Function to select an image
def select_image():
    global img_path
    img_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if img_path:
        img = Image.open(img_path)
        img = img.resize((200, 200))
        img_tk = ImageTk.PhotoImage(img)
        label_image.config(image=img_tk)
        label_image.image = img_tk

# GUI Setup
root = tk.Tk()
root.title("Image Steganography")
root.geometry("400x500")

img_path = None

tk.Label(root, text="*** Image Steganography ***", font=("Arial", 14, "bold")).pack(pady=10)
tk.Button(root, text="Select Image", command=select_image).pack(pady=5)
label_image = tk.Label(root)
label_image.pack()

tk.Button(root, text="Encode Message", command=encode_message).pack(pady=10)
tk.Button(root, text="Decode Message", command=decode_message).pack(pady=10)

root.mainloop()
