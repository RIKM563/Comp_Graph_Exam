import matplotlib.pyplot as plt


def find_maxes(Xa, Xb, Xc, Ya, Yb, Yc):
    Ymax = max(Ya, Yb, Yc)
    Xmax = max(Xa, Xb, Xc)
    return Ymax, Xmax


def point_in_triangle(Xa, Xb, Xc, Ya, Yb, Yc, x, y):
    s1 = (Xa - x) * (Yb - Ya) - (Xb - Xa) * (Ya - y)
    s2 = (Xb - x) * (Yc - Yb) - (Xc - Xb) * (Yb - y)
    s3 = (Xc - x) * (Ya - Yc) - (Xa - Xc) * (Yc - y)
    if (s1 <= 0 and s2 <= 0 and s3 <= 0) or (s1 >= 0 and s2 >= 0 and s3 >= 0):
        return True
    else:
        return False


def shading(Xa, Xb, Xc, Ya, Yb, Yc):
    triangle_K = []
    Ymax, Xmax = find_maxes(Xa, Xb, Xc, Ya, Yb, Yc)
    for y in range(1, Ymax+1):
        for x in range(1, Xmax+1):
            flag = point_in_triangle(Xa, Xb, Xc, Ya, Yb, Yc, x, y)
            if flag == True:
                triangle_K.append([x, y])
    return triangle_K


if __name__ == '__main__':
    data = input()
    data = data.split()
    list = shading(int(data[0]), int(data[2]), int(data[4]), int(data[1]), int(data[3]), int(data[5]))
    for i in list:
        plt.plot(i[0], i[1], 'ro')
    plt.show()
