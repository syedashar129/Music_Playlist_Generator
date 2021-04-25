#Playlist
import random
#https://epsil.github.io/spotgen/
#https://register.tamuhack.com/accounts/login/
#https://hackreason.aisutd.org/
# team code :      28401dfb-2946-4a3e-910b-79399db8d85f

#run and c
def calcEnds(fil):
     FILE= open(fil)
     fir=True
     sec=True
     #try again
     for i, line in enumerate(FILE):
          if len(line.strip())==0 and fir:
               end1=i
               fir=False
          elif len(line.strip())==0 and sec:
               end2=i
               sec=False
          end3=i  
     end1 -=1
     end2 -=1
     return end1,end2,end3
     print(str(end1)+' '+str(end2)+' '+str(end3))
'''Artists: 
          Rap: Eminem, Lil wayne, Tupac, Drake, Snoop, Travis Scott
          R&B: 6lack, Bryson tiller, Don toliver, Usher, Michael Jackson
          Country: Lee Brice, Wheeler walker Jr., Render sisters, Carrie Underwood
          Classical: Beethoven, Chopin, Brahms
          Pop: Beyonce, Taylor Swift, Justin Bieber, Katy Perry, Lady Gaga, The Beatles
'''

names=[
     ['Rap', 'Snoop', 'Tupac', 'Eminem', 'Jay-Z', 'Drake' , 'Travis Scott'],
     ['R&B', 'Michael Jackson', 'Usher', 'Bryson Tiller', '6lack', 'Don Toliver'],
     ['Country', 'Lee Brice', 'Render sisters','Wheeler walker Jr.', 'Carrie Underwood'],
     ['Classical', 'Beethoven', 'Chopin', 'Brahms'],
     ['Pop', 'The Beatles', 'Lady Gaga', 'Beyonce', 'Katy Perry', 'Taylor Swift', 'Justin Bieber']
]
Exit=False
i=1
for genre in names:
          for name in genre:
               if name != 'Rap' and name != 'R&B' and name != 'Country' and name != 'Classical' and name != 'Pop':
                    print(str(i)+' '+name)
                    i = i + 1

rap=False
rb=False
country=False
classical=False
pop=False

rap2000=False
rap2008=False
rap2015=False
rb2000=False
rb2008=False
rb2015=False
country2000=False
country2008=False
country2015 = False
pop2000=False
pop2008=False
pop2015=False

'''bet so like we should prob put the in roder in list so its easy to calc when nuber eneter like 1-3 is 2000s, 3-5 is 2008s bet yeah
Rap : 2000-2008(Snoop, Tupac, Eninem), 2009-2015(Drake, Eninem), 2016-Present(Drake, Lil Wayne and Travis Scott)
R&B : 2000-2008 (michael jackson, usher) 2009-2015(bryson tiller), 2016-present(6lack, don, )
Country : 2000-2008 (lee) 2009-2015(render), 2016-present(wheeler, carrie)
Classical: -------------> all in classical era no specefic decade
Pop: 2000-2008 (beatles, lady gaga) 2009-2015(katy perry, beyonce), 2016-present(taylor, justin)
'''

while not(Exit):
     num = int(input('Choose artists numbers and press 0 to exit: '))
     if num==0:
          Exit=True
     elif num >=1 and num <=6: 
          rap=True
          if num >= 1 and num <=4:
               rap2000 = True
          if num >=3 and num <=5:
               rap2008 = True
          if num >= 5 and num<=6:
               rap2015=True
     elif num >=7 and num <=11:
          rb=True
          if num >= 7 and num <=8:
               rb2000 = True
          if num == 9:
               rb2008 = True
          if num >= 10 and num<=11:
               rb2015=True
     elif num >=12 and num <=15:
          country = True
          if num == 12:
               country2000 = True
          if num ==13:
               country2008 = True
          if num >= 14 and num<=15:
               country2015=True
     elif num >=16 and num <=18:
          classical = True
     elif num >=19 and num <=24:
          pop = True
          if num >= 19 and num <=20:
               pop2000 = True
          if num >=21 and num <=22:
               pop2008 = True
          if num >=23 and num<=24:
               pop2015=True
print()
Playlist= set([''])
while (len(Playlist)<16):
     if rap:      
          RAP = open("rap.txt")
          #end1=0
          #end2=0
          #end3=0
          end=calcEnds("rap.txt")#,end1,end2,end3) print(str(end1)+' '+str(end2)+' '+str(end3))
          #try again
          # so should we do a function n pass these in as parameters, since we'll use same function for all cate
          #yeah lets make a function
          # bruh wat its printing 17
          #lmfaoo
          #fr imma give up, run one last time
          rap1 = random.randint(1, end[0])#17
          rap2 = random.randint(end[0]+3, end[1])#20,40
          rap3 = random.randint(end[1]+3, end[2])#43,62
          content=RAP.readlines()
          if rap2000:
               #print(str(rap1+1)+' rap2000 '+content[rap1])
               Playlist.add(content[rap1])
          if rap2008:
               #print(str(rap2+1)+' rap2008 '+content[rap2])
               Playlist.add(content[rap2])
          if rap2015:
               #print(str(rap3+1)+' rap2015 '+content[rap3])
               Playlist.add(content[rap3])
          RAP.close()
     if country:
          COUNTRY = open("country.txt")
          country1 = random.randint(1, 22)
          country2 = random.randint(25, 40) 
          country3 = random.randint(43, 62)
          content=COUNTRY.readlines()
          if country2000:
               #print(str(country1+1) + ' country2000 - '+content[country1])
               Playlist.add(content[country1])
          if country2008:
               #print(str(country2+1) + ' country2008 - '+content[country2])
               Playlist.add(content[country2])
          if country2015:
               #print(str(country3+1) + ' country2015 - '+content[country3])
               Playlist.add(content[country3])
          COUNTRY.close()
     if pop:
          POP = open("pop.txt")
          pop1 = random.randint(1, 11)
          pop2 = random.randint(14, 33) 
          pop3 = random.randint(36, 55)
          content=POP.readlines()
          if pop2000:
               #print(str(pop1+1) + ' pop2000 - '+content[pop1])
               Playlist.add(content[pop1])
          if pop2008:
               #print(str(pop2+1) + ' pop2008 - '+content[pop2])
               Playlist.add(content[pop2])
          if pop2015:
               #print(str(pop3+1) + ' pop2015 - '+content[pop3])
               Playlist.add(content[pop3])
          POP.close()
     if rb:
          RB = open("rb.txt")
          rb1 = random.randint(1, 15)
          rb2 = random.randint(18, 37) 
          rb3 = random.randint(40, 60)
          content=RB.readlines()
          if rb2000:
               #print(str(rb1+1) + ' rb2000 - '+content[rb1])
               Playlist.add(content[rb1])
          if rb2008:
               #print(str(rb1+1) + ' rb2008 - '+content[rb2])
               Playlist.add(content[rb2])
          if rb2015:
               #print(str(rb1+1) + ' rb2015 - '+content[rb3])
               Playlist.add(content[rb3])
          RB.close()
     if classical:
          CLASSICAL = open("classical.txt")
          classical1 = random.randint(1, 50)
          for i, line in enumerate(CLASSICAL):
              if i == classical1:
                   #print(str(i) + ' Classical all time - '+line)
                   Playlist.add(line)
          CLASSICAL.close()
print('The length of the playlist is :' + str(len(Playlist)))
print('Your playlist :')
print(*Playlist)
