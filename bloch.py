from lib import *
from qiskit.visualization import array_to_latex
from pylatexenc.latex2text import LatexNodes2Text
import IPython






circuit = QuantumCircuit(3, 2)
circuit.h(0)


show_circuit(circuit)
statevector = show_bloch(circuit)
print_statevector(circuit)

