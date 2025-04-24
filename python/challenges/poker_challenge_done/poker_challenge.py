from collections import defaultdict


def python_challenge_datah():

    class PokerHand():

        def __init__(self, hand):
            self.hand = hand

        def cards(self):
            return self.hand.split(" ")

        def compare_with(self, challenge_poker_hand):

            #Dictionary that check the card signature with her value
            card_order_dict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11,
                               "Q": 12, "K": 13, "A": 14}

            #Dictionary that check the suit signature with his value
            suit_order_dict = {"S": 1, "D": 2, "C": 3, "H": 4}

            #Checking method for Royal Straight Flush
            def check_royal_straight_flush(hand):
                cards = ''.join([h[0] for h in hand])
                suits = [h[1] for h in hand]
                if cards == "TJQKA" and len(set(suits)) == 1:
                    return True
                return False

            #Checking method for Royal Straight Flush Suit
            def get_straight_flush_highest_suit(hand):
                suit_value = [h[1] for h in hand]
                suit = list(set(suit_value))
                return suit_order_dict[suit[0]]

            #Checking method for Flush
            def check_flush(hand):
                suit = set([h[1] for h in hand])
                if len(suit) == 1:
                    return True
                else:
                    return False

            #Checking method for Straight
            def check_straight(hand):
                card_values = [h[0] for h in hand]
                values_counts = defaultdict(lambda: 0)
                for v in card_values:
                    values_counts[v] += 1
                rank_values = [card_order_dict[i] for i in card_values]
                if rank_values == [2, 3, 4, 5, 14]:
                    rank_values = [1, 2, 3, 4, 5]
                value_range = max(rank_values) - min(rank_values)
                if len(set(values_counts.values())) == 1 and (value_range == 4):
                    return True
                else:
                    if set(values) == set(["A", "2", "3", "4", "5"]):
                        return True
                    return False

            #Checking method for Straight Flush
            def check_straight_flush(hand):
                if check_straight(hand) and check_flush(hand):
                    return True
                else:
                    return False

            # Checking method for Four of a Kind
            def check_four_kind(hand):
                card_values = [i[0] for i in hand]
                value_counts = defaultdict(lambda: 0)
                for v in card_values:
                    value_counts[v] += 1
                if sorted(value_counts.values()) == [1, 4]:
                    return True
                return False

            # Checking method for Four of kind highest card
            def check_four_highest_card(hand):
                card_values = [h[0] for h in hand]
                value_dict = defaultdict(lambda: 0)
                for i in set(card_values):
                    value_dict[card_values.count(i)] = i
                return card_order_dict[value_dict[4]]

            # Checking method for Full House
            def check_full_house(hand):
                card_values = [i[0] for i in hand]
                value_counts = defaultdict(lambda: 0)
                for v in card_values:
                    value_counts[v] += 1
                if sorted(value_counts.values()) == [2, 3]:
                    return True
                else:
                    return False

            # Checking method for Three of a Kind
            def check_three_kind(hand):
                card_value = [i[0] for i in hand]
                value_counts = defaultdict(lambda: 0)
                for v in card_value:
                    value_counts[v] += 1
                if set(value_counts.values()) == set([3, 1]):
                    return True
                else:
                    return False

            # Checking method for Three of a Kind highest card
            def check_three_highest_card(hand):
                card_values = [h[0] for h in hand]
                value_dict = defaultdict(lambda: 0)
                for i in set(card_values):
                    value_dict[card_values.count(i)] = i
                return card_order_dict[value_dict[3]]

            # Checking method for Two Pair
            def check_two_pair(hand):
                card_values = [i[0] for i in hand]
                value_counts = defaultdict(lambda: 0)
                for v in card_values:
                    value_counts[v] += 1
                if sorted(value_counts.values()) == [1, 2, 2]:
                    return True
                else:
                    return False

            # Checking method for One Pair
            def check_one_pairs(hand):
                card_values = [i[0] for i in hand]
                value_counts = defaultdict(lambda: 0)
                for v in card_values:
                    value_counts[v] += 1
                if 2 in value_counts.values():
                    return True
                else:
                    return False

            #Checking method for Two Pair highest card
            def check_double_pair_highest_card(hand):
                card_values = [h[0] for h in hand]
                card_list = []
                for card in card_values:
                    if card_values.count(card) == 2 and card not in card_list:
                        card_list.append(card)

                return card_order_dict[card_list[-1]]

            # Checking method for Two Pair highest card
            def check_double_pair_highest_solo_card(hand):
                card_values = [h[0] for h in hand]
                card_list = []
                for card in card_values:
                    if card_values.count(card) == 1 and card not in card_list:
                        card_list.append(card)

                return card_order_dict[card_list[-1]]

            # Checking method for Two Pair highest solo card
            def check_pair_highest_solo_card(hand):
                card_values = [h[0] for h in hand]
                card_list = []
                for card in card_values:
                    if card_values.count(card) == 1 and card not in card_list:
                        card_list.append(card)
                return card_order_dict[card_list[-1]]

            # Checking method for Pair highest card
            def check_pair_highest_card(hand):
                card_values = [h[0] for h in hand]
                for card in card_values:
                    if card_values.count(card) == 2:
                        return card_order_dict[card]

            # Checking method for highest card
            def get_highest_card(hand):
                value_poker_hand1 = [h[0] for h in hand]
                value_list = []
                for i in value_poker_hand1:
                    value_list.append(card_order_dict[i])
                return max(value_list)

            # Checking method for highest straight
            def get_straight_value(hand):
                card_value = [h[0] for h in hand]
                straight_sum = 0
                if card_value == ['2', '3', '4', '5', 'A']:
                    card_value = [1, 2, 3, 4, 5]
                    return sum(card_value)
                for card in card_value:
                    straight_sum += card_order_dict[card]

                return straight_sum

            # Checking method for Two Pair solo card highest suit
            def get_double_pair_solo_card_highest_suit(hand):
                card_value = [h[0] for h in hand]
                card_position = -1
                for card in card_value:
                    card_position += 1
                    if card_value.count(card) == 1:
                        return suit_order_dict[hand[card_position][1]]

            # Checking method solo card highest suit
            def get_pair_highest_card_suit(hand):
                card_value = [h[0] for h in hand]
                card_position = -1
                card_list = []
                for card in card_value:
                    card_position += 1
                    if card_value.count(card) == 1:
                        card_list.append(hand[card_position])

                card_suit = card_list[-1][1]
                return suit_order_dict[card_suit]

            values = dict(zip('23456789TJQKA', range(2, 15)))
            poker_hand_1 = sorted(self.cards(), key=lambda x: values[x[0]])
            poker_hand_2 = sorted(challenge_poker_hand.cards(), key=lambda x: values[x[0]])

            #1 - Royal Straight Flush
            if check_royal_straight_flush(poker_hand_1) or check_royal_straight_flush(poker_hand_2):

                if check_royal_straight_flush(poker_hand_1) and check_royal_straight_flush(poker_hand_2):
                    if get_straight_flush_highest_suit(poker_hand_1) > get_straight_flush_highest_suit(poker_hand_2):
                        return "WIN"

                    else:
                        return "LOSS"

                elif check_royal_straight_flush(poker_hand_1):
                    return "WIN"

                else:
                    return "LOSS"

            #2 - Straight Flush
            elif check_straight_flush(poker_hand_1) or check_straight_flush(poker_hand_2):

                if check_straight_flush(poker_hand_1) and check_straight_flush(poker_hand_2):

                    if get_highest_card(poker_hand_1) > get_highest_card(poker_hand_2):
                        return "WIN"

                    elif get_highest_card(poker_hand_1) == get_highest_card(poker_hand_2):
                        if get_straight_flush_highest_suit(poker_hand_1) > get_straight_flush_highest_suit(poker_hand_2):
                            return "WIN"

                        else:
                            return "LOSS"

                    else:
                        return "LOSS"

                elif check_straight_flush(poker_hand_1):
                    return "WIN"

                else:
                    return "LOSS"

            #3 - Four of a Kind
            elif check_four_kind(poker_hand_1) or check_four_kind(poker_hand_2):

                if check_four_kind(poker_hand_1) and check_four_kind(poker_hand_2):
                    if check_four_highest_card(poker_hand_1) > check_four_highest_card(poker_hand_2):
                        return "WIN"
                    else:
                        return "LOSS"

                elif check_four_kind(poker_hand_1):
                    return "WIN"

                else:
                    return "LOSS"

            #4 - Full House
            elif check_full_house(poker_hand_1) or check_full_house(poker_hand_2):

                if check_full_house(poker_hand_1) and check_full_house(poker_hand_2):

                    if check_three_highest_card(poker_hand_1) > check_three_highest_card(poker_hand_2):
                        return "WIN"
                    else:
                        return "LOSS"

                elif check_full_house(poker_hand_1):
                    return "WIN"

                else:
                    return "LOSS"

            #5 - Flush
            elif check_flush(poker_hand_1) or check_flush(poker_hand_2):

                if check_flush(poker_hand_1) and check_flush(poker_hand_2):
                    if get_highest_card(poker_hand_1) > get_highest_card(poker_hand_2):
                        return "WIN"

                    elif get_highest_card(poker_hand_1) == get_highest_card(poker_hand_2):
                        if get_straight_flush_highest_suit(poker_hand_1) > get_straight_flush_highest_suit(poker_hand_2):
                            return "WIN"

                        else:
                            return "LOSS"

                    else:
                        return "LOSS"

                elif check_flush(poker_hand_1):
                    return "WIN"

                else:
                    return "LOSS"

            #6 - Straight
            elif check_straight(poker_hand_1) or check_straight(poker_hand_2):

                if check_straight(poker_hand_1) and check_straight(poker_hand_2):
                    if get_straight_value(poker_hand_1) > get_straight_value(poker_hand_2):
                        return "WIN"

                    else:
                        return "LOSS"

                elif check_straight(poker_hand_1):
                    return "WIN"

                else:
                    return "LOSS"

            #7 - Three of kind
            elif check_three_kind(poker_hand_1) or check_three_kind(poker_hand_2):

                if check_three_kind(poker_hand_1) and check_three_kind(poker_hand_2):

                    if check_three_highest_card(poker_hand_1) > check_three_highest_card(poker_hand_2):
                        return "WIN"

                    else:
                        return "LOSS"

                elif check_three_kind(poker_hand_1):
                    return "WIN"

                else:
                    return "LOSS"

            #8 - Two Pair
            elif check_two_pair(poker_hand_1) or check_two_pair(poker_hand_2):

                if check_two_pair(poker_hand_1) and check_two_pair(poker_hand_2):

                    if check_double_pair_highest_card(poker_hand_1) > check_double_pair_highest_card(poker_hand_2):
                        return "WIN"

                    elif check_double_pair_highest_card(poker_hand_1) == check_double_pair_highest_card(poker_hand_2):

                        if check_double_pair_highest_solo_card(poker_hand_1) > check_double_pair_highest_solo_card(poker_hand_2):
                            return "WIN"

                        elif check_double_pair_highest_solo_card(poker_hand_1) == check_double_pair_highest_solo_card(poker_hand_2):

                            if get_double_pair_solo_card_highest_suit(poker_hand_1) > get_double_pair_solo_card_highest_suit(poker_hand_2):
                                return "WIN"

                            else:
                                return "LOSS"

                        else:
                            return "LOSS"

                    else:
                        return "LOSS"


                elif check_two_pair(poker_hand_1):
                    return "WIN"

                else:
                    return "LOSS"

            #9 - One Pair
            elif check_one_pairs(poker_hand_1) or check_one_pairs(poker_hand_2):

                if check_one_pairs(poker_hand_1) and check_one_pairs(poker_hand_2):

                    if check_pair_highest_card(poker_hand_1) > check_pair_highest_card(poker_hand_2):
                        return "WIN"

                    elif check_pair_highest_card(poker_hand_1) == check_pair_highest_card(poker_hand_2):

                        if check_pair_highest_solo_card(poker_hand_1) > check_pair_highest_solo_card(poker_hand_2):
                            return "WIN"

                        elif check_pair_highest_solo_card(poker_hand_1) == check_pair_highest_solo_card(poker_hand_2):

                            if get_pair_highest_card_suit(poker_hand_1) > get_pair_highest_card_suit(poker_hand_2):
                                return "WIN"

                            else:
                                return "LOSS"

                        else:

                            return "LOSS"

                    else:
                        return "LOSS"

                elif check_one_pairs(poker_hand_1):
                    return "WIN"

                else:
                    return "LOSS"

            #10 - High Card
            else:
                if get_highest_card(poker_hand_1) > get_highest_card(poker_hand_2):
                    return "WIN"

                elif get_highest_card(poker_hand_1) == get_highest_card(poker_hand_2):

                    if get_pair_highest_card_suit(poker_hand_1) > get_pair_highest_card_suit(poker_hand_2):
                        return "WIN"

                    else:
                        return "LOSS"

                else:
                    return "LOSS"

    #Test -> Must be 1º:WIN,  2º:LOSS

    #1
    print("Check Royal Straight Flush:")
    print(PokerHand("TH JH QH KH AH").compare_with(PokerHand("TC JC QC KC AC")))
    print(PokerHand("TC JC QC KC AC").compare_with(PokerHand("TH JH QH KH AH")))

    #2
    print("\nCheck Straight Flush:")
    print(PokerHand("AH 2H 3H 4H 5H").compare_with(PokerHand("AC 2C 3C 4C 5C")))
    print(PokerHand("AC 2C 3C 4C 5C").compare_with(PokerHand("AH 2H 3H 4H 5H")))

    #3
    print("\nCheck four of kind:")
    print(PokerHand("AC AD AS AH 5H").compare_with(PokerHand("KC KS KH KD 5C")))
    print(PokerHand("KC KS KH KD 5C").compare_with(PokerHand("AC AD AS AH 5H")))

    #4
    print("\nCheck full house:")
    print(PokerHand("QC QD QS 5H 5H").compare_with(PokerHand("JC JS JH 5D 5C")))
    print(PokerHand("JC JS JH 5D 5C").compare_with(PokerHand("QC QD QS 5H 5H")))

    #5
    print("\nCheck flush:")
    print(PokerHand("2H 4H 6H 5H KH").compare_with(PokerHand("2C 4C 6C 5C KC")))
    print(PokerHand("2C 4C 6C 5C KC").compare_with(PokerHand("2H 4H 6H 5H KH")))

    #6
    print("\nCheck flush:")
    print(PokerHand("2C 3D 4H 5D 6S").compare_with(PokerHand("AC 2D 3C 4D 5S")))
    print(PokerHand("AC 2D 3C 4D 5S").compare_with(PokerHand("2C 3D 4H 5D 6S")))

    #7
    print("\nThree of a kind:")
    print(PokerHand("JC JD JH AD 9S").compare_with(PokerHand("6C 6D 6H 8D 7S")))
    print(PokerHand("6C 6D 6H 8D 7S").compare_with(PokerHand("7C 7D 7H AD 9S")))

    #8
    print("\nTwo pair:")
    print(PokerHand("7C 7D AH AD 9S").compare_with(PokerHand("6C 6D 8H 8D 7S")))
    print(PokerHand("6C 6D 8H 8D 7S").compare_with(PokerHand("7C 7D 7H AD 9S")))
    print("\nTwo pair, 5º card win:")
    print(PokerHand("6C 6D 8C 8D 7H").compare_with(PokerHand("6H 6S 8H 8S 7S")))
    print(PokerHand("6H 6S 8H 8S 7S").compare_with(PokerHand("6C 6D 8C 8D 7H")))

    #9
    print("\nOne pair:")
    print(PokerHand("7C 7D AH 8D 9S").compare_with(PokerHand("6C 6D 8H 9D 7S")))
    print(PokerHand("6C 6D 8H 9D 7S").compare_with(PokerHand("7C 7D AH 8D 9S")))

    print("\nOne pair highest card win:")
    print(PokerHand("7C 7D AH 8D 9S").compare_with(PokerHand("7S 7H KS 9D 6S")))
    print(PokerHand("7S 7H KS 9D 6S").compare_with(PokerHand("7C 7D AH 8D 9S")))

    print("\nOne pair highest suit win:")
    print(PokerHand("7C 7D AH 8D 9S").compare_with(PokerHand("7S 7H AS 8D 9S")))
    print(PokerHand("7S 7H AS 8D 9S").compare_with(PokerHand("7C 7D AH 8D 9S")))

    #10
    print("\nHigh card:")
    print(PokerHand("7C 5D AH 8D 9S").compare_with(PokerHand("6C 3D 8H 9D 7S")))
    print(PokerHand("6C 3D 8H 9D 7S").compare_with(PokerHand("7C 5D AH 8D 9S")))

    print("\nHigh suit:")
    print(PokerHand("7C 2D AH 8D 9S").compare_with(PokerHand("7S 2D AS 8C 9D")))
    print(PokerHand("7S 2D AS 8C 9D").compare_with(PokerHand("7C 2D AH 8D 9S")))


    print("\nPDF TEST:")
    print(PokerHand("JH JC JS JD TH").compare_with(PokerHand("7C 8S 9H TH JH")))

    print(PokerHand("TS TD KC JC 7C").compare_with(PokerHand("JS JC AS KC TD")))

    print(PokerHand("7H 7C QC JS TS").compare_with(PokerHand("7D 7C JS TS 6D")))

    print(PokerHand("5S 5D 8C 7S 6H").compare_with(PokerHand("7D 7S 5S 5D JS")))

    print(PokerHand("AS AD KD 7C 3D").compare_with(PokerHand("AD AH KD 7C 4S")))

    print(PokerHand("TS JS QS KS AS").compare_with(PokerHand("AC AH AS AS KS")))

    print(PokerHand("TS JS QS KS AS").compare_with(PokerHand("TC JS QC KS AC")))

    print(PokerHand("TS JS QS KS AS").compare_with(PokerHand("QH QS QC AS 8H")))

    print(PokerHand("AC AH AS AS KS").compare_with(PokerHand("TC JS QC KS AC")))

    print(PokerHand("AC AH AS AS KS").compare_with(PokerHand("QH QS QC AS 8H")))

    print(PokerHand("TC JS QC KS AC").compare_with(PokerHand("QH QS QC AS 8H")))

    print(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("JH JC JS JD TH")))

    print(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("4H 5H 9H TH JH")))

    print(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("7C 8S 9H TH JH")))

    print(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("TS TH TD JH JD")))

    print(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("JH JD TH TC 4C")))

    print(PokerHand("JH JC JS JD TH").compare_with(PokerHand("4H 5H 9H TH JH")))

    print(PokerHand("JH JC JS JD TH").compare_with(PokerHand("7C 8S 9H TH JH")))

    print(PokerHand("JH JC JS JD TH").compare_with(PokerHand("TS TH TD JH JD")))

    print(PokerHand("JH JC JS JD TH").compare_with(PokerHand("JH JD TH TC 4C")))

    print(PokerHand("4H 5H 9H TH JH").compare_with(PokerHand("7C 8S 9H TH JH")))

    print(PokerHand("4H 5H 9H TH JH").compare_with(PokerHand("TS TH TD JH JD")))

    print(PokerHand("4H 5H 9H TH JH").compare_with(PokerHand("JH JD TH TC 4C")))

    print(PokerHand("7C 8S 9H TH JH").compare_with(PokerHand("TS TH TD JH JD")))

    print(PokerHand("7C 8S 9H TH JH").compare_with(PokerHand("JH JD TH TC 4C")))

    print(PokerHand("TS TH TD JH JD").compare_with(PokerHand("JH JD TH TC 4C")))



if __name__ == '__main__':
    python_challenge_datah()

