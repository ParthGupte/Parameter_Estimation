import numpy as np
import matplotlib.pyplot as plt
import csv
import random as rd

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
    u = 1
    F_og, d_og = F.copy(), d.copy()
    while True:
        m = estimate_model_L2(F,d)
        plot_model(m,"iter "+str(u))
        m_L.append(m)
        if len(m_L) >2:
            del m_L[0]
        if len(m_L) == 2:
            t = L2_norm(m_L[1]-m_L[0])/(1+L2_norm(m_L[1]))
            if t<t_0:
                break
        r = d - np.matmul(F,m)
        R = np.zeros((r.shape[0],r.shape[0]))
        # print(F.transpose().shape,R.shape,d.shape)
        for i in range(r.shape[0]):
            R[i,i] = 1/abs(r[i][0])
        F, d = np.matmul(np.matmul(F.transpose(),R),F), np.matmul(np.matmul(F.transpose(),R),d)
        u += 1
    # plot_data(F_og,d_og)
    # plt.legend()
    # plt.title("Q2 plots of L1 iterations")
    # # plt.savefig("assignment1/figs/L1iterplot.png")
    # plt.show()
    # return m

def F_dagger_L2(F:np.ndarray):
    return np.matmul(np.linalg.inv(np.matmul(F.transpose(),F)),F.transpose())

def numpy_to_csv(arr:np.ndarray):
    f = open("assignment1//model_table.csv","w")
    writer = csv.writer(f)
    writer.writerow(["True Model","Estimated Model"])
    for i in range(arr.shape[0]):
        row = arr[i]
        writer.writerow(row)
    f.close()


def numpy_to_csv_Q2(arr:np.ndarray):
    f = open("assignment1//model_table_Q2.csv","w")
    writer = csv.writer(f)
    writer.writerow(["True Model","L1 Estimated Model", "L2 Estimated Model"])
    for i in range(arr.shape[0]):
        row = arr[i]
        writer.writerow(row)
    f.close()


def numpy_to_csv_Q3(arr:np.ndarray):
    f = open("assignment1//model_table_Q3.csv","w")
    writer = csv.writer(f)
    writer.writerow(["True Model","Estimated Model"])
    for i in range(arr.shape[0]):
        row = arr[i]
        writer.writerow(row)
    f.close()

def plot_model(m:np.ndarray,label:str,color:str):
    P = list(m.transpose()[0])
    P.reverse()
    poly_obj = np.poly1d(P)
    X = np.linspace(-10,10,100)
    plt.plot(X,poly_obj(X),label = label,c = color)   

def plot_data(F,d,color,label = 'Noisy Data'):
    plt.scatter(list(F[:,1]),list(d),color = color,label = label)    

def plot_data_Q3(F,d,L,label = 'Noisy Data'):
    colors = ['r']*F.shape[0]
    for i in L:
        colors[i] = 'g'
    plt.scatter(list(F[:,1]),list(d),c = colors,label = label)    

def matrix_img(M:np.ndarray,title:str):
    plt.imshow(M)
    plt.title(title)
    plt.colorbar()







