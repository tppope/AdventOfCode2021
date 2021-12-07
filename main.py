import day_1_sonar_sweep as day1
import day_2_dive as day2
import day_3_binary_diagnostic as day3
import day_4_giant_squid as day4
import day_5_hydrothermal_venture as day5
import day_6_lanternfish as day6
import day_7_the_treachery_of_whales as day7


def day1GetAnswers(inputDirectory):
    print("--- Day 1: Sonar Sweep ---")
    print("Count of measurements that are larger than the previous measurement is %s" % day1.getAnswerPart1(
        inputDirectory))
    print("Count of sum that are larger than the previous sum is %s" % day1.getAnswerPart2(inputDirectory))
    print("--- End of the day ---")
    print()


def day2GetAnswers(inputDirectory):
    print("--- Day 2: Dive! ---")
    print("Multiply of horizontal position and depth in Part 1 is %s" % day2.getAnswerPart1(inputDirectory))
    print("Multiply of horizontal position and depth in Part 2 is %s" % day2.getAnswerPart2(inputDirectory))
    print("--- End of the day ---")
    print()


def day3GetAnswers(inputDirectory):
    print("--- Day 3: Binary Diagnostic ---")
    print("Power consumption of the submarine is %s" % day3.getAnswerPart1(inputDirectory))
    print("Life support rating of the submarine is %s" % day3.getAnswerPart2(inputDirectory))
    print("--- End of the day ---")
    print()


def day4GetAnswers(inputDirectory):
    print("--- Day 4: Giant Squid ---")
    print("Final score of last winning board is %s" % day4.getAnswer(inputDirectory))
    print("--- End of the day ---")
    print()


def day5GetAnswers(inputDirectory):
    print("--- Day 5: Hydrothermal Venture ---")
    print("Points that do at least two lines overlap are %s" % day5.getAnswer(inputDirectory))
    print("--- End of the day ---")
    print()


def day6GetAnswers(inputDirectory):
    print("--- Day 6: Lanternfish ---")
    print("Count of lanternfish that there would be after 80 days is %s" % day6.getAnswer(inputDirectory))
    print("--- End of the day ---")
    print()


def day7GetAnswers(inputDirectory):
    print("--- Day 7: The Treachery of Whales ---")
    print("To align in same positions crabs must spend %s fuel" % day7.getAnswer(inputDirectory))
    print("--- End of the day ---")
    print()


if __name__ == '__main__':
    # day1GetAnswers('input/day_1_sonar_sweep/input.txt')
    # day2GetAnswers('input/day_2_dive/input.txt')
    # day3GetAnswers('input/day_3_binary_diagnostic/input.txt')
    # day4GetAnswers('input/day_4_giant_squid/input.txt')
    # day5GetAnswers('input/day_5_hydrothermal_venture/input.txt')
    # day6GetAnswers('input/day_6_lanternfish/input.txt')
    day7GetAnswers('input/day_7_the_treachery_of_whales/input.txt')
