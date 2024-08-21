from pyrs.hmp2030 import HMP2030

address = 'USB0::0x0AAD::0x0117::120470::INSTR'


def main():
    device = HMP2030(address)
    device.beep()

    print("----------------------------------------------------------------------------------------------------------")
    print(f"device identity  : {device.identity}")
    print("----------------------------------------------------------------------------------------------------------")
    for channel in [1, 2, 3]:
        device.channel = channel
        print("-----------------------------------------------------------------------------------------------------")
        print(f"-> measure subsystem...channel={device.channel}")
        print("-----------------------------------------------------------------------------------------------------")
        print(f"current          : {device.measure_current}")
        print(f"voltage          : {device.measure_voltage}")


if __name__ == '__main__':
    main()
