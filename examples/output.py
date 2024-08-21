"""
example on output sub-command
"""
from pyrs.hmp2030 import HMP2030


def main():
    """
    main procedure
    :return:
    """
    device = HMP2030('USB0::0x0AAD::0x0117::120470::INSTR')
    device.beep()
    print("----------------------------------------------------------------------------------------------------------")
    print(f"device identity  : {device.identity}")
    print("----------------------------------------------------------------------------------------------------------")
    for channel in range(1, 4):
        device.channel = channel
        print("-----------------------------------------------------------------------------------------------------")
        print(f"-> output subsystem...channel={device.channel}")
        print("-----------------------------------------------------------------------------------------------------")
        device.output = 'ON'
        print(f"output state    : {device.output}")
        device.output = 'OFF'
        print(f"output state    : {device.output}")


if __name__ == '__main__':
    main()
