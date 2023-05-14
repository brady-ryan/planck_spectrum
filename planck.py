import numpy as np
import matplotlib.pyplot as plt

h = 6.626e-34
c = 3.0e+8
k = 1.38e-23
sigma = 5.67e-8

class Planck:

    def __init__(self,T,name):
        self.T = T
        self.name = name
        self.wls = np.arange(1e-9, 2e-6, 1e-9)

    def B(self,wl,T):
        a = 2.*h*c**2
        b = (h*c)/(wl*k*T)
        ans = a/((wl**5)*(np.exp(b)-1.))
        return ans
    
    def plot(self):
        xs = self.wls*1e9
        ys = self.B(self.wls,self.T)
        ymax = max(ys)
        if ymax:
            self.peak = xs[np.argmax(ys)]
            print(f'Max intensity of {self.T} K at {self.peak} nm')
        plt.plot(xs,ys,label=f'{self.name}')
        plt.ylabel(r"Radiance (J/$m^{2}$/sr/$\lambda$)")
        plt.xlabel(r"Wavelength (nm)")
        plt.title(r"Planck Spectra of Various Stars")
        plt.legend()

    def wien(self):

        ans = 0.0029e9/self.T
        print(ans)

    
betelgeuse = Planck(3500,'Betelgeuse')
arcturus = Planck(4290,'Arcturus')
sun = Planck(5578,'Sun')
rigel = Planck(11000,'Rigel')


stars = [betelgeuse,arcturus,sun]

for s in stars:

    s.plot()

plt.show()
