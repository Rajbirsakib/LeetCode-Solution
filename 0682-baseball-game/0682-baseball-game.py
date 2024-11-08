class Solution:
    def calPoints(self, operations: List[str]) -> int:
        list_stack=[]
        for i in range(len(operations)):
            if operations[i]=="D":
                list_stack.append(list_stack[-1]*2)
            elif operations[i]=="C":
                list_stack.pop(-1)
            elif operations[i]=="+":
                list_stack.append(list_stack[-1]+list_stack[-2])
            else:
                list_stack.append(int(operations[i]))
        
        return sum(list_stack)