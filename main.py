def book_process(path):
    with open(path) as f:
        text = f.read()
        return text

def count_words(text):
    word_count = len(text.split())
    return word_count

if __name__ == '__main__':
    path = 'books/frankenstein.txt'
    text = book_process(path)
    word_count = count_words(text)
