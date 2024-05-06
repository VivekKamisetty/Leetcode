#https://leetcode.com/problems/daily-temperatures/description/

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index
            stack.append(i)

        return res
        # stack = []
        # temps = temperatures
        # res = [0]*len(temps)

        # curr = 0

        # for i in range(len(temps)):
        #     stack.append(temps[i])
        #     if i < len(temps) - 1 and stack[-1] < temps[i+1]:
        #         # print(stack, temps[i], "if")
        #         stack.pop()
        #         res[i] = 1
        #     else:
        #         curr = temps[i]
        #         j = i + 1
        #         if j == len(temps):
        #             count = 0
        #         else:
        #             count = 1
        #         # print(curr, temps[j], "while")
        #         while j < len(temps) and curr >= temps[j]:
        #             # print(j, len(temps), "while")
        #             if j+1 == len(temps):
        #                 count = 0
        #                 j+=1
        #             else:
        #                 count+=1
        #                 j+=1
        #         stack.pop()
        #         # print(count)
        #         res[i] = count
        #         # print(stack, temps[i], res)

        # return res
