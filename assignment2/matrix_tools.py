import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)

def tikonov_inverse(F:np.ndarray,k = 0.1):
    return np.matmul(np.linalg.inv((np.matmul(F.transpose(),F)+k*np.identity(F.shape[1]))),F.transpose())

def tikonov_est(F:np.ndarray,d:np.ndarray,k = 0.1):
    return np.matmul(tikonov_inverse(F,k),d)

def generate_random_model(deg:int,rng:tuple):
    '''
    Enter a degree and a range and a model is generated for that range and degree
    '''
    m = np.random.uniform(low = rng[0], high = rng[1], size = (deg+1,1))
    return m

def gen_random_data(model:np.ndarray,size = 20, noise = 0.1,rng = (-10,10)):
    '''
    Enter a model, and data is generated for that model with added guassian noise
    '''
    f_0 = np.random.uniform(low = rng[0], high = rng[1], size = (size,1))
    F = np.concatenate([f_0**i for i in range(len(model))], axis=1)
    d_true = np.matmul(F,model) 
    d = d_true + noise*d_true*np.random.normal(0,1,d_true.shape)
    return F,d

def plot_model(m:np.ndarray,label:str,color:str):
    P = list(m.transpose()[0])
    P.reverse()
    poly_obj = np.poly1d(P)
    X = np.linspace(-10,10,100)
    plt.plot(X,poly_obj(X),label = label,c = color)   

def matrix_img(M:np.ndarray,title:str):
    plt.imshow(M)
    plt.title(title)
    plt.colorbar()


# m = generate_random_model(6,(-1,1))
# F,d = gen_random_data(m,size =3 ,noise=0)
# m_est = tikonov_est(F,d,k=1)
# plot_model(m,"True",'g')
# # plot_model(m_est,"Est",'r')
# plt.show()