def jumpingOnClouds(c):
    # Write your code here
    jump = 0
    index = len(c)-1
    for i in range(len(c)-1,-1,-1):
        if index == 0:
            break
        if c[index-2] == 0 and index > 1:
            index -= 2 
            jump += 1
        elif c[index-1] == 0 and index > 0:
            index -= 1
            jump += 1


    return jump

if __name__ == '__main__':

    n = 7
    c = [0,0,1,0,0,1,0]
    result = jumpingOnClouds(c) # 4， 跳了4次
    print(result)
    n = 7
    c = [0,1,0,0,0,1,0]
    result = jumpingOnClouds(c) # 3， 跳了3次
    print(result)
