class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0] * len(temperatures)  # This will hold our results
        stack = []  # This will store indices of the temperatures list

        for i, temp in enumerate(temperatures):
            # Check if the current day's temperature is warmer than the day at the stack's top
            while stack and temperatures[stack[-1]] < temp:
                index = stack.pop()
                answer[index] = i - index  # Calculate how many days it took to get a warmer temperature
            stack.append(i)  # Push the current day's index onto the stack

        return answer




solution=Solution()
temperatures = [73,74,75,71,69,72,76,73]
print(solution.dailyTemperatures(temperatures))
print(solution.dailyTemperatures(temperatures = [30,40,50,60]))
print(solution.dailyTemperatures(temperatures = [30,60,90]))