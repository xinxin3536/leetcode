class Solution:
    def reverseWords(self, s: str) -> str:
        tmp = s
        for i in range(0,len(s)):
            if s[i]!=' ':
                break
            else:
                tmp = s[i+1:]
        res = tmp[::-1]
        tmp2 = res
        for i in range(0,len(res)):
            if res[i]!=' ':
                break
            else:
                tmp2 = res[i+1:]
       # print(tmp2)
        result = ''
        tmp3 = ''
        i=0
        tmp4 = True
        while i < len(tmp2):
            if tmp2[i] == ' ':
                i += 1
                continue
            else:
                low = 0
                for j in range(i,len(tmp2)):
                    if tmp2[j] == ' ':
                        low = j
                        break
                    if j == len(tmp2)-1:
                        tmp4 = False
                if tmp4:
                    tmp3 = tmp2[i:low]
                    tmp3 = tmp3[::-1]
                    result = result + tmp3 +' '
                    i = low
                    i += 1
                else:
                    tmp3 = tmp2[i:]
                    result = result + tmp3[::-1]
                    break      
        return result



        