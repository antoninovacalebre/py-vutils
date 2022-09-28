def dict2mat(mat, s):
    a = s.split('.')
    temp = mat[a[0]][0, 0]
    for i in range(1, len(a) - 1):
        temp = temp[a[i]][0, 0]
    temp = temp[a[len(a) - 1]]
    if(len(temp) == 1 and len(temp[0]) == 1):
        temp = temp[0, 0]
    return temp

if __name__ == "__main__":
    pass