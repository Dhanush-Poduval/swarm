import bluetooth

addr = "00:16:53:0C:14:E0"

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

print("Connecting...")
sock.connect((addr, 1))
print("Connected!")
print(sock)
pkt = bytes([0x01, 0x88])
tx = len(pkt).to_bytes(2, "little") + pkt

print("Sending:", tx.hex(" "))

sock.send(tx)

print("Sent!")
