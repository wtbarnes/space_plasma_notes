import numpy as np
import matplotlib.pyplot as plt

#Define normalized omega coordinate
x1R = np.linspace(0,1,1000)
x2R = np.linspace(np.sqrt(5)/2+1/2,5,1000)
x1L = np.linspace(0,9.999999e-4,1000)
x2L = np.linspace(np.sqrt(5)/2-1/2,5,1000)

#Define L and R dispersion relations as normalized wave vector 
def dr_R(x):
    return np.sqrt(x**2 - x/(x-1))
    
eps_1 = 1e-3
eps_2 = 1e-3    
def dr_L(x,e1,e2):
    return np.sqrt(x**2 - x/(x+1) - e1*x/(x-e2))
    
#plot the dispersion relations
fig = plt.figure(figsize=(8,6))
ax = fig.gca()
ax.plot(dr_R(x1R),x1R,'b',label=r'RCP')
ax.plot(dr_R(x2R),x2R,'b')
ax.plot(dr_L(x1L,eps_1,eps_2),x1L,'r',label=r'LCP')
ax.plot(dr_L(x2L,eps_1,eps_2),x2L,'r')
ax.plot(np.linspace(0,5),np.linspace(0,5),'-.k')
ax.axhline(y=1,color='black',linestyle='dotted')
ax.axhline(y=eps_2,color='black',linestyle='dotted')
ax.set_yscale('log')
ax.set_xscale('log')
ax.set_xlim([0.05,5])
ax.set_ylim([0.0001,5])
ax.set_xlabel(r'$kc/\omega_{pe}$',fontsize=20)
ax.set_ylabel(r'$\omega/\omega_{pe}$',fontsize=20)
ax.legend(loc='best',fontsize=16)
plt.savefig('cmp_dispersion.pdf',dpi=1000,format='pdf',bbox='tight')
plt.show()