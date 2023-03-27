from qiskit import *
from qiskit_ibm_provider import IBMProvider
from qiskit.tools.visualization import plot_histogram, plot_bloch_multivector, state_drawer
import matplotlib.pyplot as plt
from qiskit.quantum_info import Statevector

def back(prov):
    if (prov == "simulator"):
        return Aer.get_backend('qasm_simulator')
    else:
        provider = IBMProvider()
        return provider.get_backend('ibmq_lima')


actual=['ibm_nairobi', 'ibmq_lima', 'ibmq_belem', 'ibmq_manila', 'ibm_oslo',  'ibmq_jakarta', 'ibm_lagos' , 'ibm_perth', 'ibmq_quito']
simulatora=['ibmq_qasm_simulator', 'simulator_mps', 'simulator_statevector', 'simulator_extended_stabilizer', 'simulator_stabilizer']


def show_circuit(circuit):
    circuit.draw(output='mpl', style={'backgroundcolor': '#EEEEEE'})
    wm = plt.get_current_fig_manager()
    wm.window.wm_geometry("1450x230+0+0")
    plt.show(block=False)
    print(circuit)
    input()


def show_bloch(circuit):
    result = execute(circuit, backend = BasicAer.get_backend('statevector_simulator')).result()
    statevector = result.get_statevector()
    plot_bloch_multivector(statevector)
    wm = plt.get_current_fig_manager()
    wm.window.wm_geometry("1450x230+0+0")
    plt.show(block=False)
    input()
    return statevector


def show_histo(circuit, back, shts):
    result = execute(circuit, backend=back, shots = shts).result()
    counts = result.get_counts()
    plot_histogram(counts)
    plt.show(block=False)
    input()


def print_statevector (circuit):  # pip install ipython, sudo apt-get install texlive-latex-extra texlive-fonts-recommended dvipng cm-super, brew install texlive
    #mpl.rcParams.update(mpl.rcParamsDefault) #SERVE import matplotlib as mpl
    # plt.rcParams.update({
    #     "text.usetex": True,
    #     "font.family": "monospace",
    #     "font.monospace": 'Computer Modern Typewriter',
    #    'legend.fontsize': 'x-large',
    #         'figure.figsize': (5, 5),
    #         'axes.labelsize': 'x-large',
    #         'axes.titlesize':'x-large',
    #         'xtick.labelsize':'x-large',
    #         'ytick.labelsize':'x-large
    # })

    ket = Statevector(circuit)
    ket_latex = "$" + state_drawer(ket, 'latex_source') + "$"
    fig = plt.figure()
    plt.plot()
    fig.suptitle(ket_latex, fontsize=25, y=0.65)

    wm = plt.get_current_fig_manager()
    wm.window.wm_geometry("1450x230+0+0")
    plt.show(block=False)
    input()
