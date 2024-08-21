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
        print(f"-> source subsystem...channel={device.channel}")
        print("-----------------------------------------------------------------------------------------------------")
        print("--> get values...")
        device.source = 'volt'
        print(f"volt parameter   : {device.param}")
        print(f"volt step        : {device.step}")
        device.source = 'curr'
        print(f"current parameter: {device.param}")
        print(f"current step     : {device.step}")

        print("--> set volt...")
        device.volt = 'MAX'
        print(f"voltage (max)    : {device.volt}")
        device.volt = 'MIN'
        print(f"voltage (min)    : {device.volt}")
        device.volt = 1.0
        print(f"voltage (1.0)    : {device.volt}")

        device.source = 'volt'
        print(f"source           : {device.source}")
        print(f"parameter        : {device.param}")
        print(f"step             : {device.step}")
        device.param += 1
        print(f"parameter        : {device.param}")
        device.param -= 1
        print(f"parameter        : {device.param}")
        device.step += 1
        print(f"step             : {device.step}")
        device.step -= 1
        print(f"step             : {device.step}")

        device.move_up()
        print(f"parameter up     : {device.param}")
        device.move_down()
        print(f"parameter down   : {device.param}")

        device.source = 'curr'
        print(f"source           : {device.source}")
        print(f"parameter        : {device.param}")
        print(f"step             : {device.step}")
        device.param += 1
        print(f"parameter        : {device.param}")
        device.param -= 1
        print(f"parameter        : {device.param}")
        device.step += 1
        print(f"step             : {device.step}")
        device.step -= 1
        print(f"step             : {device.step}")
        device.move_up()
        print(f"step up          : {device.param}")
        device.move_down()
        print(f"step down        : {device.param}")

        # get current channel all properties
        settings = device.source_properties
        print(f"properties (init): {settings}")

        # program new settings
        new_settings = {
            'volt': {'value': 2, 'step': 2},
            'current': {'value': 0.5, 'step': 0.2}
        }

        device.source_properties = new_settings
        # get current channel all properties for checking
        print(f"properties (new ): {device.source_properties}")
        device.source_properties = settings
        print(f"properties (init): {device.source_properties}")


if __name__ == '__main__':
    main()
