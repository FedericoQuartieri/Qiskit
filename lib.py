from qiskit import *
from qiskit_ibm_provider import IBMProvider
from qiskit.tools.visualization import plot_histogram, plot_bloch_multivector
import matplotlib.pyplot as plt

def back(prov):
    if (prov == "simulator"):
        return Aer.get_backend('qasm_simulator')
    else:
        provider = IBMProvider()
        return provider.get_backend('ibmq_lima')


actual=['ibm_nairobi', 'ibmq_lima', 'ibmq_belem', 'ibmq_manila', 'ibm_oslo',  'ibmq_jakarta', 'ibm_lagos' , 'ibm_perth', 'ibmq_quito']
simulatora=['ibmq_qasm_simulator', 'simulator_mps', 'simulator_statevector', 'simulator_extended_stabilizer', 'simulator_stabilizer']


def show_block(circuit):
    #plt.figure(figsize=(5, 5))
    circuit.draw(output='mpl', style={'backgroundcolor': '#EEEEEE'})
    plt.show(block=False)
    print(circuit)
    input()

