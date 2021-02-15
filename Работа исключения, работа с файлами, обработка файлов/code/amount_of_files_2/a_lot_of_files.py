def count_words(filename):
    """Считает количество строк в файле"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"В этом {filename} около {num_words} слов.")


filenames = ['evgini-onegin.txt', 'prestuplenie-i-nakaznia.txt',
             'voyna-i-mir.txt']
for filename in filenames:
    count_words(filename)
