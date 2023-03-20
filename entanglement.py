from lib import *

circuit = QuantumCircuit(2,2)
circuit.h(0)
circuit.cx(0,1)  #reverse q2 if q1 is |1>
circuit.measure([0,1],[0,1])

show_block(circuit)

result = execute(circuit, backend = back('simulator'), shots = 9999).result()
plot_histogram(result.get_counts(circuit))
plt.show(block=False)
input()