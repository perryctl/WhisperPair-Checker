import asyncio
from bleak import BleakScanner, BleakClient
from datetime import datetime

# Google Fast Pair Service UUID (16-bit: 0xFE2C)
FAST_PAIR_UUID = "0000fe2c-0000-1000-8000-00805f9b34fb"

# Store discovered devices
seen_devices = {}

def detection_callback(device, advertisement_data):    
    # Observe BLE advertisements. No interaction/pairing/connection.
    
    uuids = advertisement_data.service_uuids or []

    if FAST_PAIR_UUID.lower() in [u.lower() for u in uuids]:
        if device.address not in seen_devices:
            seen_devices[device.address] = device.name
            print("\n[!] Fast Pair advertisement detected")
            print(f"    Time: {datetime.now()}")
            print(f"    Name: {device.name}")
            print(f"    MAC:  {device.address}")
            print(f"    RSSI: {advertisement_data.rssi}")

async def passive_scan(duration=30):
    # Scan for BLE devices passively without interaction.
    print("[*] Starting PASSIVE BLE scan")
    scanner = BleakScanner(detection_callback)
    await scanner.start()
    await asyncio.sleep(duration)
    await scanner.stop()
    print("[*] Scan complete")

async def main():
    await passive_scan()

    print("\n[*] Summary of Fast Pair devices:")
    if not seen_devices:
        print("    No Fast Pair advertisements observed.")
        return
    
    print("*** Vulnerable devices detected! ***")
    for addr, name in enumerate(seen_devices.items(), start=1):
        print(f"device found: - {name} ({addr})")
        # await unauthorized_pairing(addr)
    

if __name__ == "__main__":
    asyncio.run(main())
