class Solution:
    def posInfinite(self, s: str, pos: int) -> str:
        # lengths[i] = length of the string after i steps:
        # lengths[0] = len(s), lengths[i] = 2 * lengths[i - 1] + i
        lengths = [len(s)]
        while lengths[-1] < pos:
            i = len(lengths)
            lengths.append(2 * lengths[-1] + i)

        # Walk back from the step whose string first covers pos.
        step = len(lengths) - 1
        while step > 0:
            prev = lengths[step - 1]
            if pos <= prev:
                step -= 1                       # inside the earlier string
            elif pos <= prev + step:
                return "$"                      # inside the block of '$'
            else:
                pos = prev - (pos - prev - step) + 1  # mirrored position
                step -= 1
        return s[pos - 1]
