class TataSky():

    def __init__(self,channel):
        self.channel=channel
    
    def displayPack(self):
        print("Your Channels/Packs are : ")
        for channel in self.channel:
             print(f" * {channel}")
        

    def addChannel(self,channelname):
        if channelname in self.channel:
            print(f"Dear Subscriber, {channelname} has been already added to your Pack.")
        else:
         self.channel.append(channelname)
         print(f"Dear Subscriber, {channelname} channel has been successfully add to your pack. Check Your Pack.")
    
    def dropChannel(self,channelname):
        if channelname not in self.channel:
            print(f"Dear Subscriber, {channelname} channel cannot be dropped from your Pack because you have not subscribed this channel.")
        else:
            self.channel.remove(channelname)
            print(f"Dear Subscriber, {channelname} channel has been successfully dropped from your pack.")
    
    def clearPack(self):
        print("You have removed all the packs.")
        return self.channel.clear()

class User():
    def requestChannel(self):
        self.channel=input("Enter the name of the channel you want to add in your pack : ")
        return self.channel    
    
    def removeChannel(self):
        self.channel=input("Enter the name of the channel you want to drop from your pack : ")
        return self.channel    
    


t=TataSky(["MTV","Aaho Music","Zoom","9XM","9X Tashan"])
u=User()

while True:
 try:
  l=int(input('''If you want to make your pack, press 1 : '''))
  if l==1:
   while(True):
       print('''======= Welcome to Tata Sky! ======= 
       1. See Your Pack
       2. Modify your Pack
       3. Reset Pack
       4. Exit''')
       a=int(input("Enter your choice : "))
       if a==1:
           t.displayPack()
    
       elif a==2:
           print("\n1. Add Channel\n2. Drop Channel")
           b=int(input("Enter your choice : "))
           if b==1:
              t.addChannel(u.requestChannel())
           elif b==2:
              t.dropChannel(u.removeChannel())
           else:
              print("Oops! Invalid Choice.")
    
       elif a==3:
           t.clearPack()
    
       elif a==4:
           print("Thanks for using Tata Sky. If you have any query related to My Packs, reach to us through WhatsApp. ")
           exit()
    
       else:
           print("Oops! Invalid Choice.")

  else:
      print("Make sure you entered a correct choice.")

 except ValueError:
     print("Please enter a value not a character. Try Again!")

 except Exception as e:
     print(e)

