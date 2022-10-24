import subprocess
import time

global scopy_path
global m2k_config

scopy_path = "C:\Program Files\Scopy\Scopy.exe"
m2k_config = "instr_config.js"
# m2k_config = "siggen_spec.js"

def func_on(instr, func, freq, ampl, offset):
    if instr == "m2k":
        
        copy_conf = subprocess.run('copy instr_config_base.js instr_config.js', shell=True)
        instr_config = open("instr_config.js","a")
        instr_config.writelines(["function set_signal_generator(){ \n", "siggen.enabled[0] = true \n", "siggen.enabled[1] = false \n"])
        instr_config.writelines(["siggen.mode[0] = 1 \n", "siggen.waveform_type[0] = 0 \n"])
        instr_config.write("siggen.waveform_frequency[0] = " + str(freq) + " \n")
        instr_config.write("siggen.waveform_amplitude[0] = " + str(ampl) + " \n")
        instr_config.write("siggen.waveform_offset[0] = " + str(offset) + " \n")
        instr_config.write("siggen.waveform_phase[0] = 0 \n")
        instr_config.write("siggen.running = true} \n")
        instr_config.close()
        
        proc = subprocess.Popen(scopy_path + " --script " + m2k_config)
        print("Launced Scopy and configured instruments.")
    
    return proc

def func_off(instr, proc):
    if instr == "m2k":
        proc.kill()
        subprocess.run('del instr_config.js', shell=True)
        print("Successfully killed scopy!")
        del proc
    
    return
