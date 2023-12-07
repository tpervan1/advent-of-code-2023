import numpy as np
import copy


def change_letters_to_numbers1(char):
    replacement = {'T': '10', 'J': '11', 'Q': '12', 'K': '13', 'A': '14'}
    return replacement[char] if char in ('T', 'J', 'Q', 'K', 'A') else char


def change_letters_to_numbers2(char):
    replacement = {'T': '10', 'J': '0', 'Q': '12', 'K': '13', 'A': '14'}
    return replacement[char] if char in ('T', 'J', 'Q', 'K', 'A') else char


def scale_numbers(number):
    replacement = [3, 6, 9, 12]
    return replacement[number - 2] if number in range(2, len(replacement) + 2) else number


def parse_input(lines, part):
    hands = []
    for line in lines:
        cards = [*line[0]]
        if part == 1:
            cards = list(map(change_letters_to_numbers1, line[0]))
        elif part == 2:
            cards = list(map(change_letters_to_numbers2, line[0]))
        hands.append([int(num) for num in cards])
        # append bid as well
        hands[-1].append(int(line[1]))
    return hands


def part1(hands):
    for hand in hands:
        cards = hand[0:len(hand) - 1]
        values, counts = np.unique(cards, return_counts=True)
        hand.append(sum(list(map(scale_numbers, counts))))
    return hands


def part2(hands):
    for hand in hands:
        cards = hand[0:len(hand) - 1]
        # count how many cards are not jokers
        cards = list(filter(lambda count: count, cards))
        values, counts = np.unique(cards, return_counts=True)
        cards_to_add = 5 - sum(counts)
        for i, count in enumerate(counts):
            if count == max(counts):
                # add all jokers to card that repeats the most
                counts[i] += cards_to_add
        if cards_to_add == 5:
            counts = [5]
        hand.append(sum(list(map(scale_numbers, counts))))
    return hands


with open('input.txt') as f:
    lines = [line.strip().split() for line in f.readlines()]

hands = parse_input(lines, 1)
hands1 = part1(hands)
hands1.sort(key=lambda hand: (hand[-1], hand[0], hand[1], hand[2], hand[3], hand[4]))
print('Solution for part 1:', sum([(i + 1) * hand[-2] for i, hand in enumerate(hands1)]))

hands = parse_input(lines, 2)
hands2 = part2(hands)
hands2.sort(key=lambda hand: (hand[-1], hand[0], hand[1], hand[2], hand[3], hand[4]))
print('Solution for part 2:', sum([(i + 1) * hand[-2] for i, hand in enumerate(hands2)]))
