from random import randint

words = [
    'Nepal', 'China', 'Bhutan', 'America', 'Russia', 'Japan', 'Korea', 'India', 'UK', 'Australia', 'Canada'
]

def customize(word):
    edited_word = randint(0, len(words) -1)
    return f'{word} {words[edited_word]}'
paragraphs = int(input("Enter the number of paragraphs you want:"))

with open('write.txt') as file:
    individual_words = file.read().split()

    for n in range(paragraphs):
        final_text = list(map(customize, individual_words))

        with open('project_output.txt', 'a') as final_file:
            final_file.write(' '.join(final_text) + '\n\n\n')
