def main():
    path_to_file = "books/frankenstein.txt"
    contents = get_book_contents(path_to_file)
    word_count = count_words(contents)
    word_dict = count_word(contents)
    report = get_report(word_dict)
    # print(contents)
    
    # print(count_words(contents))
    
    # print(word_dict)
    
    print(f"--- Begin report of {path_to_file} --- \n")
    print(f"{word_count} words found in the document \n\n")
    print(report)
    print("--- End report ---")

        
def get_book_contents(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    

def count_words(string):
    return len(string.split())


def count_word(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = {}
    
    for letter in alphabet:
        string = string.lower()
        
        for word in string:
            if letter in word:
                if letter in result:
                    result[letter] += 1
                else:
                    result[letter] = 1
    
    return result
    
    
def get_report(dict):
    found = ""
    for key, value in dict.items():
        found += f"The {key} character was found {value} times \n"
    
    return found


main()