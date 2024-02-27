def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        print(f"{len(words)} words found in the document")
        characterCount(file_contents)

def sort_on(dict):
    return dict["num"]

def characterCount(file_contents):

    # Initialize an empty dictionary
    char_counts = {}

    for char in file_contents:
        char = char.lower()
        if char.lower().isalpha():
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1

    listofdict = [{"letter": key, "num": val} for key, val in char_counts.items()]
    listofdict.sort(reverse=True, key=sort_on)
    
    for dictionary in listofdict:
        letter = dictionary["letter"]
        num = dictionary["num"]
        print(f"The '{letter}' character was found {num} times")

main()
