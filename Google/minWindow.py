def minWindow( s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: str
        """
        j =0 
        output ={}
        for i in range(len(s1)):
            if s1[i] == s2[j]:
                j += 1
                if j == len(s2):
                    j -= 1
                    end = i
                    while (j >=0):
                        if s1[i] == s2[j]:
                            j -= 1
                            i -= 1
                    temp =s1[end - i -1:end+1]
                    if temp not in output:
                        output[temp] = len(temp)
        output = sorted(output.items(),key=lambda item:item[1])
        if len(output) == 0:
            return ""
        return output[0][0]
        
#s1 = "abcdebdde"
#s2 = "bde"

s1 = "cnhczmccqouqadqtmjjzl"
s2 = "mm"
print(minWindow( s1, s2))