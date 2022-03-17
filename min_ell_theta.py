

def learn_theta(data, colors):

    min_red = float('inf')
    max_blue = float('-inf')

    for n in range(len(data)):
        if(colors[n] == 'blue'):
            if(data[n] > max_blue):
                max_blue = data[n]
        elif(colors[n]== 'red'):
            if(data[n] < min_red):
                min_red = data[n]

    return (min_red + max_blue) / 2





def compute_ell(data, colors, theta):
    loss = 0

    for n in range(len(data)):
        if (colors[n] == 'blue'):
            if (data[n] > theta):
                loss+=1
        elif (colors[n] == 'red'):
            if (data[n] <= theta):
                loss+=1

    return loss

def minimize_ell(data,colors):

    min_ell = float('inf')
    min_index = 0
    for n in range(len(data)):
        temp_ell = compute_ell(data, colors,data[n])
        if temp_ell < min_ell:
            min_ell = temp_ell
            min_index = n

    return data[min_index]

def minimize_ell_sorted(data,colors):

    blue_gt_theta = int(len(data)/2)
    red_lte_theta = 0

    min_theta_index = 0
    min_ell = float('inf')

    for n in range(len(data)):
        if colors[n] == 'blue':
            blue_gt_theta -= 1
        elif colors[n] == 'red':
            red_lte_theta += 1

        temp_ell = blue_gt_theta + red_lte_theta
        #print(temp_ell)
        #print()
        if temp_ell < min_ell:
            min_ell = temp_ell
            min_theta_index = n
            #print("min_theta_index", min_theta_index)


    return data[min_theta_index]


#data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#colors = ['blue', 'blue', 'blue', 'blue', 'red', 'red', 'red', 'blue', 'red', 'red']
#minimize_ell_sorted(data,colors)
