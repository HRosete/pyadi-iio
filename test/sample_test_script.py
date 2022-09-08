from funcgen import find_instrument, func_on, func_off
import random

siggen = find_instrument()
idn = siggen.query("*IDN?")
func = ["sine", "square"]
for i in range(5):
    freq = random.randint(1000,20000)
    print(freq)
    func_on(siggen, func[i%2], freq, 2, 0)
    
func_off(siggen)