import collections

# Assume you are given this class
class Card:
    def __init__(self, rank, suit):
        self.rank = rank # e.g., 'A', 'K', '7'
        self.suit = suit # e.g., '♥', '♠'
    def __repr__(self):
        return f"{self.rank}{self.suit}"

class HandEvaluator:
    # Define the rank map as a class variable (it's constant)
    # Note: 'A' is 14 for high straights. We'll handle 'A-2-3-4-5' as a special case.
    RANK_MAP = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, 
                '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    def __init__(self, hand):
        # 'hand' is a list of 5 Card objects
        self.hand = hand

        # Calculate all counters and sorted lists ONCE here.
        self.ranks_counter = collections.Counter([c.rank for c in hand])    # count many times each rank appears
        self.suits_counter = collections.Counter([c.suit for c in hand])    # count many times each suit appears
        
        # Get the sorted *values* of the ranks (e.g., [2, 5, 5, 13, 14])
        self.sorted_values = sorted([self.RANK_MAP[c.rank] for c in hand])
        
        # Get the unique, sorted values. Crucial for straight detection.
        # e.g., [2, 5, 13, 14]
        self.unique_sorted_values = sorted(list(set(self.sorted_values)))
        
        # Pre-calculate rank counts, e.g., [1, 1, 3] or [1, 2, 2] or [2, 3]
        self.rank_counts = sorted(self.ranks_counter.values())

    def has_flush(self):
        # If there's only one suit, the suits_counter will only have 1 key.
        return len(self.suits_counter) == 1

    def has_straight(self):
        
        # 1. A straight can't have any pairs, so we must have 5 unique ranks.
        if len(self.unique_sorted_values) != 5:
            return False
        
        # 2. Check for the normal straight (e.g., 9-T-J-Q-K)
        # 13 - 9 == 4
        is_normal_straight = (self.unique_sorted_values[4] - self.unique_sorted_values[0] == 4)
        
        # 3. Check for the special 'A-2-3-4-5' (Wheel) case
        # This will be [2, 3, 4, 5, 14] after mapping 'A' to 14.
        is_wheel = (self.unique_sorted_values == [2, 3, 4, 5, 14])

        return is_normal_straight or is_wheel

    def has_straight_flush(self):
        # A hand is a straight flush if it's BOTH a straight and a flush
        return self.has_straight() and self.has_flush()

    def has_four_of_a_kind(self):
        # We pre-calculated counts. For 5 cards, this must be [1, 4].
        return self.rank_counts == [1, 4]

    def has_full_house(self):
        # We pre-calculated counts. For 5 cards, this must be [2, 3].
        return self.rank_counts == [2, 3]

    def has_three_of_a_kind(self):
        # Check for [1, 1, 3]. We check for Full House *first* in evaluate(),
        # so this logic is safe.
        return self.rank_counts == [1, 1, 3]

    def has_two_pair(self):
        # Check for [1, 2, 2].
        return self.rank_counts == [1, 2, 2]

    def has_one_pair(self):
        # Check for [1, 1, 1, 2].
        return self.rank_counts == [1, 1, 1, 2]

    def evaluate(self):
        # IMPROVEMENT (Completeness):
        # This is the full, correct order of checks.
        
        # We must check Straight Flush first
        if self.has_straight_flush():
            return "Straight Flush"
        if self.has_four_of_a_kind():
            return "Four of a Kind"
        if self.has_full_house():
            return "Full House"
        if self.has_flush():
            return "Flush"
        if self.has_straight():
            return "Straight"
        if self.has_three_of_a_kind():
            return "Three of a Kind"
        if self.has_two_pair():
            return "Two Pair"
        if self.has_one_pair():
            return "One Pair"
        
        return "High Card"

# # --- Test it ---
# hand1 = [Card('9', '♠'), Card('K', '♠'), Card('Q', '♠'), Card('J', '♠'), Card('10', '♠')]
# print(f"Hand 1: {HandEvaluator(hand1).evaluate()}") # Should be "Straight Flush"

# hand2 = [Card('K', '♥'), Card('K', '♣'), Card('K', '♦'), Card('5', '♠'), Card('5', '♥')]
# print(f"Hand 2: {HandEvaluator(hand2).evaluate()}") # Should be "Full House"

# hand3 = [Card('A', '♥'), Card('A', '♣'), Card('A', '♦'), Card('A', '♠'), Card('J', '♥')]
# print(f"Hand 3: {HandEvaluator(hand3).evaluate()}") # Should be "Four of a Kind"

# # --- NEW TEST CASES to verify bug fixes ---

# # Test for 'A-2-3-4-5' (Wheel) Straight
# hand4 = [Card('A', '♥'), Card('2', '♣'), Card('3', '♦'), Card('4', '♠'), Card('5', '♥')]
# print(f"Hand 4: {HandEvaluator(hand4).evaluate()}") # Should be "Straight"

# # Test for '10-J-Q-K-A' (Royal) Straight
# hand5 = [Card('10', '♥'), Card('J', '♣'), Card('Q', '♦'), Card('K', '♠'), Card('A', '♥')]
# print(f"Hand 5: {HandEvaluator(hand5).evaluate()}") # Should be "Straight"

# # Test for Straight with a pair (which is not a straight)
# hand6 = [Card('5', '♥'), Card('5', '♣'), Card('6', '♦'), Card('7', '♠'), Card('8', '♥')]
# print(f"Hand 6: {HandEvaluator(hand6).evaluate()}") # Should be "One Pair"

# # Test for Two Pair
# hand7 = [Card('J', '♥'), Card('J', '♣'), Card('3', '♦'), Card('3', '♠'), Card('8', '♥')]
# print(f"Hand 7: {HandEvaluator(hand7).evaluate()}") # Should be "Two Pair"


# -----------------------------------------------------------------
# --- JOKER CHALLENGE: Implement this class ---
# -----------------------------------------------------------------

class HandEvaluatorWithJoker:
    RANK_MAP = HandEvaluator.RANK_MAP
    
    def __init__(self, hand):
        self.hand = hand
        self.real_cards = []
        self.num_jokers = 0
        
        # --- 1. Separate Jokers from Real Cards ---
        for card in hand:
            if card.rank == 'JOKER':
                self.num_jokers += 1
            else:
                self.real_cards.append(card)
        
        # --- 2. Pre-calculate all counters *for real cards only* ---
        self.real_ranks_counter = collections.Counter([c.rank for c in self.real_cards])
        self.real_suits_counter = collections.Counter([c.suit for c in self.real_cards])
        
        self.real_sorted_values = sorted([self.RANK_MAP[c.rank] for c in self.real_cards])
        self.real_unique_sorted_values = sorted(list(set(self.real_sorted_values)))
        
        # e.g., [1, 1, 2] or [1, 3] or [2]
        self.real_rank_counts = sorted(self.real_ranks_counter.values())

    def has_flush(self):
        # A flush is possible if all *real* cards have the same suit.
        # If len(self.real_suits_counter) is 0 (all Jokers) or 1 (all
        # real cards are one suit), the Jokers can fill in to make a flush.
        # If len > 1 (e.g., {'♥': 3, '♠': 1}), it's impossible.
        return len(self.real_suits_counter) <= 1

    def has_straight(self):
        # This is the hardest one!
        # Hint: How many "gaps" can you fill with self.num_jokers?
        # 1. You need 5 unique ranks total.
        #    `num_unique_real_ranks = len(self.real_unique_sorted_values)`
        #    If `num_unique_real_ranks + self.num_jokers < 5`, a straight is impossible.
        # 2. If you have 5 real, unique ranks, check for a normal straight (like before).
        # 3. If you have (e.g.) 4 real, unique ranks and 1 joker:
        #    - Get the lowest and highest rank: `min_rank = self.real_unique_sorted_values[0]`
        #    - and `max_rank = self.real_unique_sorted_values[3]`
        #    - What's the *maximum* allowed gap between them (max_rank - min_rank)?
        #    - (e.g., 5, 6, 8, 9 + Joker -> min=5, max=9. Gap is 4. This works.)
        #    - (e.g., 5, 6, 7, 9 + Joker -> min=5, max=9. Gap is 4. This works.)
        #    - (e.g., 5, 6, 7, 10 + Joker -> min=5, max=10. Gap is 5. Impossible.)
        # 4. Don't forget the 'A-2-3-4-5' (Wheel) case! This is tricky.
        #    (e.g., A, 2, 3 + 2 Jokers) -> [2, 3, 14]
        pass

    def has_straight_flush(self):
        # Hint: A hand is a straight flush if it's BOTH a straight and a flush
        # *at the same time*.
        # Be careful! A hand like [Joker, 10♥, J♥, Q♥, K♦] can be a Straight OR a Flush,
        # but not a Straight Flush.
        # Logic: Check if all real cards have the same suit. If not, it's impossible.
        # If they *do*, then just run the `has_straight` logic on them.
        pass

    def has_five_of_a_kind(self):
        # This one is new! 5 cards of the same rank.
        # (e.g., 4 Aces + 1 Joker)
        # (e.g., 3 Kings + 2 Jokers)
        # Hint: Check the highest count in `self.real_rank_counts`.
        pass

    def has_four_of_a_kind(self):
        # (e.g., 4 Aces + 0 Jokers) -> `self.real_rank_counts` is [1, 4]
        # (e.g., 3 Aces + 1 Joker)  -> `self.real_rank_counts` is [1, 1, 3] or [2, 3]
        # (e.g., 2 Aces + 2 Jokers)  -> `self.real_rank_counts` is [1, 1, 1, 2] or [1, 2, 2]
        # Hint: What's the highest count among your real cards?
        # `max_real_count = self.real_rank_counts[-1]`
        # If `max_real_count + self.num_jokers >= 4`, is that enough? Almost...
        pass

    def has_full_house(self):
        # (e.g., 3 Kings, 2 Fives + 0 Jokers) -> `self.real_rank_counts` is [2, 3]
        # (e.g., 3 Kings, 1 Five, 1 Joker)   -> `self.real_rank_counts` is [1, 1, 3]
        # (e.g., 2 Kings, 2 Fives, 1 Joker)   -> `self.real_rank_counts` is [1, 2, 2]
        # This one is also tricky!
        pass

    def has_three_of_a_kind(self):
        # Hint: Similar to 4-of-a-kind.
        # `max_real_count = self.real_rank_counts[-1]`
        # If `max_real_count + self.num_jokers >= 3`, is that sufficient?
        pass

    def has_two_pair(self):
        # Hint:
        # (e.g., 2 Kings, 2 Fives + 0 Jokers) -> `self.real_rank_counts` is [1, 2, 2]
        # (e.g., 2 Kings, 1 Five, 1 Ace, 1 Joker) -> `self.real_rank_counts` is [1, 1, 1, 2]
        pass

    def has_one_pair(self):
        # Hint:
        # A Joker *always* creates a pair with the highest real card.
        # So, if `self.num_jokers > 0`, this is always True.
        # If `self.num_jokers == 0`, check for a normal pair.
        if self.num_jokers > 0:
            return True
        elif self.num_jokers == 0:
            return self.real_rank_counts == [1, 1, 1, 2]


    def evaluate(self):
        # This is the full, correct order of checks.
        # Note: "Five of a Kind" is now the best hand!
        
        if self.has_five_of_a_kind():
            return "Five of a Kind"
        if self.has_straight_flush():
            return "Straight Flush"
        if self.has_four_of_a_kind():
            return "Four of a Kind"
        if self.has_full_house():
            return "Full House"
        if self.has_flush():
            return "Flush"
        if self.has_straight():
            return "Straight"
        if self.has_three_of_a_kind():
            return "Three of a Kind"
        if self.has_two_pair():
            return "Two Pair"
        if self.has_one_pair():
            return "One Pair"
        
        return "High Card"


# -----------------------------------------------------------------
# --- JOKER CHALLENGE: Test Cases ---
# -----------------------------------------------------------------
print("\n--- HandEvaluatorWithJoker Tests ---")

joker = Card('JOKER', 'JOKER')

# Test 1: Five of a Kind
# 4 real Aces + 1 Joker
j_hand_1 = [Card('A', '♥'), Card('A', '♣'), Card('A', '♦'), Card('A', '♠'), joker]
print(f"Joker Hand 1: {HandEvaluatorWithJoker(j_hand_1).evaluate()}") # EXPECTED: Five of a Kind

# Test 2: Straight Flush
# 4 real cards to a straight flush + 1 Joker
j_hand_2 = [Card('9', '♠'), Card('K', '♠'), Card('Q', '♠'), Card('J', '♠'), joker]
print(f"Joker Hand 2: {HandEvaluatorWithJoker(j_hand_2).evaluate()}") # EXPECTED: Straight Flush

# Test 3: Straight (using Joker)
# 10, J, Q, K + Joker should make a straight
j_hand_3 = [Card('10', '♥'), Card('J', '♣'), Card('Q', '♦'), Card('K', '♠'), joker]
print(f"Joker Hand 3: {HandEvaluatorWithJoker(j_hand_3).evaluate()}") # EXPECTED: Straight

# Test 4: Flush (using Joker)
# 4 real cards of same suit + 1 Joker
j_hand_4 = [Card('2', '♥'), Card('5', '♥'), Card('9', '♥'), Card('K', '♥'), joker]
print(f"Joker Hand 4: {HandEvaluatorWithJoker(j_hand_4).evaluate()}") # EXPECTED: Flush

# Test 5: Full House (using Joker)
# Two pairs + 1 Joker -> Full House
j_hand_5 = [Card('K', '♥'), Card('K', '♣'), Card('5', '♦'), Card('5', '♠'), joker]
print(f"Joker Hand 5: {HandEvaluatorWithJoker(j_hand_5).evaluate()}") # EXPECTED: Full House

# Test 6: Full House (using Joker)
# Three of a kind + 1 real pair (this is just a normal full house)
j_hand_6 = [Card('K', '♥'), Card('K', '♣'), Card('K', '♦'), Card('5', '♠'), Card('5', '♥')]
print(f"Joker Hand 6: {HandEvaluatorWithJoker(j_hand_6).evaluate()}") # EXPECTED: Full House

# Test 7: Full House (using Joker)
# Three of a kind + 1 unrelated card + 1 Joker -> Full House? No, Four of a Kind!
j_hand_7 = [Card('Q', '♥'), Card('Q', '♣'), Card('Q', '♦'), Card('2', '♠'), joker]
print(f"Joker Hand 7: {HandEvaluatorWithJoker(j_hand_7).evaluate()}") # EXPECTED: Four of a Kind

# Test 8: Straight (Wheel, using Joker)
# A, 2, 3, 5 + Joker
j_hand_8 = [Card('A', '♥'), Card('2', '♣'), Card('3', '♦'), Card('5', '♠'), joker]
print(f"Joker Hand 8: {HandEvaluatorWithJoker(j_hand_8).evaluate()}") # EXPECTED: Straight

# Test 9: One Pair (with Joker)
# 4 high cards + 1 Joker -> One Pair (Joker pairs with highest card, 'A')
j_hand_9 = [Card('A', '♥'), Card('K', '♣'), Card('Q', '♦'), Card('J', '♠'), joker]
print(f"Joker Hand 9: {HandEvaluatorWithJoker(j_hand_9).evaluate()}") # EXPECTED: One Pair

# Test 10: Two Jokers!
# 3, 5, 7 + 2 Jokers -> Straight
j_hand_10 = [Card('3', '♥'), Card('5', '♣'), Card('7', '♦'), joker, joker]
print(f"Joker Hand 10: {HandEvaluatorWithJoker(j_hand_10).evaluate()}") # EXPECTED: Straight