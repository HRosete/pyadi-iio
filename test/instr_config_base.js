#!/usr/bin/scopy -s

var host = "ip:192.168.2.1"
// var host = "usb:1.19.5"
function connect(host) {
	print("Connecting to " + host + "...")
	var success = launcher.connect(host)
	if (success)
		print("Connected!")
	else
		print("Failed!")
	return success;
}

/*Setup Oscilloscope*/
function set_oscilloscope(){
	/* Enable only Spectrum Analyzer Channel 1  */
	osc.channels[0].enabled = true
    osc.channels[1].enabled = false
	osc.running = true
	msleep(1000)
	launcher.focused_instrument=0
}

/*Setup Spectrum Analyzer*/
function set_spectrum(){
	/* Enable only Spectrum Analyzer Channel 1  */
	spectrum.channels[0].enabled = true
    spectrum.channels[1].enabled = false
	spectrum.running = true
	msleep(1000)
	launcher.focused_instrument=1
}
function main() {
	var connected = connect(host)
	if (!connected)
		return Error()
    set_signal_generator()
    msleep(1000)
	set_oscilloscope()
	msleep(1000)
	
	/* Read Channel 1 Signal Period Value */
	var period = osc.channels[0].period
	var frequency = 1/period
	/* Write frequency to file */
	read_val_path = "frequency.txt"
	fileIO.writeToFile(frequency,read_val_path)


	msleep(1000)
	returnToApplication();
}

main()

