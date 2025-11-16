class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # O(n) time, O(1) space
        word_ptr = abbr_ptr = 0

        while word_ptr < len(word) and abbr_ptr < len(abbr):
            if word[word_ptr] != abbr[abbr_ptr]:
                # if not, we have 2 cases
                # 1. abbr could have leading zeroes, or char that is not a number and not unmatching
                if abbr[abbr_ptr] == '0' or abbr[abbr_ptr].isalpha():
                    return False

                # 2. it should be a number, we need to capture it fully
                else:
                    num = 0
                    while abbr_ptr < len(abbr) and abbr[abbr_ptr].isdigit():
                        num = num * 10 + int(abbr[abbr_ptr])
                        abbr_ptr += 1

                    # continue cross check from (word_ptr+num)-th position in word
                    word_ptr += num
            
            # when there is a match, we just go forward by 1 step
            else:
                word_ptr += 1
                abbr_ptr += 1

        return word_ptr == len(word) and abbr_ptr == len(abbr)
        