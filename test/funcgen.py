import time
import pyvisa

supported_instruments = ["Agilent Technologies,33220A,MY44053237,2.07-2.06-22-2"]

def find_instrument():
    rm = pyvisa.ResourceManager()
    all_resources = rm.list_resources()
    if len(all_resources) == 0:
        return None
    for i in range(0, len(all_resources)):
        my_instrument = rm.open_resource(
            all_resources[i],
            write_termination="\n",
            read_termination="\n",
        )

        try:
            idn = my_instrument.query("*IDN?")
            if idn in supported_instruments:
                break
            else:
                print("This instrument is currently not supported!")
        except Exception as e:
            my_instrument = None
            continue
    return my_instrument

def func_on(instr, func, freq, ampl, offset):
    # reset function generator
    instr.write("*RST")
    # set waveshape: sine, square, ramp, pulse, noise, dc
    func = func.lower()
    if func == "sine":
        func = "SINusoid"
    elif func == "square":
        func = "SQUare"
    elif func == "ramp":
        func = "RAMP"
    elif func == "pulse":
        func == "PULSe"
    elif func == "noise":
        func = "NOISe"
    elif func == "dc":
        func = "DC"
    instr.write("FUNCtion " + func)
    # set frequency
    instr.write("FREQuency " + str(freq))
    # set amplitude
    instr.write("VOLTage " + str(ampl))
    # set offset
    instr.write("VOLTage:OFFSet " + str(offset))
    # turn on instrument output
    instr.write("OUTPut ON")
    time.sleep(3)
    return

def func_off(instr):
    # turn off output
    instr.write("OUTPut OFF")
    # reset function generator
    instr.write("*RST")
    return