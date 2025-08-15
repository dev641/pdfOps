param(
    [Parameter(Mandatory=$true)][string]$PfxPath,
    [Parameter(Mandatory=$true)][string]$OldPassword,
    [Parameter(Mandatory=$true)][string]$NewPassword
)

# Validate if file exists
if (-not (Test-Path $PfxPath)) {
    Write-Error "PFX file '$PfxPath' does not exist."; exit 1
}

# Ask before overwrite
$confirm = Read-Host "This will overwrite '$PfxPath'. Continue? (y/n)"
if ($confirm -ne 'y' -and $confirm -ne 'Y') { Write-Host "Aborted."; exit }

$tempPath = "$PfxPath.temp"

# Load old PFX
$cert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2
$cert.Import($PfxPath, $OldPassword, 'Exportable,PersistKeySet')

# Export to temp with new password
$secureNewPass = ConvertTo-SecureString $NewPassword -AsPlainText -Force
Export-PfxCertificate -Cert $cert -FilePath $tempPath -Password $secureNewPass

# Delete old and replace
Remove-Item $PfxPath -Force
Rename-Item $tempPath $PfxPath

Write-Host "Updated PFX password and retained original filename: $PfxPath"


powershell -ExecutionPolicy Bypass -File "C:\Users\Devas\Personal-Development\Projects\PdfOps\installer\scripts\reset_password.ps1" `
    -PfxPath "C:\WINDOWS\system32\PdfOps.pfx" `
    -OldPassword "PFX_PASSWORD" `
    -NewPassword "admin@123"
