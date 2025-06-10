# LAN-Scan

Simple Python script to scan local networks for IPs, MAC addresses, and resolve MAC vendors.

## Setup

```
git clone https://github.com/josias-qr25/lan-scan.git
cd lan-scan
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage Linux/MacOS

```
sudo python lan-scan.py
```

## Usage Windows
Run terminal as administrator.
```
python lan-scan.py
```

Root privilege is required on most systems to send ARP requests.


