import math 

def calculateStats(numbers):
    average=0
    maximum=0
    minimum=0
    if isEmpty(numbers):
        return {"avg":float("nan"),"max":float("nan"),"min":float("nan")}
    if not is_valid_number(numbers):
        return {"avg":float("nan"),"max":float("nan"),"min":float("nan")}
    average=sum(numbers)/len(numbers)
    maximum=max(numbers)
    minimum=min(numbers)
    return {"avg":average,"max":maximum,"min":minimum}
    

def isEmpty(numbers):
    if len(numbers)==0:
        return True
    else:
        return False
        
def is_valid_number(numbers):
    for num in numbers:
        try:
            if math.isnan(float(num)):
                return False
        except (ValueError, TypeError):
            return False
    return True


if __name__ == "__main__":
    computedStats = calculateStats([1.5, 8.9, 3.2, 4.5])
    print(computedStats)
