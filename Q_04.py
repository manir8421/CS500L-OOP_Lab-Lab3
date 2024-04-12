
# 20099_Maniruzzaman_Md_lab3
# Week_03/lab_03/Q_04
# Question: program prompts students to enter whether they like or dislike a particular food ...

def main():
    print("Electronics Lunch Menu Survey")
    votes = [
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
    ]

    menu = ["Pizza", "Hot Dog", "Ham", "Cheese"]

    while True:
        for i in range(len(menu)):
            ans = input(f"Do you like {menu[i]} (y/n)?")
            if ans.lower() == "y":
                votes[i][0] += 1
            else:
                votes[i][1] += 1

        conf = input("Do you want another student to vote (y/n)?")
        if conf.lower() != "y":
            break

    print("\n\t\tLike\tDislike\n")

    for i in range(len(menu)):
        print(f"{menu[i]}\t\t{votes[i][0]}\t{votes[i][1]}")

if __name__ == "__main__":
    main()

