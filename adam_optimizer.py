import numpy as np

def adam_optimizer(f, grad, x0, learning_rate=0.001, beta1=0.9, beta2=0.999, epsilon=1e-8, num_iterations=10):
    x=x0.copy()
    t=0
    m,v= np.zeros_like(x0), np.zeros_like(x0)
    for _ in range(num_iterations):
        t+=1
        g=grad(x)
        m=beta1*m+(1-beta1)*g
        v=beta2*v+(1-beta2)*g**2
        m_hat=m/(1-beta1**t)
        v_hat=v/(1-beta2**t)
        x-=(learning_rate*m_hat)/(np.sqrt(v_hat)+ epsilon)
    return x


def objective_function(x):
    return x[0]**2 + x[1]**2

def gradient(x):
    return np.array([2*x[0], 2*x[1]])

x0 = np.array([1.0, 1.0])
x_opt = adam_optimizer(objective_function, gradient, x0)

print("Optimized parameters:", x_opt)