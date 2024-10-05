if __name__ == '__main__':
    with open('books/frankenstein.txt') as f:
        text = f.read()
        words = text.split()
        print(len(words))
