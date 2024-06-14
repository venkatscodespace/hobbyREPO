def split_and_join(line):
    l=line.split()
    final_result='-'.join(l)
    return final_result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
