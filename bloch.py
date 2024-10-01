import matplotlib
from lib import *

#from scipy.misc import toimage
#from scipy.misc import imshow # SE NON LO USI RICORDATI DI METTERE pip3 install scipy==1.7.3 (rimuovere 1.1.0 se non lo fa da solo)
import matplotlib.mathtext as mathtext

matplotlib.rc('image', origin='upper')



circuit = QuantumCircuit(3, 2)
circuit.h(0)

statevector = show_bloch(circuit)


#parser = mathtext.MathTextParser("Bitmap")
#parser.to_png('test2.png', statevector, color='green', fontsize=14, dpi=100)

# rgba1, depth1 = parser.to_rgba(r'IQ: $\sigma_i=15$', color='blue', fontsize=20, dpi=200)
# rgba2, depth2 = parser.to_rgba(r'some other string', color='red', fontsize=20, dpi=200)


fig = plt.figure()
# fig.figimage(rgba1, 100, 100)
# fig.figimage(rgba2, 100, 300)

plt.show()



# print(statevector)
# toimage(statevector).show()
# plt.imshow(statevector, interpolation='nearest')
# plt.show()

#imshow(statevector)
