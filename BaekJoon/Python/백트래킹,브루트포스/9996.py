import sys

N = int(sys.stdin.readline())

pattern = sys.stdin.readline().rstrip()

star_index = pattern.index(chr(42))
s_left = pattern[:star_index]
s_right = pattern[star_index+1:]


for i in range(N):
    file_name = sys.stdin.readline().strip()
    
    if len(file_name) >= len(s_left) + len(s_right):
    
        if star_index != 0 and star_index != len(pattern) - 1:
            if s_left == file_name[:len(s_left)] and s_right == file_name[len(file_name)-len(s_right):]:
                print("DA")    
            else:
                print("NE")
        else:
            if star_index == 0:
                if s_right == file_name[len(file_name)-len(s_right):]:
                    print("DA")
                else:
                    print("NE")
            elif star_index == len(pattern) - 1:
                if s_left == file_name[:len(s_left)]:
                    print("DA")
                else:
                    print("NE")
    else:
        print("NE")