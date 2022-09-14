from funcgen import find_instrument, func_on, func_off
import random

siggen = find_instrument()
idn = siggen.query("*IDN?")
func = ["sine", "square"]
for i in range(5):
    freq = random.randint(1000,20000)
    ampl = random.random(1.0,3.0)
    offset = random.random(0.0, 2.0)
    offset = random.ran
    print(freq)
    func_on(siggen, func[i%2], freq, ampl, offset)
    
func_off(siggen)