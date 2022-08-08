# [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]

a={"science": [88, 89, 62, 95], "language": [77, 78, 84, 80]}
length=len(a["science"])
length1=len(a["language"])
i=0
dic={}
list=[]
while i<length:
    dic["science"]=a["science"][i]
    dic["language"]=a["language"][i]
    list.append(dic)
    i=i+1
    print(dic) 