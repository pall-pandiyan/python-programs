arr = list(map(int,input().strip().split()))
n = len(arr)
d = int(input())

def rotate(array,m):
    cutoff_arr = array[0:m]
    rotated_arr = array[m:] + cutoff_arr
    return (rotated_arr)


if __name__ == '__main__':
    print (rotate(arr,d))
