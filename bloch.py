from lib import *

circuit = QuantumCircuit(2, 2)
circuit.h(0)

show_block(circuit)

result = execute(circuit, backend = BasicAer.get_backend('statevector_simulator')).result()
statevector = result.get_statevector()
plot_bloch_multivector(statevector)

circuit.y([0,1])

show_block(circuit)


result = execute(circuit, backend = BasicAer.get_backend('statevector_simulator')).result()
statevector = result.get_statevector()
plot_bloch_multivector(statevector)

print(statevector)
