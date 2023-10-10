from polyfit_helper import *

np.random.seed(1)

poly = generate_random_model(3,(-10,10))
F, d = gen_random_data(poly)

#svd

svd = np.linalg.svd(F)
U = svd[0]
print(U.shape,F.shape)
S = svd[1]
r = sum(S!=0)
U_0 = U[:,r+1:]
print(U_0.shape)
d_0 = np.matmul(U_0,np.random.uniform(low = -3000, high = 3000,size = (15,1))) 

d_new = d+d_0
old_model = estimate_model_L2(F,d)
plot_data(F,d,'red')
plot_model(old_model,"Old data plot","red")
new_model = estimate_model_L2(F,d_new)
plot_model(new_model,"New data plot","blue")
plot_data(F,d_new,"blue")
plt.show()


