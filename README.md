# linuxsystemsB9
Gruppearbejde

## Python, flask og python-kasa
Information om python-kasa findes her: <https://python-kasa.readthedocs.io/en/latest/smartplug.html>

python-kasa kan "snakke" med TP-plug. Python-kasa kræver python3.8. Installer python3.8 vha.
```
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
```
Lav virtuelt python environment med og gå ind i det.
``` 
virtualenv -p /usr/bin/python3.8 venv
python3.8 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
``` 
Start service med `python app.pyi`. Tjek at den svare ved at skrive `curl -X POST localhost:5000/deactivate`.

# Nedenstående er gammelt og skal nok droppes...
## Om filerne
Bash-scriptet hs100/hs100.sh tager parametre som 'on', 'off', 'check', 'emeter' og 'status'.

Filen pluginfo.txt indeholder alle de informationer om plugs som kan findes med scriptet hs100.sh.
Bash-scriptet updateJSON.sh bruges til at opdatere filen pluginfo.txt, ved at køre hs100.sh flere gange.
Bash-scriptet simple_plug_check.sh bruges ikke længere (det var test).
Filen plugIPlist.txt er en midlertidig fil. Den findes fordi jeg ikke er dygtig nok til bash.

## Struktur
```
.
├── hs100
│   ├── hosts
│   ├── hs100.sh
│   ├── myip.sh
│   ├── README.md
│   └── systemd
│       ├── hs100@.service
│       └── hs100@.timer
├── pluginfo.txt
├── plugIPlist.txt
├── README.md
├── simple_plug_check.sh
└── updateJSON.sh
```

# Docker
Docker image til at køre en json-server. Skriv fx.
`$ sudo docker run -p 8080:80 -v /home/pauli/linuxsystemsB9/testdb.json:/data/db.json clue/json-server`

# Log af leg med hs100.sh findes her
View the recording at:

    https://asciinema.org/a/YleGF8GHOaxxGPhQzm8PqjUoy?speed=1.8
