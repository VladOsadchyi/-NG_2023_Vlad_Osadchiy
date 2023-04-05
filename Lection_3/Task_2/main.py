def diamond(size, tractor=0):
   if size<=0:
       return 
   print(' '*(size-1)+'*'*(2*tractor+1))
   if size>1:
       diamond(size-1, tractor+1)
   print(' '*(size-1)+'*'*(2*tractor+1))
def mainpartofpr():
    print("This program will paint a diamond for you!Good Luck!")
    size=int(input("Enter the size of your diamond: "))
    diamond(size)
mainpartofpr()

