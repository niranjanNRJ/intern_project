# Image Steganography Using OpenCV

---

## 📌 Project Overview
This project implements **Image Steganography** using Python and OpenCV, allowing users to hide and retrieve messages within an image securely. A graphical user interface (GUI) built with Tkinter provides an easy-to-use experience.

---

## 🏆 Features
- **GUI-based Encoding & Decoding**: User-friendly interface for embedding and extracting secret messages.
- **Passcode Protection**: Ensures only authorized users can access the hidden message.
- **Secure Communication**: Messages are embedded within image pixels, making them undetectable to the naked eye.
- **Error Handling**: Ensures incorrect passwords do not reveal messages.
- **Maintains Image Integrity**: The original image is visually unaffected after encoding.

---

## 🛠️ Technologies Used
- **Programming Language**: Python  
- **Libraries**: OpenCV, Tkinter, PIL (Pillow)  
- **IDE**: Visual Studio Code  
- **Platform**: Windows/Linux

---

## 📂 Project Structure
```
📦 Image Steganography
 ┣ 📜 steganography.py  # Main Python script with GUI
 ┣ 📜 requirements.txt  # Dependencies
 ┣ 📜 README.md         # Project documentation
 ┗ 📂 images/           # Folder to store input/output images
```

---

## 🚀 How to Run
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/image-steganography.git
   cd image-steganography
   ```
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Application**
   ```bash
   python steganography.py
   ```

---

## 🔮 Future Scope
- Implement **Least Significant Bit (LSB)** technique for improved security.
- Add **encryption algorithms** for enhanced message protection.
- Support multiple image formats and **larger file handling**.

---

## 🔗 GitHub Repository
[GitHub Link](https://github.com/yourusername/image-steganography)

---
