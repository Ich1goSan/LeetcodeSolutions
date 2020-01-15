def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
    arr = text.split()
    result = []
        for i in range(1, len(arr)-1):
         if(arr[i-1] == first and arr[i] == second):
            result.append(arr[i+1])
    return result