# 📄 PdfOps

**pdfOps** is a desktop-based **PDF utility application** built with [PySide6](https://doc.qt.io/qtforpython/) for managing and processing PDF files quickly and efficiently.  
It is designed for print shops, small businesses, and individuals who frequently handle PDF files and need tools like sorting, merging, cost calculation, and bill generation.

---

## ✨ Features

- **Drag & Drop Support**
  - Choose between dragging **folders** or **files** into the application.
  - Only `.pdf` files are accepted — other formats are silently ignored.
  - *(Upcoming)* Seamless drag & drop without having to choose file/folder type first.

- **File Browser Support**
  - Select PDF files or folders using a `QFileDialog` interface.

- **PDF Information View**
  - Displays PDF **name** and **page count**.
  - Remove unwanted PDFs from the list with a close button.

- **Sorting**
  - Sort PDFs by **name** or **page count**.

- **Print Cost Calculation**
  - Choose from predefined rates (e.g., `0.4`, `0.5`, `0.7`, `0.9`).
  - Automatically calculates total print cost based on page count.

- **Merging PDFs**
  - Merge selected PDFs from the list into a single PDF file.

- **Bill Generation**
  - Create a **PDF bill** that can be sent to customers or used by shopkeepers.

---

## 🖥️ How to Use

1. **Start the Application**
   - Run the `pdfOps` executable or launch via Python script.
   
2. **Load PDFs**
   - Option 1: **Drag & Drop**
     - Select whether you want to drag **files** or **folders**.
     - Drag `.pdf` files or folders containing PDFs into the app window.
   - Option 2: **File Dialog**
     - Click "Browse" and choose your PDFs or a folder containing them.

3. **View & Manage PDFs**
   - Check the displayed PDF list with **names** and **page counts**.
   - Remove unwanted files using the close button.
   - Sort by **name** or **page count** as needed.

4. **Set Print Rate**
   - Select a rate from the dropdown (e.g., `0.4`, `0.5`, etc.).
   - The application will automatically calculate the total cost.

5. **Merge PDFs**
   - Merge the loaded PDFs into a single document.

6. **Generate Bill**
   - Export a **PDF bill** for printing or sending to clients.

---

## 📦 Installation

Please refer to the detailed **[Setup Guide](Setup.md)** for installation instructions.

---

## 📷 Screenshots

<img src="images\preview\MainScreen.png" alt="MainScreen" />

<img src="images\preview\PDF_LIST_PREVIEW.png" alt="PDFList" />

---

## 📜 License

This project is licensed under the [MIT License](License) © 2025 Dev Ashish

---

## 💡 Roadmap

- Remove file/folder selection restriction for seamless drag & drop.
- Add more flexible rate customization.
- Include PDF splitting functionality.
- Multi-language support.

---

**Developed with ❤️ using PySide6**
