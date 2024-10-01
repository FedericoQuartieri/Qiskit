from lib import *
from qiskit_algorithms import Shor
from qiskit.aqua import QuantumInstance


quantum_instance_sim = QuantumInstance(back('simulator'), shots = 1000)
quantum_instance_ibmq = QuantumInstance(back('c'), shots = 1000)
                                        
#my_shor_sim = Shor(N= 21, a = 2, quantum_instance = quantum_instance_sim)
#Shor.run(my_shor_sim)

my_shor_ibmq = Shor(N= 9, a = 2, quantum_instance = quantum_instance_sim)
Shor.run(my_shor_ibmq)
