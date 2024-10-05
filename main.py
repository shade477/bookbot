def book_process(path):
    with open(path) as f:
        text = f.read()
        return text

def count_words(text):
    word_count = len(text.split())
    return word_count

def char_count(strings):
    count = {}
    for c in strings:
        c.lower()
        if ord('a') <= ord(c) <= ord('z'):
            count[c] = 1 + count.get(c, 0)  
    return count

def display(obj):
    print(obj)

if __name__ == '__main__':
    path = 'books/frankenstein.txt'
    text = book_process(path)
    word_count = count_words(text)
    display(word_count)
    chars = char_count(text)
    display(chars)
