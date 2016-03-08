mport subprocess

for ping in range(1,10):
    address = "192.168.31." + str(ping)
    res = subprocess.call(['ping', '-c', '1', address])
    if res == 0:
        print("ping to", address, "acık")
    elif res == 2:
        print("no response from", address)
    else:
        print("ping to", address, "kapalı!")import subprocess

