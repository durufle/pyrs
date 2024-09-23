"""
Example on measure domain
"""
import argparse
import pyvisa.errors
from pyrs.hmp2030 import HMP2030

NAME = 'USB0::0x0AAD::0x0117::120470::INSTR'
LIBRARY = '/usr/lib/librsvisa.so'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', default=NAME, help=f'device visa name or address. default = {NAME}')
    parser.add_argument('-l', '--library', default=LIBRARY, help=f'visa shared library. default = {LIBRARY}')
    args = parser.parse_args()

    try:
        device = HMP2030(name=args.name, library=args.library)
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
    except pyvisa.errors.VisaIOError as msg:
        print(msg)


if __name__ == '__main__':
    main()
