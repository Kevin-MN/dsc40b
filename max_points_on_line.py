
def max_points_on_line(list_points, point):
    max_points = 0

    if len(list_points) == 0:
        return max_points

    hash_table = {}

    for x in list_points:
        calc_slope, calc_int = calculate_slope_and_intercept(x, point)
        hash_ix = hash_line(calc_slope, calc_int)

        if (hash_ix not in hash_table):
            hash_table[hash_ix] = 1
        else:
            hash_table[hash_ix]+=1

        if(hash_table[hash_ix] > max_points):
            max_points = hash_table[hash_ix]

    return max_points




def calculate_slope_and_intercept(point1, point2):
    print(point1[0], point1[1])
    if(point1[0] - point2[0] == 0):
        return float('inf'), float('inf')
    slope = (point2[1] - point1[1]) / (point2[0] - point1[0])
    y_int = point1[1] - (slope * point1[0])
    return slope, y_int

def hash_line(slope, int):
    print(str(slope) + str(int))
    return str(slope) + str(int)






X = [(1,1), (3,1), (5,2), (3,6), (1,7), (7,4), (9,3), (9,9)]
p = (5,5)

print(max_points_on_line(X,p))

print(str(1))
print(str(-1))

