if (!(Test-Path .\env)) {
    python.exe -m venv env
    .\env\Scripts\activate
    pip.exe install -r .\requirements.txt    
}
else {
    .\env\Scripts\activate
}

python.exe .\main.py

deactivate