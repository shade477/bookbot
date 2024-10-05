def book_process(path):
    with open(path) as f:
        text = f.read()
        return text

def count_words(text):
    word_count = len(text.split())
    return word_count

def get_char_count(strings):
    count = {}
    for c in strings:
        c.lower()
        if ord('a') <= ord(c) <= ord('z'):
            count[c] = 1 + count.get(c, 0)  
    return count

def display_report(path):
    text = book_process(path)
    word_count = count_words(text)
    msg = f'--- Begin report of {path} ---'
    display(msg)
    msg = f'{word_count} words found in the document'
    display(msg)
    char_count = get_char_count(text)
    for k, v in char_count.items():
        display(f"The '{k}' character was found {v} times")

def display(obj):
    print(obj)

if __name__ == '__main__':
    path = 'books/frankenstein.txt'
    # text = book_process(path)
    # word_count = count_words(text)
    # display(word_count)
    # chars = char_count(text)
    # display(chars)
    display_report(path)

