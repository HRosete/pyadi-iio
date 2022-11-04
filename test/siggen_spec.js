#!/usr/bin/scopy -s

/* This is the script that starts scopy up and connects to the emulator */
var host = "192.168.2.1"


function connect(host) {
	print("Connecting to " + host + "...")

	var success = launcher.connect("ip:" + host)

	if (success)
		print("Connected!")
	else
		print("Failed!")

	return success;
}

/*Setup Signal Generator*/
function set_signal_generator(){

	/* Enable only Signal Generator Channel 1  */
	siggen.enabled[0] = true
    siggen.enabled[1] = false
	
	/* Set Channel 1 operation mode to Waveform */
	siggen.mode[0] = 1
	
	/* Set Channel 1 Waveform type to Sine */
	siggen.waveform_type[0] = 0
	
	/* Set Channel 1 frequency to 1kHz */
	siggen.waveform_frequency[0] = 25000000
	
	/* Set Channel 1 amplitude to 3V */
	siggen.waveform_amplitude[0] = 3
	
	/* Set Channel 1 offset to 1V */
	siggen.waveform_offset[0] = 0
	
	/* Set Channel 1 phase to 0 degrees */
	siggen.waveform_phase[0] = 0
	
	/* Run Signal Generator */
	siggen.running = true
}

/*Setup Oscilloscope*/
function set_oscilloscope(){
	
	/* Enable only Oscilloscope Channel 1  */
	osc.channels[0].enabled = true
	osc.channels[1].enabled = false
	
	/* Set Volts/Div to 1V/div */
	osc.channels[0].volts_per_div = 1
	
	/* Set Time Base to 1 ms */
	osc.time_base = 0.001
	
	/* Set Time Position to 0s */
	osc.time_position = 0
	
	/* Run Oscilloscope */
	osc.running = false
}

/*Setup Spectrum Analyzer*/
function set_spectrum(){
	
	/* Enable only Spectrum Analyzer Channel 1  */
	spectrum.channels[0].enabled = true
    spectrum.channels[1].enabled = false
	
	/* Run Oscilloscope */
	spectrum.running = true
}


function main() {
	/* hardcoded for now */

	var connected = connect(host)
	if (!connected)
		return Error()

    set_signal_generator()

    msleep(1000)
    
    set_oscilloscope()
    
    msleep(1000)

	set_spectrum()
	
	msleep(1000)

	/* Focus spectrum analyzer */
	launcher.focused_instrument=1
	/* Resume control to the application*/
	returnToApplication();
}

main()
