def radius(x, y):
    from numpy import empty
    Nx, Ny = x.shape[0], y.shape[0]
    r = empty((Nx, Ny))
    for i in range(Nx):
        for j in range(Ny):
            r[i, j] = (x[i] - y[j])
    return r

def inv_radius(x, y):
    from numpy import empty
    Nx, Ny = x.shape[0], y.shape[0]
    r = empty((Nx, Ny))
    for i in range(Nx):
        for j in range(Ny):
            r[i, j] = (1/x[i] - 1/y[j])
    return r

def se_kernel(w, l, R):
    from numpy import exp
    K0 = exp(-(R/l)**2)
    return w**2 * K0

def ise_kernel(w, l, R):
    from numpy import exp
    K0 = exp(-(R*l)**2)
    return w**2 * K0

def gpr_se(Kdd, x, y, yinf_min, yinf_max, y_bins, w_hyp, l_hyp):
    from numpy import array, empty, linspace, arange, diag, maximum, sqrt, exp
    from numpy.linalg import eigh
    td  = array(xd, dtype='float64')                  #input radius data
    yd  = array(y - y[-1], dtype='float64')           #input tabulated potential
    nd  = td.shape[0]                                 #size of the input data

    Λ, V = eigh(Kdd)
    Λ[Λ < 1e-14] = 1e-14                             #round-off error correction
    α = V @ ((yd.T @ V) / Λ).T                       #inv(Kdd) @ Yd
    ti      = linspace(yinf_min, yinf_max, y_bins)   #new points for regression (default is to use input points)
    Rid     = radius(ti, td)                         #euclidean distance between input and output radii
    Rii     = radius(ti, ti)                         #euclidean distance between output radii
    Kid     = se_kernel(w_hyp, l_hyp, Rid)                 #squared exponential kernel applied to input and output data
    Kii     = se_kernel(w_hyp, l_hyp, Rii)                 #squared exponential kernel applied to output data
    β       = V @ ((Kid @ V) / Λ).T                  # inv(Kdd) @ Kid
    μ_post  = (Kid @ α)                              #calculate posterior mean
    Σ_post  = Kii - Kid @ β                          #calculate posterior covariance
    σ2_post = maximum(0.0, diag(Σ_post))             #posterior variance
    σ_post  = sqrt(σ2_post)                          #posterior standard deviation
    return μ_post, σ_post 

def gpr_ise(Kdd, x, y, yinf_min, yinf_max, y_bins, w_hyp, l_hyp):
    from numpy import array, empty, linspace, arange, diag, maximum, sqrt, exp
    from numpy.linalg import eigh
    td  = array(x, dtype='float64')                  #input radius data
    yd  = array(y - y[-1], dtype='float64')           #input tabulated potential
    nd  = td.shape[0]                                 #size of the input data

    Λ, V = eigh(Kdd)
    Λ[Λ < 1e-14] = 1e-14                           # round-off error correction
    α = V @ ((yd.T @ V) / Λ).T                     # inv(Kdd) @ Yd
    ti      = linspace(yinf_min, yinf_max, y_bins) #new points for regression (default is to use input points)
    Rid     = inv_radius(ti, td)                   #euclidean distance between input and output radii
    Rii     = inv_radius(ti, ti)                   #euclidean distance between output radii
    Kid     = ise_kernel(w_hyp, l_hyp, Rid)         #squared exponential kernel applied to input and output data
    Kii     = ise_kernel(w_hyp, l_hyp, Rii)         #squared exponential kernel applied to output data
    β       = V @ ((Kid @ V) / Λ).T                # inv(Kdd) @ Kid
    μ_post  = (Kid @ α)                            #calculate posterior mean
    Σ_post  = Kii - Kid @ β                        #calculate posterior covariance
    σ2_post = maximum(0.0, diag(Σ_post))           #posterior variance
    σ_post  = sqrt(σ2_post)                        #posterior standard deviation
    return μ_post, σ_post 
