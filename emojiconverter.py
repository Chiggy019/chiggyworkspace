message = input(">")
li = message.split()
upmsg = ""
emoji={
    ":)":"đ",
    ":D":"đ",
    ":(":"âšī¸",
    ";)":"đ",
    ":|":"đ",
    "**)":"đ",
    ";p":"đ",
    ":'(":"đĨ˛"
}
for i in li:
    upmsg+=emoji.get(i,i)+" "
print(upmsg)
