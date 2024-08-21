from pyrs.hmp2030 import HMP2030

address = 'USB0::0x0AAD::0x0117::120470::INSTR'


def main():
    device = HMP2030(address)
    device.beep()

    print("----------------------------------------------------------------------------------------------------------")
    print(f"device identity  : {device.identity}")
    print("----------------------------------------------------------------------------------------------------------")
    for channel in range(1, 4):
        device.channel = channel
        print(f"device channel   : {device.channel}")
        device.output = 'OFF'


if __name__ == '__main__':
    main()
