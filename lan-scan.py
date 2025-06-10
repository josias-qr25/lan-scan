from scapy.all import ARP, Ether, srp
import json
from datetime import datetime

# CREATE ARP REQUEST PACKET
arp = ARP(pdst="192.168.1.0/24")
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether / arp

# CREATE FILENAME USING DATETIME
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"scan-results-{timestamp}.txt"

# SEND ARP REQUEST PACKET
print("Sending ARP requests...")
result = srp(packet, timeout=3, verbose=0)[0]
print(f"Received {len(result)} responses")

# DEVICE LIST
devices = []
for sent , received in result:
    vendor = "Unknown"
    try:
        vendor = mac_lookup.lookup(received.hwsrc)
    except Exception:
        pass

    device.append({
        'ip': received.psrc, 
        'mac': received.hwsrc, 
        'vendor': vendor
    })

# DISPLAY IP AND MAC IN TERMINAL
print("Available devices on the network:")
for device in devices:
    print(f"{device['ip']:20} {device['mac']:20}")

# SAVE LIST AS FILE
while True:
    ans = input("Save to file? [Y/N] ").lower()
    if ans == "y":
        with open(filename, "w") as f:
            json.dump(devices, f, indent=4)
        print(f"Results saved to {filename}.")
        print("Thanks for using lan-scan. Have a nice day!")
        break
    elif ans =="n":
        print("Thanks for using lan-scan. Have a nice day!")
        break
    else:
        print("Option unavailable. Please enter [Y] or [N].")
