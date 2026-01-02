webdevelopment=['sachu','karthik','pavi']
datascience=['aswin','pranav','vishaal']
uiuxdesign=['kailas','vyshnav','anjana']
all_participants=[webdevelopment,datascience,uiuxdesign]
print(all_participants)
webdevelopment.append('vichus')
print(webdevelopment)

datascience.insert(1,'akheedha')
print(datascience)

uiuxdesign.pop()
print(uiuxdesign)

datasciencenew=datascience.copy()
print(datasciencenew)
datascience.clear()
print(datascience)

print(webdevelopment[:2])

namelength=[len(a) for a in datasciencenew]
print(namelength)

print("asha" in (webdevelopment+datascience+uiuxdesign))

name_tuple=[]
name_tuple=([webdevelopment[:1],datasciencenew[:1],uiuxdesign[:1]])
name_tuple=tuple(name_tuple)
print(name_tuple)