from qiskit import *
from qiskit.visualization import plot_histogram, plot_bloch_multivector, state_drawer
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

from qiskit.quantum_info import Statevector
from qiskit_aer import Aer
from qiskit_ibm_runtime import QiskitRuntimeService

from dotenv import load_dotenv
import os
load_dotenv()  # Load the environment variables from .env

my_token = os.getenv("MY_SECRET_TOKEN")
if my_token is None:
    raise ValueError("Token not found in environment variables")

service = QiskitRuntimeService.save_account(channel="ibm_quantum", token=my_token, overwrite=True)




def back(prov):
    if (prov == "simulator"):
        return Aer.get_backend('qasm_simulator')
    else:
        service = QiskitRuntimeService(channel="ibm_quantum", token=my_token)
        backend = service.least_busy(operational=True, simulator=False)
        return backend

#actual=['ibm_nairobi', 'ibmq_lima', 'ibmq_belem', 'ibmq_manila', 'ibm_oslo',  'ibmq_jakarta', 'ibm_lagos' , 'ibm_perth', 'ibmq_quito']
#simulatora=['ibmq_qasm_simulator', 'simulator_mps', 'simulator_statevector', 'simulator_extended_stabilizer', 'simulator_stabilizer']


def show_circuit(circuit):
    circuit.draw(output='mpl', style={'backgroundcolor': '#EEEEEE'})
    wm = plt.get_current_fig_manager()
    wm.window.setGeometry(0, 0, 1450, 230)
    plt.show(block=False)
    print(circuit)
    input()


def show_bloch(circuit):
    backend = Aer.get_backend('statevector_simulator')
    new_circuit = transpile(circuit, backend)
    result = backend.run(new_circuit).result()
    statevector = result.get_statevector()
    plot_bloch_multivector(statevector)
    wm = plt.get_current_fig_manager()
    wm.window.setGeometry(0, 0, 1450, 230)
    plt.show(block=False)
    print(statevector)
    input()
    return statevector


def show_histo(circuit, backend, shts):
    new_circuit = transpile(circuit, backend, shts)
    result = backend.run(new_circuit).result()
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

    ket = Statevector(circuit) # esplode se misuri
    ket_latex = "$" + state_drawer(ket, 'latex_source') + "$"
    fig = plt.figure()
    plt.plot()
    fig.suptitle(ket_latex, fontsize=25, y=0.65)
    wm = plt.get_current_fig_manager()
    wm.window.setGeometry(0, 0, 1450, 230)
    plt.show(block=False)
    input()



def show(circuit):
    show_circuit(circuit)
    show_bloch(circuit)
    print_statevector(circuit)
