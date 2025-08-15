# 📦 PdfOps – Build & Create Trusted Installer

This document explains how to **build the PdfOps executable** from Python code and create a **digitally signed installer** using **Inno Setup**.

---

## 1️⃣ Build the EXE with PyInstaller

Make sure you have Python 3.11+ installed and **PyInstaller**:

```bash
pip install pyinstaller
```

Run the following command to generate a single-file executable:

```bash
pyinstaller --onefile --windowed --name "PdfOps" --icon "C:\path\to\pdfOps.ico" app.py
```

- `--onefile` → Packs everything into one EXE

- `--windowed` → No console window (for GUI apps)

- `--name` → Name of the output EXE

- `--icon` → Path to your .ico file for the EXE icon

The compiled EXE will be in the dist folder.

## 2️⃣ Generate a Self-Signed Certificate (Optional for Testing)

If you don't already have a code signing certificate, you can create one locally for testing:

```powershell
# Generate PFX (private + public key) and CER (public only)
$cert = New-SelfSignedCertificate `
  -Type CodeSigningCert `
  -Subject "CN=PdfOps" `
  -CertStoreLocation Cert:\CurrentUser\My

$pwd = ConvertTo-SecureString -String "YourPfxPassword" -Force -AsPlainText

Export-PfxCertificate -Cert $cert -FilePath "mycodesign.pfx" -Password $pwd
Export-Certificate -Cert $cert -FilePath "mycodesign.cer"
```

- `.pfx` → Used for signing EXE/Installer

- `.cer` → Used to install the certificate on other machines so it’s trusted

- Replace `"CN=PdfOps"` with your desired subject name.
Replace `"YourPfxPassword"` with your desired password.

- Replace `"mycodesign.pfx"` and `"mycodesign.cer"` with your output

## 3️⃣ Install Certificate Locally (Trusted Publisher + Root)

Run this PowerShell script as Administrator:

```powershell
certutil.exe -addstore "Root" mycodesign.cer
certutil.exe -addstore "TrustedPublisher" mycodesign.cer
```

## 4️⃣ Prepare Inno Setup Script

Install Inno Setup from:
👉 <https://jrsoftware.org/isinfo.php>

You can find `.iss` script for this project here.
 > installer\pdfOpsInstaller.iss

## 5️⃣ Install Certificate Automatically at Setup

You can find `install_certs.ps1` at this location:

> installer\scripts\install_cert.ps1

## 6️⃣ Build the Installer

- Open the Inno Installer Application
- load the `pdfOpsInstaller.iss` into Inno Setup.
- Click "Build" to create the installer.