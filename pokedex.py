import requests
from bs4 import BeautifulSoup
import tkinter as tk
from PIL import ImageTk, Image

"""
Dawn Suehle 5/13/24
This project was difficult, to say the least I had to work with 2 hard to work with modules being 
tkinter and web scraping tkinter can just break sometimes and figuring out how to do directories 
with it took like a day's worth of work. Web scrapping was annoying because of all the formatting 
I had to do with the HTML. I feel good about what im at at the moment although there are 2-3 more features
I want to add being fixing a problem with displaying images making it so you can type in a Pokemon's
name to search and just making the UI look better.
"""

#plase input the directory all the way to the images folder
directory=r"[insert directory]\pics"



#creates an empty string varable for use later
gcheck=""
#ask for the pokemon in wich will display first
pokenum= input("input a number from 1 to 1025")
#formats the number for use in the URL
if len(pokenum)==1:
    pokenum=f"000{pokenum}"
if len(pokenum)==2:
    pokenum=f"00{pokenum}"
if len(pokenum)==3:
    pokenum=f"0{pokenum}"    
# Making a GET request for the URL
r = requests.get(f'https://sg.portal-pokemon.com/play/pokedex/{pokenum}')
 
#empty string for use later
new_string =""

#a list of types of images to be looped trough later
imgdif=['uk','mf','fd','fo','mo','md']
        
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
#turning it into a strinh
soup=str(soup)
#turn the string int a list
yes=soup.split()
#filtering for what I need in the list
x=[item for item in yes if '>' not in item]    
y=[item for item in x if '<' not in item] 
#hels later in the formating
type=['pokemon-type__type--normal','pokemon-type__type--fire','pokemon-type__type--water','pokemon-type__type--grass','pokemon-type__type--flying','pokemon-type__type--fighting','pokemon-type__type--poison','pokemon-type__type--electric','pokemon-type__type--ground','pokemon-type__type--rock','pokemon-type__type--psychic','pokemon-type__type--ice','pokemon-type__type--bug','pokemon-type__type--ghost','pokemon-type__type--steel','pokemon-type__type--dragon','pokemon-type__type--dark','pokemon-type__type--fairy']
wordcnt=0
INH=""
#formats for the actual things that will be displayed
for word in y:
    if word in type:
        new_string+= f"{word} "
    elif "content" and "Pokédex" in word:
        INH+=y[wordcnt-1]
        new_string+= f"{word} "
    wordcnt+=1
work=new_string.split()
look=[]
var=0
work[1]=f"{INH} {work[1]}"
#changes the items that I need into more readable items
for string in work:
    cnt=0
    str1=""
    if string in type:
        cnt=-1
    if var==1:
        if  string.startswith('|in| content='):
            for letter in string:
                if letter == ",":
                    cnt+=1
                if cnt==1:
                    str1+=letter
                if letter =='"':
                    cnt+=1
                if letter =='_':
                    cnt+=1

        if  string.startswith('|content='):
            
            for letter in string:
                if letter == ',':
                    cnt+=1
                if letter=='|':
                    continue
                elif cnt==1:
                    str1+=letter
                if letter=='"':
                    cnt+=1
        for letter in string:
            if letter==',':
                cnt+=1
            if cnt==0:
                str1+=letter                
                
    else:
        for letter in string:
            if letter == ",":
                cnt+=1
            if cnt==1:
                str1+=letter
            if letter =='"':
                cnt+=1
            if letter =='_':
                cnt+=1
        
    var+=1    
    look.append(str1)
#makes a variable that will be used a lot to tell what form a pokemon is
formcnt=0

cnt=0  
string=""
#for the next lines it checs to make sure the pokemon has a form and to format that in
form_check=[item for item in yes if 'size-20' in item]    

final_form=[]
for item in yes:
    if cnt==1 and item=="</div>":
        cnt+=1
    if item == form_check[1]:
        cnt+=1
    if cnt==1:
        final_form.append(item)
cnt=0
formstring=""
for item in final_form:
    formstring+=f"{item} "
for letter in formstring:
    if letter =='<':
        cnt+=1
    if cnt==1:
        string+=letter
    if letter=='>':
        cnt+=1
formstring=string   
if not 'Mega' in formstring:
    look[1]=f"{formstring} {look[1]}"

def formater():
    """
    it has all of the common code throughout the comming functions that will get the website and format it down to the display

    Returns
    -------
    None.

    """
    global pokenum,r,type,y,new_string,look,formcnt,gcheck,imgdif    
    #this try is here for image display reasons
    try:
        #gets html parsses it resets a variable
        r = requests.get(f'https://sg.portal-pokemon.com/play/pokedex/{pokenum}_{formcnt}')
        new_string =""
           
    
        soup = BeautifulSoup(r.content, 'html.parser')
        soup=str(soup)
        yes=soup.split()
        #starts formating it
        x=[item for item in yes if '>' not in item]    
        y=[item for item in x if '<' not in item] 
        #craetes variables word count and INH(I need help because i cant think of another name for a string variable)
        wordcnt=0
        INH=""
        for word in y:
            if word in type:
                new_string+= f"{word} "
            elif "content" and "Pokédex" in word:
                INH+=y[wordcnt-1]
                new_string+= f"{word} "
            wordcnt+=1
        #turns string into a lsit and creatws and assigns a few things
        work=new_string.split()
        look=[]
        var=0
        work[1]=f"{INH} {work[1]}"
        #starts the basic format loop
        for string in work:
            cnt=0
            str1=""
            if string in type:
                cnt=-1
            if var==1:
                #each if for a differnt reason because pokemons html is stupid
                if  string.startswith('|in| content='):
                    for letter in string:
                        if letter == ",":
                            cnt+=1
                        if cnt==1:
                            str1+=letter
                        if letter =='"':
                            cnt+=1
                        if letter =='_':
                            cnt+=1
    
                if  string.startswith('|content='):
                    
                    for letter in string:
                        if letter == ',':
                            cnt+=1
                        if letter=='|':
                            continue
                        elif cnt==1:
                            str1+=letter
                        if letter=='"':
                            cnt+=1
                for letter in string:
                    if letter==',':
                        cnt+=1
                    if cnt==0:
                        str1+=letter                
                        
            else:
                for letter in string:
                    if letter == ",":
                        cnt+=1
                    if cnt==1:
                        str1+=letter
                    if letter =='"':
                        cnt+=1
                    if letter =='_':
                        cnt+=1
                
            var+=1    
            look.append(str1)
        #starts checking for forms and assigning them
        if 'X' in look[1]:
            if pokenum=="0006":
                look[1]="Mega Charizard X"
            else:
                look[1]="Mega Mewtwo X"
        elif 'Y' in look[1]:
            if pokenum=="0006":
                look[1]="Mega Charizard Y"
            else:
                look[1]="Mega Mewtwo Y"
        elif 'content="Mega'in y:
            look[1]=f"{look[1]}"
        elif 'size-20">Gigantamax</p>'in yes:
            #g check stands for gigantimax check because of how the stupid images are formated
            if gcheck=='g':
                gcheck=''
                formcnt=1
            else:   
                 gcheck="g"
                 look[1]=f"Gigantimax {look[1]}" 
                 formcnt=0
        elif 'size-20">Alola'in yes:
            look[1]=f"Alolan {look[1]}"  
        elif 'size-20">Galarian'in yes:
            look[1]=f"Galarian {look[1]}"           
        elif 'size-20">Paldean'in yes:
            look[1]=f"Paldean {look[1]}" 
        elif 'size-20">Hisuian'in yes:
            look[1]=f"Hisuian {look[1]}" 
        else:
            cnt=0
            string=""
            form_check=[item for item in yes if 'size-20' in item]    
            
            final_form=[]
            for item in yes:
                if cnt==1 and item=="</div>":
                    cnt+=1
                if item == form_check[1]:
                    cnt+=1
                if cnt==1:
                    final_form.append(item)
            cnt=0
            formstring=""
            for item in final_form:
                formstring+=f"{item} "
            for letter in formstring:
                if letter =='<':
                    cnt+=1
                if cnt==1:
                    string+=letter
                if letter=='>':
                    cnt+=1
            formstring=string   

            if not form_check[1] =='</p>':
                look[1]=f"{formstring} {look[1]}"      
        #changes the labels to what they need to be
        lbl_1.config(text=look[1])
        lbl_2.config(text=look[3])
        if len(look)==5:
            lbl_3.config(text=look[4])
        else:
            lbl_3.config(text="") 
    #the except to the earlier try
    except:
        #grabs the correct images from the folder
        if gcheck == 'g':
            for dif in imgdif:
                try:
                    path = directory + f'/poke_icon_{pokenum}_00{formcnt}_{dif}_g_00000000_f_n.png'
                    img = ImageTk.PhotoImage(Image.open(path))
                    panel.configure(image=img)
                    panel.image = img
                except:
                    continue
        else:
            for dif in imgdif:
                try:
                    path = directory + f'/poke_icon_{pokenum}_00{formcnt}_{dif}_n_00000000_f_n.png'
                    img = ImageTk.PhotoImage(Image.open(path))
                    panel.configure(image=img)
                    panel.image = img
                except:
                    continue

    if gcheck == 'g':
        for dif in imgdif:
            try:
                path = directory + f'/poke_icon_{pokenum}_00{formcnt}_{dif}_g_00000000_f_n.png'
                img = ImageTk.PhotoImage(Image.open(path))
                panel.configure(image=img)
                panel.image = img
            except:
                continue
    else:
        for dif in imgdif:
            try:
                path = directory + f'/poke_icon_{pokenum}_00{formcnt}_{dif}_n_00000000_f_n.png'
                img = ImageTk.PhotoImage(Image.open(path))
                panel.configure(image=img)
                panel.image = img
            except:
                continue
    lbl_4.config(text=f"#{pokenum}")
def shiny_btn():
    """
    for the shinify button changes the displayed image to the shiny version

    Returns nothing
    -------
    None.

    """
    #just changes the displayed image to the shiny version
    global imgdif
    if gcheck == 'g':
        for dif in imgdif:
            try:
                path = directory + f'/poke_icon_{pokenum}_00{formcnt}_{dif}_g_00000000_f_r.png'
                img = ImageTk.PhotoImage(Image.open(path))
                panel.configure(image=img)
                panel.image = img
            except:
                continue
    else:
        for dif in imgdif:
            try:
                path = directory + f'/poke_icon_{pokenum}_00{formcnt}_{dif}_n_00000000_f_r.png'
                img = ImageTk.PhotoImage(Image.open(path))
                panel.configure(image=img)
                panel.image = img
            except:
                continue
def search_btn_click():
    """
    does what happens when you click the button search

    Returns nothing
    -------
    None.

    """
    global pokenum,r,type,y,new_string,look,formcnt,gcheck,imgdif
    #resets some variables
    gcheck=""
    t=ent_1.get()
    formcnt=0
    #formats pokenum to work
    if len(t)==1:
        pokenum=f"000{t}"
    elif len(t)==2:
        pokenum=f"00{t}"
    elif len(t)==3:
        pokenum=f"0{t}"
    else:
        pokenum=t
    print(pokenum,t,len(t))
    
    formater()
def form_up():
    """
    changes the pokemons form if it has one to the next form

    Returns noting
    -------
    None.

    """
    global pokenum,r,type,y,new_string,look,formcnt,gcheck
    formcnt+=1
    formater()
def form_dwn():
    """
    changes the pokemons form if it has one to the previous form

    Returns noting
    -------
    None.

    """
    global pokenum,r,type,y,new_string,look,formcnt,gcheck
    formcnt-=1
    formater()
def poke_up():
    """
    changes to the next pokemon by pokedex number 

    Returns
    -------
    None.

    """
    global pokenum,r,type,y,new_string,look,formcnt,gcheck
    gcheck=""    
    pokenum=int(pokenum)
    pokenum+=1
    pokenum=str(pokenum)
    formcnt=0
    if len(pokenum)==1:
        pokenum=f"000{pokenum}"
    if len(pokenum)==2:
        pokenum=f"00{pokenum}"
    if len(pokenum)==3:
        pokenum=f"0{pokenum}"
    formater()
def poke_down():
    """
    changes to the previous pokemon by pokedex number 

    Returns
    -------
    None.

    """
    global pokenum,r,type,y,new_string,look,formcnt,gcheck
    gcheck=""
    pokenum=int(pokenum)
    pokenum-=1
    pokenum=str(pokenum)
    formcnt=0
    if len(pokenum)==1:
        pokenum=f"000{pokenum}"
    if len(pokenum)==2:
        pokenum=f"00{pokenum}"
    if len(pokenum)==3:
        pokenum=f"0{pokenum}"
    formater()
#creates the root for tkinter and its look
root = tk.Tk()
root.geometry("800x500+69+69")
#makes the font
font = ('Arial',24)
#makes the display image
for dif in imgdif:
    try:
        path = directory + f'/poke_icon_{pokenum}_00{formcnt}_{dif}_n_00000000_f_n.png'
        img = ImageTk.PhotoImage(Image.open(path))
        panel = tk.Label(root, image = img)
        panel.grid(row=0,column=1)
    except:
        continue
#creates all the labels and buttons
lbl_1 = tk.Label(root,text=look[1], font=font)
lbl_1.grid(row=0,column=0)
lbl_2 = tk.Label(root,text=look[3], font=font)
lbl_2.grid(row=1,column=0)
lbl_3 = tk.Label(root,text="", font=font)
lbl_3.grid(row=2,column=0)
lbl_4 = tk.Label(root,text=f"#{pokenum}", font=font)
lbl_4.grid(row=1,column=1)
if len(look)==5:
    lbl_3.config(text=look[4])
#can also pack things ^.pack()
ent_1 = tk.Entry(root, width=40)
ent_1.grid(row=3,column=0)
#creates a bunch of buttons
btn_1=tk.Button(root,text="search",command=search_btn_click, bg="red")
btn_1.grid(row=5,column=0)
btn_6=tk.Button(root,text="shinify",command=shiny_btn, bg="yellow")
btn_6.grid(row=5,column=1)
btn_2=tk.Button(root,text="form up",command=form_up, bg="red")
btn_2.grid(row=7,column=0)
btn_3=tk.Button(root,text="form down",command=form_dwn, bg="red")
btn_3.grid(row=7,column=1)
btn_4=tk.Button(root,text="pokemon # ▲",command=poke_up, bg="red")
btn_4.grid(row=6,column=0)
btn_5=tk.Button(root,text="pokemon # ▼",command=poke_down, bg="red")
btn_5.grid(row=6,column=1)
#starts the window
root.mainloop()

