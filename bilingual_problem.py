D={"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}

sen='merry christmas and happy new year'


def translate(D,sen):
    sentance=sen.split()
    res=[]
    for i in sentance:
        res.append(D[i])
    t_res=" ".join(res)
    return t_res
  
s=translate(D,sen)
print(s)
        
