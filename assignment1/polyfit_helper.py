import numpy as np
import matplotlib.pyplot as plt
import csv

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
    F = np.concatenate([f_0**i for i in range(len(m))], axis=1)
    d_true = np.matmul(F,m) 
    d = d_true + noise*d_true*np.random.normal(0,1,d_true.shape)
    return F,d

def L2_norm(V:np.ndarray):
    S = (sum(V**2)/len(V))**(1/2)
    return S

def estimate_model_L2(F:np.ndarray,d:np.ndarray):
    '''
    Estimates the model using L2 norm minimisation formula for full coloumn rank matrices
    '''
    m_est = np.matmul(np.matmul(np.linalg.inv(np.matmul(F.transpose(),F)),F.transpose()),d)
    return m_est

def estimate_model_L1(F:np.ndarray,d:np.ndarray,t_0):
    '''
    Estimates the model using L1 norm minimisation algorithm
    '''
    m_L = []
    while True:
        m = estimate_model_L2(F,d)
        m_L.append(m)
        if len(m_L) >2:
            del m_L[0]
        if len(m_L) == 2:
            t = L2_norm(m_L[1]-m_L[0])/(1+L2_norm(m_L[1]))
            if t<t_0:
                break
        r = d - np.matmul(F,m)
        R = np.zeros((r.shape[0],r.shape[0]))
        print(F.transpose().shape,R.shape,d.shape)
        for i in range(r.shape[0]):
            R[i,i] = 1/abs(r[i][0])
        F, d = np.matmul(np.matmul(F.transpose(),R),F), np.matmul(np.matmul(F.transpose(),R),d)

    return m
    
def plot_model():
    pass
     

def numpy_to_csv(arr:np.ndarray):
    f = open("assignment1//model_table.csv","w")
    writer = csv.writer(f)
    writer.writerow(["True Model","Estimated Model"])
    for i in range(arr.shape[0]):
        row = arr[i]
        writer.writerow(row)
    f.close()


np.random.seed(0)
#Q1
m = generate_random_model(3,(-10,10)) # generated a random model
F, d = gen_random_data(m) #generate random data with noise for said model
m_est = estimate_model_L2(F,d) #estimate model from data
F_est, d_est = gen_random_data(m_est,70,0) # generate data points for estimated model

#save model values
M = np.concatenate((m,m_est),axis=1)
numpy_to_csv(M)

#Q2
d[0] += 500 # adding outlier
m_est_L1 = estimate_model_L1(F,d,0.5)
m_est_L2 = estimate_model_L2(F,d)



plt.scatter(list(F[:,1]),list(d))
# plt.scatter(list(F_est[:,1]),list(d_est))
plt.show()
