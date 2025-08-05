param (
    [string]$cerPath
)

Write-Host "Checking if certificate is already installed..."

# Load certificate from file
$cert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2
$cert.Import($cerPath)
$thumb = $cert.Thumbprint.ToUpper()

function Test-CertExist($storeName, $thumb) {
    $store = New-Object System.Security.Cryptography.X509Certificates.X509Store($storeName, 'LocalMachine')
    $store.Open('ReadOnly')
    $exists = $store.Certificates | Where-Object { $_.Thumbprint.ToUpper() -eq $thumb }
    $store.Close()
    return $exists
}

$needRoot      = -not (Test-CertExist 'Root' $thumb)
$needPublisher = -not (Test-CertExist 'TrustedPublisher' $thumb)

if (-not $needRoot -and -not $needPublisher) {
    Write-Host "Certificate is already installed. Skipping."
} else {
    if ($needRoot) {
        Write-Host "Installing into Trusted Root..."
        certutil.exe -addstore "Root" $cerPath
    }
    if ($needPublisher) {
        Write-Host "Installing into Trusted Publisher..."
        certutil.exe -addstore "TrustedPublisher" $cerPath
    }
}
