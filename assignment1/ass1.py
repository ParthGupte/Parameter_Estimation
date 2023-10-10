from polyfit_helper import *

np.random.seed(0)
#Q1
m = generate_random_model(3,(-10,10)) # generated a random model
F, d = gen_random_data(m) #generate random data with noise for said model
m_est = estimate_model_L2(F,d) #estimate model from data
plot_data(F,d)
plot_model(m_est,"L2 estimate")
plt.legend()
plt.title("Q1")
# plt.savefig("assignment1/figs/Q1plot.png")
plt.show()


F_dggr = F_dagger_L2(F)
data_res_matrix = np.matmul(F,F_dggr)
matrix_img(data_res_matrix,"Data Resolution Matrix")
# plt.savefig("assignment1/figs/Q1dataresmtrix.png")
plt.show()

model_res_matrix = np.matmul(F_dggr,F)
matrix_img(model_res_matrix, "Model Resolution Matrix")
# plt.savefig("assignment1/figs/Q1modelresmatrix.png")
plt.show()

#save model values
M = np.concatenate((m,m_est),axis=1)
numpy_to_csv(M)

#Q2
d_copy = d.copy()
d_copy[0] += 500 # adding outlier
m_est_L1 = estimate_model_L1(F,d_copy,0.5)
m_est_L2 = estimate_model_L2(F,d_copy)
plot_data(F,d_copy,"Data with Outlier")
plot_model(m_est_L1,"L1 estimate")
plot_model(m_est_L2,"L2 estimate")
plt.legend()
plt.title("Q2")
# plt.savefig("assignment1/figs/Q2plots.png")
plt.show()

#save model values
numpy_to_csv_Q2(np.concatenate((m,m_est_L1,m_est_L2),axis=1))

#Q3

no_of_const_pts = 2
p,q = F.shape
idx_F = list(range(p))
L = list(np.random.choice(idx_F,no_of_const_pts))
G = F[L]
h = d[L]
not_L = []
for x in idx_F:
    if x not in L:
        not_L.append(x)
G_0 = F[not_L]
d_0 = d[not_L]
G_0TG_0 = np.matmul(G_0.transpose(),G_0)
GT = G.transpose()

k = G_0.shape[1]
l = G.shape[0]
A = np.zeros((k+l,k+l))
A[:k,:k] = G_0TG_0
A[:k,k:] = GT
A[k:,:k] = G

G_0Td_0 = np.matmul(G_0.transpose(),d_0)

Y = np.zeros((k+l,1))
Y[:k] = G_0Td_0
Y[k:] = h

m_contr_est = np.matmul(np.linalg.inv(A),Y)[:k]

plot_data_Q3(F,d,L)
plot_model(m_contr_est,"Constrained L2 estimate")
plt.legend()
plt.title("Q3 Green points are the constraint points")
# plt.savefig("assignment1/figs/Q3plots.png")
plt.show()

#save model values
numpy_to_csv_Q3(np.concatenate((m,m_contr_est),axis=1))
