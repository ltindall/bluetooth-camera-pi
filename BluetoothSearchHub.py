# simple inquiry example
import bluetooth


class BluetoothSearchHub: 



    def __init__(self): 
        self.discovered_devices = []

    def start_bluetooth_scan(self): 
        self.discovered_devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True)

    def ping_addresses(self): 
        new_device_list = []
        for device in self.discovered_devices: 
            name = bluetooth.lookup_name(device[0], timeout=5)
            if name == device[1]: 
                new_device_list.append(device)
        self.discovered_devices = new_device_list


    def check_devices(self): 
        self.ping_addresses()



if __name__ == "__main__":
        bluetoothSearcher = BluetoothSearchHub()
        bluetoothSearcher.start_bluetooth_scan()
        print 'found devices = ',bluetoothSearcher.discovered_devices
        bluetoothSearcher.check_devices()

        print 'found new devices = ',bluetoothSearcher.discovered_devices
                
