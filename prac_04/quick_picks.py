import random
quick_pick_line = []
count = 0
number_of_lines = int(input("How many quick picks: "))
while number_of_lines != 0:
    while count < 6:
        random_number = random.randint(1, 45)
        if random_number not in quick_pick_line:
            quick_pick_line.append(random_number)
            count += 1
    print(quick_pick_line)
    quick_pick_line.clear()
    count = 0
    number_of_lines -= 1
