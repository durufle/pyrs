"""
Example on output domain
"""
import argparse
import pyvisa.errors
from pyrs.hmp2030 import HMP2030

NAME = 'USB0::0x0AAD::0x0117::120470::INSTR'
LIBRARY = '/usr/lib/librsvisa.so'


def main():
    """
    main procedure

    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', default=NAME, help=f'device visa name or address. default = {NAME}')
    parser.add_argument('-l', '--library', default=LIBRARY, help=f'visa shared library. default = {LIBRARY}')
    args = parser.parse_args()

    try:
        device = HMP2030(name=args.name,library=args.library)
        device.beep()
        print("-------------------------------------------------------------------------------------------------------")
        print(f"device identity  : {device.identity}")
        print("-------------------------------------------------------------------------------------------------------")
        for channel in range(1, 4):
            device.channel = channel
            print("---------------------------------------------------------------------------------------------------")
            print(f"-> output subsystem...channel={device.channel}")
            print("---------------------------------------------------------------------------------------------------")
            device.output = 'ON'
            print(f"output state    : {device.output}")
            device.output = 'OFF'
            print(f"output state    : {device.output}")
    except pyvisa.errors.VisaIOError as msg:
        print(msg)


if __name__ == '__main__':
    main()
