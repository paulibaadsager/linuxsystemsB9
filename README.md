# linuxsystemsB9
Gruppearbejde

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

# Log af leg med hs100.sh findes her
View the recording at:

    https://asciinema.org/a/YleGF8GHOaxxGPhQzm8PqjUoy?speed=1.8
