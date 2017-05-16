import urllib.request

opener = urllib.request.FancyURLopener({})
appleFile = opener.open("http://www.apple.com/")
appleSegment = str(appleFile.read(200))
urList = appleSegment.split()
print(urList)

    
def hasDigit(a):
    for j in a:
        if j.isdigit():
            return True
            
for i in range(0, len(urList)):
    if hasDigit(urList[i]):
        for k in range(len(urList[i])):
           
            if hasDigit(urList[i][k]):
                print(urList[i] ,'(',urList[i][k],')')
    else:
        print(urList[i] , '( no digit)')

    
         
