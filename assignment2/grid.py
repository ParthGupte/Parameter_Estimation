import math as mt
# module for grid making and using the grid
''' 
class makes a grid with cells numbered as (x,y,z) with no central cell
The has centroid as coordinate point (0,0,0) is located at the intercetion of 8 cells 
Grid extends infinitely on all sides 
Cells are represented as a tuple of integers
'''

class Grid:
    def __init__(self,cell_dims,dim = 3):
        if not isinstance(cell_dims,tuple):
            self.is_cubic = True
            self.cell_size = cell_dims
            self.cell_dims = tuple([self.cell_size]*dim)
        else:
            self.is_cubic = False
            self.cell_dims = cell_dims
        self.dim = dim
    def get_cell(self, coords): #returns which cell the coords belong to
        if not isinstance(coords,tuple):
            raise Exception("Please enter a tuple")
        elif len(coords) != self.dim:
            raise Exception("Coordinate of ",self.dim,"dimensions expected")
        else:
            cell = []
            for i in range(self.dim):
                x = coords[i] 
                cell.append(int(x//self.cell_dims[i]))
        return tuple(cell)
    
    def get_cell_center(self,cell): #returns the center of the cell
        center_coords = []
        for i in range(self.dim):
            l = self.cell_dims[i]*cell[i]
            if l > 0:
                coord = l - 0.5*self.cell_dims[i]
            else:
                coord = l + 0.5*self.cell_dims[i]
            center_coords.append(coord)
        return tuple(center_coords)

class Line:
    #creates a line passing through a point and having angle theta with +X axis (counter clockwise in degrees)
    def __init__(self,theta,point):
        self.theta = theta
        self.point = point
        self.m = mt.tan(mt.radians(theta))
        self.c = point[1]-self.m*point[0]
    
    def y(self,x): 
        return self.m*x+self.c
    
    def x(self,y):
        return (y-self.c)/self.m
    
    def get_point(self,d): #point at distance d from source
        x0, y0 = self.point[0], self.point[1]
        cstheta = mt.cos(mt.radians(self.theta))
        sntheta = mt.sin(mt.radians(self.theta))
        x, y = x0 + d*cstheta, y0 + d*sntheta
        return x,y
    
    def get_points_distanced(self,s,n): #n points equally distanced (s) from source 
        points = []
        for i in range(n):
            d = (i+1)*s
            points.append(self.get_point(d))
        return points
    
    def get_points_distanced_starting(self,start_dist,s,n):
        points = []
        for i  in range(n):
            d = start_dist + (i+1)*s
            points.append(self.get_point(d))
        return points

def dist(x,y):
    S = 0 
    for i,j in zip(x,y):
        S += (i-j)**2
    S **= 1/2
    return S

def get_crossing_cells(grid:Grid,line:Line,rang=((0,1000),(0,1000))): #get all the cells that the line crosses in a given range
    #0 included and 1000 not included
    sizes = []
    for pair in rang:
        sizes.append(pair[1]-pair[0])
    num_points_to_check = 0
    for s in sizes:
        num_points_to_check += s**2
    num_points_to_check **= 1/2
    num_points_to_check = int(mt.ceil(num_points_to_check))
    num_points_to_check *= 2
    points = []
    source = line.point
    pos_point1 = (rang[0][0],line.y(rang[0][0]))
    pos_point2 = (rang[0][1],line.y(rang[0][1]))
    pos_point3 = (line.x(rang[1][0]),rang[1][0])
    pos_point4 = (line.x(rang[1][1]),rang[1][1])
    pos_points = [pos_point1,pos_point2,pos_point3,pos_point4]
    to_remove = []
    for pos_point in pos_points:
        if pos_point[0] < rang[0][0] or pos_point[0] > rang[0][1] or pos_point[1] < rang[1][0] or pos_point[1] > rang[1][1]:
            to_remove.append(pos_point)
    for del_point in to_remove:
        pos_points.remove(del_point)
    if pos_points != []:
        pos_points.sort(key= lambda x: dist(source,x))
        closest_pt = pos_points[0]
        # print(closest_pt)
        start_dist = dist(source,closest_pt) - 0.5
        # print(start_dist)
        points.extend(line.get_points_distanced_starting(start_dist,0.5,num_points_to_check))
        points.extend(line.get_points_distanced_starting(start_dist,-0.5,num_points_to_check))
        points.extend(line.get_points_distanced_starting(-start_dist,-0.5,num_points_to_check))
        points.extend(line.get_points_distanced_starting(-start_dist,0.5,num_points_to_check))
    else:
        points = []
    cells = []
    for point in points:
        cell = grid.get_cell(point)
        if cell in cells:
            continue
        for i in range(len(cell)):
            c = cell[i]
            lr = rang[i][0]
            ur = rang[i][1]
            if c < lr or c >= ur:
                break
        else:
            cells.append(cell)
    
    return cells

# line = Line(90,(5.5,15))

# grid = Grid(1,dim=2)
# cells = get_crossing_cells(grid,line,((0,10),(0,10)))
# print(cells)
