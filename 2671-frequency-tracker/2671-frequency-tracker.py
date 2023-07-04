from collections import Counter
class FrequencyTracker:

    def __init__(self):
        self.counter = Counter()
        self.counts = [0]*(2*(10**5)+1)

    def add(self, number: int) -> None:
        f = self.counter[number]
        self.counter[number] += 1
        self.counts[f] = max(0, self.counts[f]-1)
        self.counts[f+1] += 1
        #print(self.counts[:10])
        
    def deleteOne(self, number: int) -> None:
        f = self.counter[number]
        self.counter[number] = max(0, self.counter[number]-1)
        self.counts[f] -= 1
        if f-1 > 0: self.counts[f-1] += 1
        
    def hasFrequency(self, frequency: int) -> bool:
        
        return self.counts[frequency] > 0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)