def count_python(paragraph):
    words = paragraph.lower().split()
    return words.count("python")


paragraph = input("Enter a paragraph: ")

count = count_python(paragraph)

print(f'The word "python" appears {count} time(s).')