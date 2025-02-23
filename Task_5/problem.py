from typing import List

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        min_val = -1
        max_val = -1
        sum = 0
        total_count = 0
        mode_val = -1
        max_freq = 0

        mid1, mid2 = None, None
        running_count = 0
        total_elements = self.findTotalCount(count)  

        for i in range(len(count)):
            if count[i] > 0:
                if min_val == -1:
                    min_val = i

                max_val = i
                sum += i * count[i]
                total_count += count[i]

                if count[i] > max_freq:
                    max_freq = count[i]
                    mode_val = i

            running_count += count[i]
            if mid1 is None and running_count >= total_elements // 2:
                mid1 = i
            if mid2 is None and running_count >= (total_elements // 2) + 1:
                mid2 = i

        mean_val = round(sum / total_elements, 5)
        median_val = (mid1 + mid2) / 2 if total_elements % 2 == 0 else float(mid2)

        return [float(min_val), float(max_val), mean_val, median_val, float(mode_val)]

    def findTotalCount(self, count: List[int]) -> int:
        total = 0
        for num in count:
            total += num
        return total
    
# count = [0,4,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# solution = Solution()
# print(solution.sampleStats(count))