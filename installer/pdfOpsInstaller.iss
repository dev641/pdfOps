#define MyAppName "PdfOps"
#define MyAppVersion "1.1.0"
#define MyAppPublisher "Romika Rani"
#define MyAppURL ""
#define MyAppExeName "PdfOps.exe"

[Setup]
AppId={{4043E972-8A6B-4720-B81B-2DF5A6FEBEEF}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={commonpf}\{#MyAppName}
OutputDir=.
OutputBaseFilename={#MyAppName}Installer
Compression=lzma
SolidCompression=yes
SignTool=signtool
SetupIconFile="C:\Users\Devas\Personal-Development\Projects\PdfOps\images\PdfOps.ico"

[Files]
Source: "C:\Users\Devas\Personal-Development\Projects\PdfOps\dist\PdfOps.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Devas\Personal-Development\Projects\PdfOps\certs\PdfOps.cer"; DestDir: "{tmp}"; Flags: ignoreversion
Source: "C:\Users\Devas\Personal-Development\Projects\PdfOps\installer\scripts\install_cert.ps1"; DestDir: "{tmp}"; Flags: ignoreversion
Source: "C:\Users\Devas\Personal-Development\Projects\PdfOps\images\PdfOps.ico"; DestDir: "{app}"; Flags: ignoreversion

[Run]
Filename: "powershell.exe"; \
  Parameters: "-ExecutionPolicy Bypass -File ""{tmp}\install_cert.ps1"" -cerPath ""{tmp}\PdfOps.cer"""; \
  Flags: runhidden waituntilterminated

Filename: "{app}\PdfOps.exe"; Description: "Launch PdfOps"; Flags: postinstall nowait

[Icons]
Name: "{commondesktop}\\PdfOps"; Filename: "{app}\\PdfOps.exe"; IconFilename: "{app}\\Pdfops.ico"
Name: "{group}\\PdfOps"; Filename: "{app}\\PdfOps.exe"; IconFilename: "{app}\\Pdfops.ico"

[UninstallDelete]
Type: files; Name: "{commondesktop}\\PdfOps.lnk"
Type: files; Name: "{group}\\PdfOps.lnk"
Type: files; Name: "{app}\\PdfOps.exe"
