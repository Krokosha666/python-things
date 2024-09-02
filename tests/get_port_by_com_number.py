import serial.tools.list_ports

def get_port_info_by_name(port_name):
    ports = list(serial.tools.list_ports.comports())
    
    for port in ports:
        if port.device == port_name:
            return port
    
    # If the specified port name is not found
    return None

# Example usage
com_port_name = input()
port_info = get_port_info_by_name(com_port_name)

if port_info:
    print("Port Found:")
    print(f"Device: {port_info.device}")
    print(f"Description: {port_info.description}")
    print(f"Hardware ID: {port_info.hwid}")
    print(f"Location: {port_info.location}")
    print(f"Manufacturer: {port_info.manufacturer}")
    print(f"Product: {port_info.product}")
    print(f"Serial Number: {port_info.serial_number}")
    print(f"VID:PID: {port_info.vid}:{port_info.pid}")
else:
    print(f"Port '{com_port_name}' not found.")