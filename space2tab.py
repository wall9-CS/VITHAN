import re 

def underbar_deletion(word):
    if re.search('_', word):
        idx = word.find("_")
        new_word = word[:idx] + word[idx+1:]
        print(new_word)
        return new_word
    else:
        return word

def space2tab(input_path, output_path):
    with open(output_path, "w") as wf:
        with open(input_path, "r") as rf:
            lines = rf.readlines()
            for line in lines:
                if len(line.split()) > 2:
                    for idx, word in enumerate(line.split()):
                        if idx % 2 == 1:
                            word = underbar_deletion(word)
                        wf.write(word+"\t")
                    wf.write("\n")

def main():
    input = "heads_with_numerics_raw.txt"   
    output = "heads_with_numerics.txt"
    space2tab(input, output)

main()


