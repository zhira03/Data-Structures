from hashmaps import HashMap

def word_counter(text):
    word_map = HashMap()

    try:
        with open(text, 'r') as file:
            for line in file:
                words = line.strip().lower().split()
                for word in words:
                    word = ''.join(char for char in word if char.isalnum())
                    if word:
                        if word in word_map:
                            word_map[word] += 1
                        else:
                            word_map[word] = 1
    except FileNotFoundError:
        print(f"File {text} not found.")
        return None
    
    return word_map.__str__()

word_map = word_counter("C:\\Users\\HomePC\\Documents\\randoms.txt")
print(word_map)