import json
import random
import time

def evaluate_accuracy(
    solution_sentence,
    attempted_sentence
):
    points = 0
    total = 0
    current_character_index = 0


    while current_character_index < len(solution_sentence):
        
        if current_character_index < len(attempted_sentence):
            if solution_sentence[ current_character_index ] == attempted_sentence[ current_character_index ]:
                points += 1
 
        total += 1
        current_character_index += 1

    return points / total

def sentence_builder(
    number_of_words,
    punctuation_included
):

    punctuation_list = [".", "?", "!", ",", ";", ":"]
    
    with open("words_dictionary.json") as word_dictionary_file:
        list_of_words = list( json.load( word_dictionary_file ).keys() )

    sentence = random.choices(list_of_words, k = number_of_words)

    if punctuation_included:
        
        number_of_punctuation_marks = number_of_words // 15
        
        for i in range(0, number_of_punctuation_marks - 1):
            sentence[i] = f"{ sentence[i] }{ random.choice(punctuation_list) }"

        random.shuffle(sentence)

        sentence[-1] = f"{ sentence[-1] }{ random.choice(punctuation_list) }"

    return " ".join(sentence).strip() # Convert the list of words to a single string joined by spaces
                                      #     ...and remove any trailing spaces

def calculate_score(
    accuracy,
    number_of_words,
    punctuation_included,
    words_per_minute
):
    scale_factor = 1

    if punctuation_included:
        scale_factor = 1.5

    score = (accuracy**3) * number_of_words * (words_per_minute**2) * scale_factor / 10

    return round(score)

def main():
    
    print("== SPEED TYPER ==\n")
    print("How fast can you type?")
    print("1: Short - 15 words [default]")
    print("2: Medium - 30 words")
    print("3: Long - 45 words")

    length_choice = input("Pick a length from 1-3: ")

    if length_choice not in ["1", "2", "3"]:
        length_choice = "1"

    number_of_words = int(length_choice) * 15

    punctuation_choice = input("\nDo you want to include punctuation? (y/n): ").upper()

    punctuation_included = False

    if punctuation_choice != "":
        if punctuation_choice[0] == "Y":
            punctuation_included = True

    solution_sentence = sentence_builder(
        number_of_words = number_of_words,
        punctuation_included = punctuation_included
    )
    
    input("\nReady when you are! Press enter to reveal your sentence. The timer starts immediately when you do!")

    print(f"\n{ solution_sentence }")

    start_time = time.time() #INFO: time is in seconds
    attempted_sentence = input("\n")
    end_time = time.time()

    minutes_elapsed = (end_time - start_time) / 60

    words_per_minute = len( attempted_sentence.split(" ") ) / minutes_elapsed

    accuracy = evaluate_accuracy(
        solution_sentence = solution_sentence,
        attempted_sentence = attempted_sentence
    )

    score = calculate_score(
        accuracy = accuracy,
        number_of_words = number_of_words,
        punctuation_included = punctuation_included,
        words_per_minute = words_per_minute
    )

    print(f"\nYour final score is: {score}!")

    
    

if __name__ == "__main__":
    main()
