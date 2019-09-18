def solution(record):
    answer=[]
    userDict=dict()
    charLog=[]
    for info in record:
        infoLst=info.split('')
        if infoLst[0]=='Enter':
            if infoLst[1] not in userDict.keys():
                userDict[infoLst[1]]=infoLst[2]
            else:
                userDict[infoLst[1]]=infoLst[2]
            chatLog.append(['님이 들어왔습니다.',infoLst[1]])
        elif infoLst[0]=='Leave':
            charLog.append('[님이 나갔습니다.',infoLst[1])
        elif infoLst[0]=='Change':
            userDict[infoLst[1]]=infoLst[2]
    for log in chatLog:
        answer.append(userDict[log[1]]+log[0])
    
    return answer



