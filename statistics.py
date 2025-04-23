import math 

def calculateStats(numbers):
    average=0
    max=0
    min=0
    if isEmpty(numbers):
        return {"avg":None,"max":None,"min":None}
    if is_valid_number(numbers):
        return {"avg":None,"max":None,"min":None}
    average=sum(numbers)/len(numbers)
    max=max(numbers)
    min=min(numbers)
    return {"avg":average,"max":max,"min":min}
    

def isEmpty(numbers):
    if len(numbers)==0:
        return True
    else:
        return False
        
def is_valid_number(numbers):
    for num in numbers:
        if math.isnan(num):
            return False
    return True
        
