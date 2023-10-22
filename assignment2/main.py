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

with_noise = True

img_names = ["alban-modified","aztec-modified","aztec2-modified","bee_nest_front_honey-modified","carved_pumpkin-modified","cow","creeper","fletching_table_front-modified","grass_block_side-modified","sheep","skeleton","steve","zombie"] 
for img_name in img_names:
    img = get_img(img_name+".png")
    arr = get_array(img)

    # img.show()
    img_shape = arr.shape
    print(img_shape)
    new_img = Image.fromarray(arr)
    # new_img.show()

    #making grid for passing light
    grid = Grid(1,dim=2)

    #passing light
    cells_information = []
    # light passing from below to up
    for x in range(img_shape[0]):
        source = (x+0.5,-1)
        ray = Line(91,source)
        cells = get_crossing_cells(grid,ray,((0,img_shape[0]),(0,img_shape[1])))
        cells_information.append(cells)
    #light passing from left to right
    for y in range(img_shape[1]):
        source = (-1,y+0.5)
        ray = Line(1,source)
        cells = get_crossing_cells(grid,ray,((0,img_shape[0]),(0,img_shape[1])))
        cells_information.append(cells)

    #light passing from diagonals
    line1 = Line(135,(-1,-1))
    num_sources = int(2*mt.ceil((img_shape[0]**2 + img_shape[1]**2)**(1/2)))
    sources = line1.get_points_distanced(0.5,num_sources)
    sources.extend(line1.get_points_distanced(-0.5,num_sources))
    for source in sources:
        ray = Line(45,source)
        cells = get_crossing_cells(grid,ray,((0,img_shape[0]),(0,img_shape[1])))
        cells_information.append(cells)

    line2 = Line(45,(img_shape[0]+1,img_shape[1]+1))
    sources = line2.get_points_distanced(0.5,num_sources)
    sources.extend(line2.get_points_distanced(-0.5,num_sources))
    for source in sources:
        ray = Line(135,source)
        cells = get_crossing_cells(grid,ray,((0,img_shape[0]),(0,img_shape[1])))
        cells_information.append(cells)





    #making F and d
    F = np.zeros((len(cells_information),prod(img_shape)))

    for i in range(len(cells_information)):
        # print(i)
        cells = cells_information[i] 
        for cell in cells:
            lst_idx = arr_indx_to_lst_indx(cell,img_shape)
            F[i,lst_idx] = 1


    m_real = np.reshape(arr,(prod(img_shape),1))

    d = np.matmul(F,m_real)
    if with_noise:
        img_name += "_noise"
        d = d + 0.05*d*np.random.normal(0,1,d.shape)

    print(F.shape)
    F_dag = tikonov_inverse(F)
    m_est = np.matmul(F_dag,d)
    model_res = np.matmul(F_dag,F)
    data_res = np.matmul(F,F_dag)
    matrix_img(model_res,"Model Resolution Matrix ("+img_name+")")
    plt.savefig("images/outputs/modelres/"+img_name)
    plt.show()
    matrix_img(data_res,"Data Resolution Matrix ("+img_name+")")
    plt.savefig("images/outputs/datares/"+img_name)
    plt.show()
    est_arr = np.reshape(m_est,img_shape)
    print(est_arr.shape)
    est_img = Image.fromarray(est_arr)
    est_img.show()
    est_img = est_img.convert('RGB')
    if with_noise:
        est_img.save("images/outputs/noise/"+img_name+".png")
    else:
        est_img.save("images/outputs/"+img_name+".png")

# # # arr_idx = (10,5)
# # arr_shape = (11,6)
# lst_idx = arr_indx_to_lst_indx(arr_idx,arr_shape)
# print(lst_idx)
# new_arr_idx = lst_indx_to_arr_indx(lst_idx,arr_shape)
# print(new_arr_idx)