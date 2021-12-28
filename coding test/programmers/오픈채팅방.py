def solution(record):
    answer = []
    uid_name = {}
    for strings in record:
        string = strings.split()
        if len(string) == 3:
            uid_name[string[1]] = string[2]
    
    for strings in record:
        string = strings.split()
        if string[0] =="Enter":
            t = uid_name[string[1]]
            temp = t+"님이 들어왔습니다."
            answer.append(temp)
        if string[0] =="Leave":
            t = uid_name[string[1]]
            temp = t+"님이 나갔습니다."
            answer.append(temp)
    return answer