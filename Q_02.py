
# 20099_Maniruzzaman_Md_lab3
# Week_03/lab_03/Q_02
# Question: program allows user to enter a scores and then choose to find the smallest, largest, sum, average or mode


MIN_SCORE = 0
MAX_SCORE = 10

# Get a list of scores from the keyboard

def get_score_list():
    #pass
    scores = input(f"Please enter a list of scores between {MIN_SCORE} and {MAX_SCORE} separated byspaces: ")
    scores = scores.split(" ")
    scores_list = []
    for score in scores:
        scores_list.append(int(score))
    return scores_list


# Find the smallest, largest, sum, avarage and mode

def process_scores(score_list):
    # pass
    sm = MAX_SCORE + 1
    lg = MIN_SCORE - 1
    sum = 0
    
    for score in score_list:
        if score < sm:
            sm = score
        if score > lg:
            lg = score
        sum += score

    average = sum / len(score_list)

    # Create a frequency array
    freq = [0] * (MAX_SCORE - MIN_SCORE +1)
    
    for score in score_list:
        freq[score] += 1

    mode = 0
    for i in range(len(freq)):
        if freq[i] > freq[mode]:
            mode = i

    return sm, lg, sum, average, mode

def show_menu():
    print("\n=== MENU ===")
    print("1. Find the smallest score")
    print("2. Find the largest score")
    print("3. Find the total score")
    print("4. Find the average score")
    print("5. Find the mode (most frequent) score")
    print("6. exit")

def main():
    # Print the program title
    print("Finding the smallest,largest, sum, average or mode")

    # Get a list of scores
    score_list = get_score_list()

    # process scores

    sm, lg, sum, average, mode = process_scores(score_list)

    while True:
        show_menu()
        choice = int(input("\nEnter your choice\t\t\t: "))
        if choice == 1:
            print("The smallest score is\t\t\t:", sm)
        elif choice == 2:
            print("The largest scoce is\t\t\t:", lg)
        elif choice == 3:
            print ("The sum score is\t\t\t:", sum)
        elif choice == 4:
            print(f"The average score is\t\t\t: {average:.2f}")
        elif choice == 5:
            print("The mode (most frequent score) is\t:", mode)
        elif choice == 6:
            print("Bye")
            break

if __name__ == "__main__":
    main()