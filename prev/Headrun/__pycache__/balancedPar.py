from StackOf import StackOf
def mat_bracket(top,brac):
    if(top =='(' and brac ==')'):
        return True
    elif(top =="{" and brac =="}"):
        return True
    elif(top=="[" and brac =="]"):
        return True
    else:
        return False

def balancedPar(para):
    s = StackOf()
    index = 0
    is_bal = True
    while index < len(para) and is_bal:
        bracket = para[index]
        if bracket in "({[":
            s.push(bracket)
        else:
            if s.is_empty():
                is_bal=False
                break
            else:
                top=s.pop()
                if not mat_bracket(top,bracket):
                    is_bal=False
                    break
        index=index+1
    if(is_bal==True):
        print("Balanced")
    else:
        print("Unbalanced")

    
para = "()"
balancedPar(para)