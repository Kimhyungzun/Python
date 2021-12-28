def solution(s):
    length = len(s)
    ans = 10000
    if length <= 2:
        return length
    for cut in range(1,length//2 + 1):
        cnt=1
        res = ""
        for j in range(cut, length+cut, cut):
            if s[(j-cut):j] == s[j:(j+cut)]:
                cnt+=1
            else:
                if cnt == 1:
                    res += s[(j-cut):j]
                else:
                    res += str(cnt) + s[(j-cut):j]
                    cnt=1
        ans = min(ans, len(res))
    
    return ans