import serial.tools.list_ports

def print_com_ports_info():
    com_ports = list(serial.tools.list_ports.comports())

    if not com_ports:
        print("No COM ports found.")
        return

    print("Available COM ports:")
    for port in com_ports:
        print(f"Port: {port.device}")
        print(f"Description: {port.description}")
        print(f"HWID: {port.hwid}")
        print(f"Location: {port.location}")
        print(f"Manufacturer: {port.manufacturer}")
        print(f"Product: {port.product}")
        print(f"Serial Number: {port.serial_number}")
        
        if port.vid is not None and port.pid is not None:
            print(f"VID:PID: {port.vid:04x}:{port.pid:04x}")
        else:
            print("VID:PID: Not available")

        print(f"USB Info: {port.usb_info()}")
        print("------")

if __name__ == "__main__":
    print_com_ports_info()
