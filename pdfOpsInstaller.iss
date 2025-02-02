[Setup]
AppName=PdfOps
AppVersion=1.0
DefaultDirName={pf}\PdfOps
DefaultGroupName=PdfOps
OutputDir=dist
OutputBaseFilename=PdfOpsInstaller
SetupIconFile=images\pdfOps.ico
UninstallDisplayIcon={app}\PdfOps.exe
Compression=lzma2
SolidCompression=yes

[Files]
Source: "dist\PdfOps.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\PdfOps"; Filename: "{app}\PdfOps.exe"

[Tasks]
Name: "desktopicon"; Description: "Create a desktop icon"; GroupDescription: "Additional icons:"; Flags: unchecked

[Code]
procedure InitializeWizard;
begin
  MsgBox('Welcome to PdfOps Setup! Click OK to install.', mbInformation, MB_OK);
end;
