tanyai=['kok','?','apa','tau','tahu','apakah','sih','siapa','dimana','mengapa','bagaimana','kenapa','ngapain']
me=['gw','saya','ane','ana','gua','gue','saya','aku']
you=['lu','kamu','anda','lo','loe','bot','botnya']
tanya={
    "?":100,
    "apa":100,
    "apakah":100,
    "siapa":100,
    "dimana":100,
    "mengapa":100,
    "bagaimana":100,
    "kenapa":100,
    "tau":20,
    "tahu":20,
    "ngapain":60,
    "kok":60
}
#---------------------------
def fobjek(kalimat):
    otput=[]
    k=kalimat.replace('?','')
    seplit = k.lower().split(" ")
    for x in seplit:
        if x in me:
            otput.append('dia')
        if x in you:
            otput.append('botnya')
    if len(otput)>1:
        return 'bisa siapa aja'
    elif len(otput)==1:
        return otput[0]
    else:
        return 'yang di tanya'

def fjenis(kalimat):
    cond=False
    percent = 1
    otput = ""

    seplit = kalimat.split(" ")
    for x in seplit:
        if "?" in x:
            percent +=100
            x = x.replace("?","")
        if x in tanyai:
            itanyai = tanyai.index(x)
            percent += tanya[tanyai[itanyai]]
            otput += x

    if percent >= 100:
        percent = 100

    try:
        ptanya = str((percent-0)/percent)+"%"
        pnyata = str((100-percent)/percent)+"%"
    except:
        ptanya = "unknown"
        pnyata = "unknown"

    otput += "\n"+str(percent)+"\n"
    otput += "\npertanyaan : "+ptanya
    otput += "\npernyataan : "+pnyata

    if ptanya>pnyata:
        cond=True
    else:
        cond=False
    return cond
#---------------------------