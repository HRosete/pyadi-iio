# This module is made to create contexts for signal sources and signal receivers
# such as IIO-based devices and other external instruments just like signal
# generators and spectrum analyzers.


def get_signal_context(uri, classname, device="iio"):
    """get_signal_context: <definition>
    parameters:
        uri: type=string
            URI of IIO context of target board/system
        classname: type=string
            Name of pyadi interface class which contain attribute
        device: type=string
            Options: iio, sig_gen, m2k, spectrum_analyzer
    """
    # Can be better - resource sweep etc.
    try:
        if device == "sig_gen" or device == "spectrum_analyzer":
            # pyvisa thingy c/o template from scipy.py
            signal_ctx = None  # As of the moment, None
        elif device == "m2k":
            # libm2k thingy
            signal_ctx = None  # As of the moment, None
        elif device == "iio":
            signal_ctx = eval(classname + "(uri='" + uri + "')")
        return signal_ctx
    except Exception as e:
        print("No context for signal source/recipient was made!")
