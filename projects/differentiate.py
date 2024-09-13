import numpy as np


def differentiate(u, dt):
    du = np.zeros(len(u)-1)
    for i in len(du):
        du[i] = (u[i+1]-u[i])/dt
    return du

def differentiate_vector(u, dt):
    du = np.zeros(len(u)-1)
    for i in len(du):
        du[i] = (u[i+1]-u[i])/dt
    return du

def test_differentiate():
    t = np.linspace(0, 1, 10)
    dt = t[1] - t[0]
    u = t**2
    du1 = differentiate(u, dt)
    du2 = differentiate_vector(u, dt)
    assert np.allclose(du1, du2)

if __name__ == '__main__':
    test_differentiate()
    
