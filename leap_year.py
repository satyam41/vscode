Year = 2024
if (Year % 4) == 0:
   if (Year % 100) == 0:
       if (Year % 400) == 0:
           print(True)
       else:
           print(False)
   else:
       print(True)
else:
   print(False)