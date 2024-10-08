# There is no need to import SAMPLE_MATRICES
# YOUR CODE AND HEADING HERE
#Kieran Uptagrafft
#U2 Lab 4 
#10/7/24

def mat_sum(m1, m2):
    width1 = None
    height2 = 0
    width2 = None
    height1 = 0
    for x in m1:
        width1 = len(x)
        height1 += 1
    for x in m2:
        width2 = len(x)
        height2 += 1
    new = [[0]*width2 for i in range(height1)]
    if width1 != width2 or height1 != height2:
        return "no solution"
    else:
        for x, y in enumerate(new):
            for z in range(width1):
                new[x][z] = m1[x][z] + m2[x][z]
        return new

    



def mat_mul(m1, m2):
    width1 = None
    height2 = 0
    width2 = None
    height1 = 0
    for x in m1:
        width1 = len(x)
        height1 += 1
    for x in m2:
        width2 = len(x)
        height2 += 1
    new = [[0]*width2 for i in range(height1)]
    if width1 != height2:
        return "no solution"
    else:
        for x in range(len(m1)):
            for y in range(len(m2[0])):
                for z in range(len(m2)):
                    new[x][y] += m1[x][z] * m2[z][y]

        
        return new
