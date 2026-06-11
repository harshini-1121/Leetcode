class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n =len(temperatures)
        answers = [0]*n
        stack=[]

    
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                answers[prev_index] = i - prev_index
           
            stack.append(i)
        
        return answers



        #    for j in range(i+1,n):
         #       if temperatures[j] > temperatures[i]:
          #          answers[i] = j-i
           #         break
            #    
        #return answers