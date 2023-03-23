from lib import *

circuit = QuantumCircuit(1, 1)
circuit.h(0)


show_block(circuit)
statevector = show_bloch(circuit)


# circuit.y(0)
# show_block(circuit)
# statevector = show_bloch(circuit)

circuit.z(0)
show_block(circuit)
statevector = show_bloch(circuit)


print(statevector)
