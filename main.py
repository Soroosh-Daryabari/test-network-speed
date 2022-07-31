from psutil import net_if_addrs
from tabulate import tabulate
from speedtest import Speedtest


class NetworkSpeed(object):
    def __init__(self):
        self.tester = net_if_addrs()
        self.speed = Speedtest()
        self.interface = self.interfaces()[0]
        self.speed_of_download = self.speed.download()
        self.speed_of_upload = self.speed.upload()

    def __str__(self):
        data = {
            "Interface": [self.interface],
            "Download": [str(self.speed_of_download) + "Mbps"],
            "Upload": [str(self.speed_of_upload) + "Mbps"]
        }
        result = tabulate(data, headers="keys", tablefmt="pretty")
        return result

    def interfaces(self):
        interfaces = list()
        for key, value in self.tester.items():
            interfaces.append(key)
        return interfaces


if __name__ == "__main__":
    print(NetworkSpeed())
