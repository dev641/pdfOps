#define MyAppName "pdfOps"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "Romika Rani"
#define MyAppURL ""
#define MyAppExeName "pdfOps.exe"

[Setup]
AppId={{4043E972-8A6B-4720-B81B-2DF5A6FEBEEF}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={commonpf}\{#MyAppName}
OutputDir=.
OutputBaseFilename={#MyAppName}_Installer
Compression=lzma
SolidCompression=yes
SignTool=signtool

[Files]
Source: "C:\Users\Devas\Personal-Development\Projects\PdfOps\dist\PdfOps.exe";         DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Devas\Personal-Development\Projects\PdfOps\certs\pdfOps.cer";    DestDir: "{tmp}"; Flags: ignoreversion
Source: "C:\Users\Devas\Personal-Development\Projects\PdfOps\installer\scripts\install_cert.ps1"; DestDir: "{tmp}"; Flags: ignoreversion

[Run]
Filename: "powershell.exe"; \
  Parameters: "-ExecutionPolicy Bypass -File ""{tmp}\install_cert.ps1"" -cerPath ""{tmp}\pdfOps.cer"""; \
  Flags: runhidden waituntilterminated

Filename: "{app}\pdfOps.exe"; Description: "Launch pdfOps"; Flags: postinstall nowait

[Icons]
Name: "{commondesktop}\pdfOps"; Filename: "{app}\pdfOps.exe"
