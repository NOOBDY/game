Write-Output "Loading..."

if (!(Test-Path .\env)) {
    Write-Output "Installing Dependencies..."
    python.exe -m venv env
    .\env\Scripts\activate
    pip.exe install -r .\requirements.txt    
}
else {
    .\env\Scripts\activate
}

python.exe .\main.py

deactivate