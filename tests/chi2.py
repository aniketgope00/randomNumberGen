#chi2 = sum((observedFreq - expectedFreq)**2 / expectedFreq)
import pandas as pd

class chi2:
    
    observedFreq = {}
    expectedFreq = {}
    
    def __init__(self, observedFreqIP) -> None:
        self.observedFreq = observedFreqIP
        
        expected_freq_sum = 0
        for freq in self.observedFreq.keys():
            expected_freq_sum += freq
        print("Expected Freq Sum:", expected_freq_sum)
        
        n = len(list(self.observedFreq.keys()))
        print("N:", n)
        expected_freq = expected_freq_sum/n
        print("Expected Freq:", expected_freq)

        for key in self.observedFreq.keys():
            self.expectedFreq[key] = expected_freq
        
    def degreeOfFreedom(self)->int:
        c = len(list(self.observedFreq.keys()))
        return c - 1
    
    def getTableValue(self, freedom, alpha)->float:
        table = pd.read_excel("chi2tablevalues.xlsx")
        chi2value = table._get_value(freedom - 1, alpha)
        return chi2value
    

    def getScore(self)->float:
        score = 0
        for fo, fe in zip(self.observedFreq.values(), self.expectedFreq.values()):
            score += ((fo - fe)**2)/fe
        print("score:", score)
        return score

    def hypothesisResult(self, chi2val, chi2tableval)->bool:
        if chi2tableval > chi2val:
            print("Hypothesis Accepted")
            return True
        else:
            print("Null Hypothesis Rejected")
            return False


    def print(self) -> None:
        r"""
        this function is for testing purposes only.
        """
        print(self.observedFreq)
        print(self.expectedFreq)


