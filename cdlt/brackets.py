def solution(S):
    stack=[]
    answer=1
    for c in S:
        if c in '{([':
            stack.append(c)
        else:
            if len(stack):
                bracket=stack.pop()
                if c=='}' and bracket!='{':
                    answer=0
                elif c==')' and bracket!='(':
                    answer=0
                elif c==']' and bracket!='[':
                    answer=0
            else:
                answer=0
        if answer==0:
            break
    if answer and len(stack):
        answer=0
    return answer
