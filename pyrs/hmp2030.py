"""
HMP2030 Power supply interface
"""

import time
import pyvisa


class HMP2030:
    """
    HMP2028 Power supply class
    """
    def __init__(self, name, library="/usr/lib/librsvisa.so"):
        """
        Create HMP2030 object

        :param name: VISA resource name
        :param library: Path on VISA backend library
        """
        self._source = 'VOLT'
        rm = pyvisa.ResourceManager(visa_library=library)
        self.instr = rm.open_resource(name)

    def send(self, command):
        """
        Send the command

        :param command: command string
        :return: None
        """
        self.instr.write(command)

    def read(self, timeout=0.3):
        """
        read command response

        :param timeout: timeout value before read
        :return:
        """
        time.sleep(timeout)
        return self.instr.read().split('\n')[0]

    # ------------------------------------------------------------------------------------------------------------------
    # COMMON subsystem
    # ------------------------------------------------------------------------------------------------------------------

    @property
    def identity(self):
        """
        Get identity string

        :return: device identity string
        """
        self.send('*IDN?')
        return self.read()

    def save(self, location):
        """
        Save the current setting in a location

        :param location: location number
        :return: None
        """
        if location in range(0, 10):
            self.send(f"*SAV {location}")

    def call(self, location):
        """
        recall settings form a location

        :param location: location number
        :return:
        """
        if location in range(0, 10):
            self.send(f"*RCL {location}")

    # ------------------------------------------------------------------------------------------------------------------
    # SYSTEM subsystem
    # ------------------------------------------------------------------------------------------------------------------

    def beep(self):
        """
        Emit a single beep from the instrument

        :return: None
        """
        self.send('SYST:BEEP')

    @property
    def version(self):
        """
        Get scpi version

        :return: version number
        """
        self.send('SYST:VERS?')
        return self.read()

    @property
    def error(self):
        """
        Query the error/event queue

        :return:
        """
        self.send('SYST:ERR?')
        return self.read()

    # ------------------------------------------------------------------------------------------------------------------
    # INSTRUMENT subsystem
    # ------------------------------------------------------------------------------------------------------------------

    @property
    def channel(self):
        """
        Get the current selected channel

        :return: Selected channel
        """
        self.send('INST?')
        return self.read()

    @channel.setter
    def channel(self, channel):
        """
        Set channel by number

        :param channel: channel number
        :return: None
        """
        if channel in [1, 2, 3]:
            self.send(f'INST:NSEL {channel}')

    # ------------------------------------------------------------------------------------------------------------------
    # MEASURE subsystem
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def measure_current(self):
        """
        Queries the current value of the selected channel

        :return: current in Ampere
        """
        self.send('MEAS:CURR?')
        return self.read()

    @property
    def measure_voltage(self):
        """
        Queries the voltage value of the selected channel

        :return: voltage in volt
        """
        self.send('MEAS:VOLT?')
        return self.read()

    # ------------------------------------------------------------------------------------------------------------------
    # OUTPUT subsystem
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def output(self):
        """
        Query the output state of the selected channel

        :return:  output state
        """
        self.send('OUTP?')
        return self.read()

    @output.setter
    def output(self, state):
        """
        Activate the selected channel and turns on the output

        :param state: ON | OFF
        :return: None
        """
        if state in ['ON', 'OFF']:
            self.send(f'OUTP:STAT {state}')

    def output_selected(self, channels: list, state):
        """
        selected channels in the list, activate and turns on output simultaneously

        :param channels: a list of channel number (1,2,3)
        :param state: 0 or 1
        :return: None
        """
        for i in channels:
            self.send(f'INST:NSEL {i}')
            self.send(f'OUTP:SEL {state}')
            self.send(f'OUTP:GEN {state}')

    # ------------------------------------------------------------------------------------------------------------------
    # SOURCE subsystem
    # ------------------------------------------------------------------------------------------------------------------

    @property
    def source(self):
        """
        Get selected source parameter

        :return:
        """
        return str(self._source).lower()

    @source.setter
    def source(self, param):
        """
        Set current source parameter

        :param param: source parameter (CURRENT, VOLT)
        :return: None
        """
        if param in ['volt', 'curr']:
            self._source = str(param).upper()

    @property
    def param(self) -> float:
        """
        Get selected source parameter value

        :return: parameter value
        """
        self.send(f"{self._source}?")
        return float(self.read())

    @param.setter
    def param(self, value: float):
        """
        Set selected source parameter value

        :param value:
        :return:
        """
        self.send(f"{self._source} {value}")

    @property
    def step(self) -> float:
        """
        Get selected source step value

        :return: parameter value
        """
        self.send(f"{self._source}:STEP?")
        return float(self.read())

    @step.setter
    def step(self, value: float):
        """
        Set selected source step value

        :param value: step value
        :return:
        """
        self.send(f"{self._source}:STEP {value}")

    @property
    def volt(self):
        """
        Get the output voltage of the selected channel

        :return: selected channel voltage
        """
        self.send('VOLT?')
        return self.read()

    @volt.setter
    def volt(self, value):
        """
        Set selected channel voltage
        :param value: voltage value
        :return: None
        """
        self.send(f"VOLT {value}")

    def volt_up(self):
        """
        Increase the selected channel voltage by step value
        :return: None
        """
        self.send('VOLT UP')

    def volt_down(self):
        """
        Decrease the selected channel voltage by step value

        :return: None
        """
        self.send('VOLT DOWN')

    @property
    def current(self):
        """
        Get the output current of the selected channel

        :return: selected channel current
        """
        self.send('CURR?')
        return self.read()

    @current.setter
    def current(self, value):
        """
        set the current of the selected channel

        :param value: current value
        :return: None
        """
        self.send(f'CURR {value}')

    def current_up(self):
        """
        Increase the selected channel current by step value

        :return: None
        """
        self.send('CURR UP')

    def current_down(self):
        """
        Decrease the selected channel current by step value

        :return: None
        """
        self.send('CURR DOWN')

    def move_up(self):
        """
        Increase the selected channel selected parameter by step value

        :return: None
        """
        self.send(f"{self._source} UP")

    def move_down(self):
        """
        Decrease the selected channel selected parameter by step value

        :return: None
        """
        self.send(f"{self._source} DOWN")

    @property
    def source_properties(self) -> dict:
        """
        Get selected channel source properties

        :return: a dictionary
        """
        self.source = 'volt'
        volt = {
            "value": self.param,
            "step": self.step
        }
        self.source = 'curr'
        current = {
            "value": self.param,
            "step": self.step
        }
        return {'volt': volt, 'current': current, 'output': self.output}

    @source_properties.setter
    def source_properties(self, settings: dict):
        """
        set the current selected channel with a dictionary

        :param settings: dictionary of settings

        :return: None
        """
        cmd = f"VOLT {settings['volt']['value']}"
        self.send(cmd)
        cmd = f"VOLT:STEP {settings['volt']['step']};"
        self.send(cmd)
        cmd = f"CURR {settings['current']['value']}"
        self.send(cmd)
        cmd = f"CURR:STEP {settings['volt']['step']};"
        self.send(cmd)

    # ------------------------------------------------------------------------------------------------------------------
    # APPLY subsystem
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def apply(self):
        """
        Get voltage and current of the selected channel

        :return: voltage and current values
        """
        self.send('APPLY?')
        return self.read()

    def set_power(self, sets: dict):
        """
        set power according to dictionary
        {1:value, 2:value}

        :warning: no control is made on dictionary content
        :return:
        """
        for i in sets:
            self.channel = i
            self.volt = sets[i]

    # ------------------------------------------------------------------------------------------------------------------
    # STATUS subsystem
    # ------------------------------------------------------------------------------------------------------------------
