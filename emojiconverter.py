message = input(">")
li = message.split()
upmsg = ""
emoji={
    ":)":"😄",
    ":D":"😂",
    ":(":"☹️",
    ";)":"😉",
    ":|":"😑",
    "**)":"😍",
    ";p":"😜",
    ":'(":"🥲"
}
for i in li:
    upmsg+=emoji.get(i,i)+" "
print(upmsg)
