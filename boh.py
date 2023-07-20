from lib import *

circuit = QuantumCircuit(3,3)
circuit.x(0)

circuit.barrier()

circuit.h(1)
circuit.cx(1,2)

show(circuit)

circuit.cx(0,1)
circuit.h(0)

show(circuit)

circuit.barrier()
circuit.measure([0,1], [0,1])


circuit.barrier()

circuit.cx(1,2)
circuit.cz(0,2)
circuit.measure(2,2)

show_circuit(circuit)
show_bloch(circuit)

show_histo(circuit, back('simulator'), 1000)




