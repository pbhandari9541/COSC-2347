import urllib.request



def ScrapeSiteSegment(site, length):
    opener = urllib.request.FancyURLopener({})
    siteFile = opener.open(site)
    siteSegment = str(siteFile.read(length))
    return siteSegment

def ScrapeSite(site):
    opener = urllib.request.FancyURLopener({})
    siteFile = opener.open(site)
    siteData = str(siteFile.read())
    return siteData

def GetDigitString(s):
    d_string = ''
    for i in s:
        if i.isdigit():
            d_string += i
    if d_string != '':
        return "(" + d_string + ")"
    return "(No digits)";

def GetSaleString(s):
    for i in s:
        for j in myKeywords:
            if j in i:
                return ("Hurray!! the store has sale!")
    return ("oops!!!no sales going on :(")

segment = ScrapeSiteSegment("http://www.apple.com", 200)
ur_list = segment.split()
print("number of element in the list :", len(ur_list))
print("Output for (a): \n \n", segment)
print("\nOutput for (b):\n")
for i in range(len(ur_list)):
    print(ur_list[i]) 
print("\nOutput for (c):\n")
for i in range(len(ur_list)):
    curr_string = ur_list[i]
    digit_string = GetDigitString(curr_string)
    print(curr_string, " ", digit_string)

myKeywords = ['sale', 'discount', 'off', 'promottion', 'b1g1 free' ]

siteData = ScrapeSite("http://www1.macys.com")
site_list = siteData.split()
print("\n Macys store Data\n")
print(GetSaleString(site_list))
