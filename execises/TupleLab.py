

def sort_by_len(aList):
    l = [(len(item), item) for item in aList]
    res = []
    for i in sorted(l):
        res.append(i[1])
    return res

if __name__ == '__main__':
    data = ['jusong', 'chen', 'something!']

    print(sort_by_len(data))
