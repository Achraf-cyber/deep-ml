import numpy as np

def adadelta_optimizer(parameter, grad, u, v, rho=0.95, epsilon=1e-6):
    """
    Update parameters using the AdaDelta optimizer.
    AdaDelta is an extension of AdaGrad that seeks to reduce its aggressive,
    monotonically decreasing learning rate.
    Args:
        parameter: Current parameter value
        grad: Current gradient
        u: Running average of squared gradients
        v: Running average of squared parameter updates
        rho: Decay rate for the moving average (default=0.95)
        epsilon: Small constant for numerical stability (default=1e-6)
    Returns:
        tuple: (updated_parameter, updated_u, updated_v)
    """
    # Your code here
    squared_grad = grad * grad
    u = rho * u + (1-rho) * squared_grad
    rms_grad = np.sqrt( u + epsilon)
    rms_step = np.sqrt( v + epsilon)
    step = - rms_step/rms_grad * grad
    v = rho * v + (1-rho) * step ** 2
    parameter += step
    return parameter, u, v