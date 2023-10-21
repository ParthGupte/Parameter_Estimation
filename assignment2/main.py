from matrix_tools import *
from img_tools import *
from grid import *
# note to self everything other than Line is generalisable to n dims in this code
def prod(lst):
    p = 1
    for a in lst:
        p *= a
    return p

def arr_indx_to_lst_indx(indx,arr_shape):
    lst_idx = 0
    for i in range(len(indx)):
        lst_idx += indx[i]*prod(arr_shape[:i])
    return lst_idx

def lst_indx_to_arr_indx(indx,arr_shape):
    arr_idx = []
    for i in range(len(arr_shape)-1,-1,-1):
        m = prod(arr_shape[:i])
        idx = indx//m
        indx = indx%m
        arr_idx.append(idx)
    arr_idx.reverse()
    return arr_idx
     
img_name = "creeper32bit.png"

img = get_img(img_name)
arr = get_array(img)

# img.show()
img_shape = arr.shape
print(img_shape)
new_img = Image.fromarray(arr)
# new_img.show()

#making grid for passing light
grid = Grid(1,dim=2)
#defining source points on all 4 sides of the img
source_pts = [(-0.5,img_shape[1]/2),(img_shape[0]/2,-0.5),(img_shape[0]+0.5,img_shape[1]/2),(img_shape[0]/2,img_shape[1]+0.5)]
cells_information = []
for source in source_pts:
    print(source)
    for deg in range(0,180,2):
        line = Line(deg,source)
        cells = get_crossing_cells(grid,line,((0,img_shape[0]),(0,img_shape[1])))
        # print(cells)
        cells_information.append(cells)

#making F and d
F = np.zeros((len(cells_information),prod(img_shape)))

for i in range(len(cells_information)):
    print(i)
    cells = cells_information[i] 
    for cell in cells:
        lst_idx = arr_indx_to_lst_indx(cell,img_shape)
        F[i,lst_idx] = 1


m_real = np.reshape(arr,(prod(img_shape),1))

d = np.matmul(F,m_real)

m_est = tikonov_est(F,d)
est_arr = np.reshape(m_est,img_shape)
est_img = Image.fromarray(est_arr)
est_img.show()

# # # arr_idx = (10,5)
# # arr_shape = (11,6)
# lst_idx = arr_indx_to_lst_indx(arr_idx,arr_shape)
# print(lst_idx)
# new_arr_idx = lst_indx_to_arr_indx(lst_idx,arr_shape)
# print(new_arr_idx)