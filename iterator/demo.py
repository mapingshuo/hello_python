
def iter1():
    a = [-1]
    for i in range(5):
        yield a
        a.append(i)

def iter2():
    a = [-1]
    for i in range(5):
        b = a[:]
        yield b
        a.append(i)

def batch(reader, batch_size=5):
    def batch_reader():
        r = reader()
        b = []
        for instance in r:
            b.append(instance)
            if len(b) == batch_size:
                yield b
                b = []
    return batch_reader

def main():
    batch_reader = batch(iter1)
    for data in batch_reader():
        print(data)

    batch_reader = batch(iter2)
    for data in batch_reader():
        print(data)
    
if __name__ == "__main__":
    main()
