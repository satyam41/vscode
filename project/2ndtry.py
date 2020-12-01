import winsound
# Play Windows exit sound.
winsound.PlaySound("SystemExit", winsound.SND_LOOP)

# Probably play Windows default sound, if any is registered (because
# "*" probably isn't the registered name of any sound).
winsound.PlaySound("*", winsound.SND_LOOP)


l = [[4,5,4,4],[1,2,3,4],[4,2,5,1]]
print(l[1])