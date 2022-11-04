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

/*Setup Spectrum Analyzer*/
function set_spectrum(){
	/* Enable only Spectrum Analyzer Channel 1  */
	spectrum.channels[0].enabled = true
    spectrum.channels[1].enabled = false
	spectrum.running = true
}
function main() {
	var connected = connect(host)
	if (!connected)
		return Error()
    set_signal_generator()
    msleep(1000)
	set_spectrum()
	msleep(1000)
	launcher.focused_instrument=1
	msleep(1000)
	returnToApplication();
}

main()

