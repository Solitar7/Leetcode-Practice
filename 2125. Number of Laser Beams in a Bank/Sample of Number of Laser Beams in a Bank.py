class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev_row_count = 0
        total = 0

        for row in bank:
            cur_row_count = sum(int(c) for c in row)
            if cur_row_count == 0:
                continue

            total += cur_row_count * prev_row_count
            prev_row_count = cur_row_count

        return total
