if __name__ == '__main__':
    data = raw_input('your input?')
    s = set()
    for w in data.split():
        s.add(w.lower())
    for item in s:
        print(item)

