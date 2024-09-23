"""
Example on instrument domain
"""

import argparse
import pyvisa.errors
from pyrs.hmp2030 import HMP2030

NAME = 'USB0::0x0AAD::0x0117::120470::INSTR'
LIBRARY = '/usr/lib/librsvisa.so'


def main():
    """
    Main entry
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', default=NAME, help=f'device visa name or address. default = {NAME}')
    parser.add_argument('-l', '--library', default=LIBRARY, help=f'visa shared library. default = {LIBRARY}')
    args = parser.parse_args()

    try:
        device = HMP2030(name=args.name, library=args.library)
        device.beep()
        print("-------------------------------------------------------------------------------------------------------")
        print(f"device identity  : {device.identity}")
        print("-------------------------------------------------------------------------------------------------------")
        for channel in range(1, 4):
            device.channel = channel
            print(f"device channel   : {device.channel}")
            device.output = 'OFF'
    except pyvisa.errors.VisaIOError as msg:
        print(msg)


if __name__ == '__main__':
    main()
