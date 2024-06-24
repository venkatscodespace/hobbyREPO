def swap_case(s):
    if len(s) in range(1,1001):
        return s.swapcase()
    
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
