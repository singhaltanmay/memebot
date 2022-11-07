from doctest import DONT_ACCEPT_BLANKLINE
from operator import ge
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from datetime import datetime
import telegram
import praw
import telepot
import os
import random
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, InputMediaPhoto
from telegram.ext import CallbackQueryHandler, CommandHandler, ContextTypes
import pandas as pd

############################################### LIBS ###############################################

TOKEN="5316299185:AAEFatF3g9yut5ItU-3Je7KBhsKYDgi-jDs"
updater = Updater("5316299185:AAEFatF3g9yut5ItU-3Je7KBhsKYDgi-jDs",
                  use_context=True)
bot = telegram.Bot(token="5316299185:AAEFatF3g9yut5ItU-3Je7KBhsKYDgi-jDs")
PORT=int(os.environ.get('PORT', 5000))
user_dict={}
helper_count=0
start_count=0
meme_count=0
vmeme_count=0
joke_count=0
policy_count=0
ad="To buy advertisement on our services contact Admin \n\n Note : Your advertisement musta adhere to our /policy"
policy = """Your advertisement must adhere to the following :-

✔ Your ad must not contain any sexual explicit information.

✔ Your advertisment must not be scammy in nature.

✔ You can have at most 1 image/GIF/video file as an ad on our services.

✔ The owner in responsible for any misunderstandings aroused due to the ad and bot is not accountable in any scenario.

"""
ad_msg1=''
ad_msg12=''
ad_msg13=''
ad_msg2=''
ad_msg22=''

ad_msg1_count=0
ad_msg2_count=0

user_list={}
user_df=pd.read_csv('users.csv', encoding = "ISO-8859-1")

############################################### VARS ###############################################

def update_block_user():
    d={'152007083':'Cuz you are a piece of sh*t','818576063':'abbey chal na spammer ke 14','1120142014':'abbey chal na spammer ke 14',
       '1875914636':'abbey chal na spammer ke 14'}
    return d
blocked_user=update_block_user()

def get_text(context):
    k = context.args
    y = ""
    try:
        if k==0:
            y=""
        else:
            for i in k:
                y=y+" "+i
            z=y.strip()
            y=z
        return y
    except Exception as e:
        print(str(e))
        return ""

def meme(genre='random'):
    reddit=praw.Reddit(client_id='m4ome4-BWHCTubwpoMXs_A',
                   client_secret='2Md4F_mp6r4-6O5SZMYoeR3x5Y0vDA',
                   user_agent='meme-collector')
    
    dank=['dankindianmemes','dankmemes','IndianDankMemes','dankindia','rareinsults','MurderedByWords','suicidebywords','DarkMemes_69']
    crypto=['cryptocurrencymemes','cryptomemes','bitcoinmemes','buttcoin','dogecoin']
    programming=['ProgrammerHumour']
    chess=['AnarchyChess']
    wholesome=['wholesomememes','memes','meme','Funnymemes','funny']
    science=['physicsmemes','sciencememes','chemistrymemes','biologymemes']
    irl=['me_irl','meirl','2meirl4meirl']
    indian=['dankindianmemes','IndianDankMemes','dankindia','bakchodi','DHHmemes']
    twitter=['Twitter_memes','terriblefacebookmemes','clevercomebacks','MurderedByWords']
    shitty=['shitposting','DevilMayCry','NobodyAsked','bakchodi','puns']
    rand=['ProgrammerHumour','AnarchyChess','Twitter_memes','clevercomebacks','MoldyMemes','2meirl4meirl','me_irl','memes','IndianDankMemes','dankmemes',
           'dankindianmemes','ComedyCemetry','PrequelMemes','terriblefacebookmemes','funny','physicsmemes','sciencememes','shitposting','dankindia',
           'wholesomememes','meme','PewdiepieSubmissions','rareinsults','MurderedByWords','suicidebywords','puns','NobodyAsked','DevilMayCry','meirl',
           'DHHMemes','DarkMemes_69','Funnymemes','bakchodi','biologymemes','chemistrymemes']

    if genre=='dank':
        pages=dank
    elif genre=='crypto':
        pages=crypto
    elif genre=='programming':
        pages=programming
    elif genre=='chess':
        pages=chess
    elif genre=='wholesome':
        pages=wholesome
    elif genre=='science':
        pages=science
    elif genre=='irl':
        pages=irl
    elif genre=='indian':
        pages=indian
    elif genre=='twitter':
        pages=twitter
    elif genre=='shitty':
        pages=shitty
    else:
        pages=rand

    categories = ['hot','top','rising']
    x=random.randint(0,2)
    try:
        z=random.randint(0,len(pages)-1)
    except:
        z=0
    subreddit = reddit.subreddit(pages[z])
    if x==0:
        posts = subreddit.hot(limit=20)
    elif x==1:
        posts = subreddit.top(limit=20)
    elif x==2:
        posts = subreddit.rising(limit=20)
    else:
        print('error')
    final=[]
    image_urls=[]
    titles=[]
    title=[]
    final3=[]
    pl=[]
    post_link=[]
    for post in posts:
          
        image_urls.append(post.url.encode('utf-8'))
        titles.append(post.title)
        pl.append("https://www.reddit.com" + post.permalink)
    
    for index, url in enumerate(image_urls):
        final.append(url)
    
    
    for x in range(len(final)):
        f=str(final[x])
        if ('.jpg' not in f) and ('.jpeg' not in f) and ('.png' not in f):
            continue
        else:
            final3.append(final[x])
            title.append(titles[x])
            post_link.append(pl[x])
            
    #print(final)
    #print(titles)
    #print(len(titles)==len(final))
    final2=[]
    for i in final3:
        i=str(i)
        f=''
        l=list(i)
        l.remove(l[0])
        l.remove(l[0])
        l.remove(l[len(l)-1])
        for i in l:
            f+=i
        final2.append(f)
    final4=[]
    title2=[]
    post_link_final=[]
    for x in range(len(final2)):
        i=final2[x]
        if ('.jpg' in i) or ('.jpeg' in i) or ('.png' in i):
            final4.append(final2[x])
            title2.append(title[x])
            post_link_final.append(post_link[x])
        else:
            continue
    z2=random.randint(0,len(final4)-1)  


    return final2[z2]+'////'+title2[z2]+'////'+post_link_final[z2]
    
def vmeme(genre='random'):
    final4=[]
    reddit=praw.Reddit(client_id='m4ome4-BWHCTubwpoMXs_A',
                   client_secret='2Md4F_mp6r4-6O5SZMYoeR3x5Y0vDA',
                   user_agent='meme-collector')
    
    dank=['dankvideos','IndianDankMemes','dankindia']
    irl=['me_irl','meirl']
    wholesome=['funny','memes','meme','AnimalsBeingDerps','funnyvideos','Funnymemes']
    shitty=['shitposting','bakchodi','DiWHY','ContagiousLaughter']
    science=['physicsmemes','sciencememes','chemistrymemes','biologymemes']
    all=['memes','funny','meirl','dankvideos','IndianDankMemes','dankindia','me_irl','shitposting','meme','AnimalsBeingDerps','DiWHY','ContagiousLaughter',
           'unexpected','funnyvideos','DHHMemes','Funnymemes','bakchodi']
    if genre=='dank':
        pages=dank
    elif genre=='irl':
        pages=irl
    elif genre=='wholesome':
        pages=wholesome
    elif genre=='shitty':
        pages=shitty
    elif genre=='science':
        pages=science
    else:
        pages=all
    categories = ['hot','top','rising']
    while final4==[]:
        x=random.randint(0,2)
        z=random.randint(0,len(pages)-1)
        subreddit = reddit.subreddit(pages[z])
        if x==0:
            posts = subreddit.hot(limit=50)
        elif x==1:
            posts = subreddit.top(limit=50)
        elif x==2:
            posts = subreddit.rising(limit=50)
        else:
            print('error')
        final=[]
        video_urls=[]
        titles=[]
        title=[]
        final3=[]
        pl=[]
        post_link=[]
        
        for post in posts:
        
            video_urls.append(post.url.encode('utf-8'))
            titles.append(post.title)
            pl.append("https://www.reddit.com" + post.permalink)
        
        for index, url in enumerate(video_urls):
            final.append(url)
    
        for x in range(len(final)):
            f=str(final[x])
            if ('.jpg' not in f) and ('.jpeg' not in f) and ('.png' not in f):
                final3.append(final[x])
                title.append(titles[x])
                post_link.append(pl[x])
                
            else:
                continue
    #print(final)
    #print(titles)
    #print(len(titles)==len(final))
        final2=[]
        for i in final3:
            i=str(i)
            f=''
            l=list(i)
            l.remove(l[0])
            l.remove(l[0])
            l.remove(l[len(l)-1])
            for i in l:
                f+=i
            final2.append(f)
    
        title2=[]
        post_link_final=[]
        
        for x in range(len(final2)):
            i=final2[x]
            if ('.jpg' in i) or ('.jpeg' in i) or ('.png' in i) or ('v.redd.it' not in i):
                continue
            else:
                final4.append(final2[x])
                title2.append(title[x])
                post_link_final.append(post_link[x])
                
            if ('.jpg' in i) or ('.jpeg' in i) or ('.png' in i) or ('v.redd.it' not in i):
                continue
            else:
                final4.append(final2[x])
                title2.append(title[x])
                post_link_final.append(post_link[x])
                
    z2=random.randint(0,len(final4)-1)
    
    
    return final4[z2]+'////'+title2[z2]+'////'+post_link_final[z2]

def jokes():
    reddit=praw.Reddit(client_id='m4ome4-BWHCTubwpoMXs_A',
                   client_secret='2Md4F_mp6r4-6O5SZMYoeR3x5Y0vDA',
                   user_agent='meme-collector')
    pages=['jokes','parrotjokes','JokesAreDark','darkjokes']
    x=random.randint(0,3)
    z=random.randint(0,len(pages)-1)
    subreddit = reddit.subreddit(pages[z])
    if x==0:
        posts = subreddit.hot(limit=50)
    elif x==1:
        posts = subreddit.top(limit=50)
    elif x==2:
        posts = subreddit.new(limit=50)
    elif x==3:
        posts = subreddit.rising(limit=50)
    else:
        print('error')
    final=[]
    joke_urls=[]
    titles=[]
    title=[]
    final3=[]
    pl=[]
    
    for post in posts:
        
        joke_urls.append(post.selftext)
        titles.append(post.title)
        pl.append("https://www.reddit.com" + post.permalink)
    
    for index, url in enumerate(joke_urls):
        final.append(url)
        
    z2=random.randint(0,len(final)-1)
    return titles[z2]+'////'+final[z2]+'////'+pl[z2]

############################################### WORKING FUNCS ###############################################

def start(update: Update, context: CallbackContext):
    global start_count
    global ad
    global blocked_user
    global user_list
    global ad_msg1_count
    global ad_msg2_count
    global user_dict
    
    z=random.randint(1,2)
    user = update.message.from_user
    if str(user['id']) in blocked_user:
        reply="You are blocked by Administrators. Reason: '"+blocked_user[str(user['id'])].capitalize()+"'"
        update.message.reply_text(reply)
    else:
        first_name=str(user['first_name'])
        last_name=str(user['last_name'])
        user_name=str(user['username'])
        user_id=str(user['id'])
        
        if user_id not in user_dict:
            user_dict[user_id] = [user_id, update.message.chat_id, first_name]
        else:
            user_dict=user_dict
            
        if user_id not in user_list:
            user_list[user_id]=0
        else:
            user_list[user_id]=user_list[user_id]
        is_bot=str(user['is_bot'])
        language_code=str(user['language_code'])
        now = datetime.now()
        start_count+=1
        
        update.message.reply_text(
            "<b>⚠️ I'm gonna die on 28th November, 2022. Only your help can save me from extinction. Contact @the_modern_prometheus to help and save me!!! ⚠️</b> \nWrite /help to see the commands available.", parse_mode='html')
        
        update.message.reply_text(ad)
        user_list[user_id]+=1
        if user_id in user_list:
            fre=user_list[user_id]
        else:
            fre=0
        z=1
        if fre>=4 and z==1:
            user_list[user_id]=0
            #bot.send_photo(chat_id=update.effective_chat.id, photo="https://i.imgur.com/ji6XCUV.jpeg", caption=ad_msg1+ad_msg12, parse_mode='html')
            ad_status='ad shown'
            ad_msg1_count+=1
        elif fre>=4 and z==2:
            user_list[user_id]=0
            #bot.send_photo(chat_id=update.message.chat_id, photo=open("ad2.jpg", 'rb'), caption=ad_msg2+ad_msg22, parse_mode='html')
            ad_status='ad shown'
            ad_msg2_count+=1
        else:
            user_list[user_id]=user_list[user_id]
            ad_status='not now'
        print(str(now) +", Ad_status: "+ad_status+", user_fre: "+str(fre)+", Frequency: " + str(start_count) + ", Command: '/start" + "' , Other : [FirstName:'" + first_name + "', LastName:'" + last_name + "', Username:'" + user_name + "', UserID:'" + user_id + "', IsBot:'" + is_bot + "', LanguageCode:'" + language_code + "']")

def helper(update: Update, context: CallbackContext):
    global helper_count
    global blocked_user
    global user_list
    global ad_msg1_count
    global ad_msg2_count
    global user_dict
    
    z=random.randint(1,2)
    user = update.message.from_user
    if str(user['id']) in blocked_user:
        reply="You are blocked by Administrators. Reason: '"+blocked_user[str(user['id'])].capitalize()+"'"
        update.message.reply_text(reply)
    else:
        first_name=str(user['first_name'])
        last_name=str(user['last_name'])
        user_name=str(user['username'])
        user_id=str(user['id'])


        if user_id not in user_dict:
            user_dict[user_id] = [user_id, update.message.chat_id, first_name]
        else:
            user_dict=user_dict
        
        if user_id not in user_list:
            user_list[user_id]=0
        else:
            user_list[user_id]=user_list[user_id]
        is_bot=str(user['is_bot'])
        language_code=str(user['language_code'])
        now = datetime.now()
        helper_count+=1
        user_list[user_id]+=1
        if user_id in user_list:
            fre=user_list[user_id]
        else:
            fre=0

        z=1
        
        if fre>=4 and z==1:
            user_list[user_id]=0
            #bot.send_photo(chat_id=update.effective_chat.id, photo="https://i.imgur.com/ji6XCUV.jpeg", caption=ad_msg1+ad_msg12, parse_mode='html')
            ad_status='ad shown'
            ad_msg1_count+=1
        elif fre>=4 and z==2:
            user_list[user_id]=0
            #bot.send_photo(chat_id=update.message.chat_id, photo=open("ad2.jpg", 'rb'), caption=ad_msg2+ad_msg22, parse_mode='html')
            ad_status='ad shown'
            ad_msg2_count+=1
        else:
            user_list[user_id]=user_list[user_id]
            ad_status='not now'
        
        print(str(now) + ", Ad_status: "+ad_status+", user_fre: "+str(fre)+", Frequency: " + str(helper_count) + ", Command: '/help" + "' , Other : [FirstName:'" + first_name + "', LastName:'" + last_name + "', Username:'" + user_name + "', UserID:'" + user_id + "', IsBot:'" + is_bot + "', LanguageCode:'" + language_code + "']")
        keyboard=[[InlineKeyboardButton(text='Add to group', url='https://t.me/MemeGetterBot?startgroup=a')]]
        reply_markup=InlineKeyboardMarkup(keyboard)
        
        update.message.reply_text("""I can help you burst out into laughter... Add me to your groups or enjoy personally with following commands :-

<code>/meme</code> <i> filter</i> - To get the memes sorted by desired flairs

<code>/vmeme</code> <i> filter</i> - To get video/gif memes sorted by desired flairs

Supported Flairs : <code>dank</code>
                               : <code>crypto</code>
                               : <code>programming</code>
                               : <code>chess</code>
                               : <code>wholesome</code>
                               : <code>science</code>
                               : <code>irl</code>
                               : <code>indian</code>
                               : <code>twitter</code>
                               : <code>shitty</code>

/joke - To get text message jokes

/policy - To buy advertisement on our services

                            """, reply_markup=reply_markup, parse_mode='html')

def meme_get(update: Update, context: CallbackContext):
    global meme_count
    global blocked_user
    global user_list
    global ad_msg1_count
    global ad_msg2_count
    global user_dict
    z=random.randint(1,2)
    user = update.message.from_user
    try:
        genre=get_text(context)
    except:
        genre='random'
    if str(user['id']) in blocked_user:
        reply="You are blocked by Administrators. Reason: '"+blocked_user[str(user['id'])].capitalize()+"'"
        update.message.reply_text(reply)
    else:
        try:
            photos=meme(genre=genre)
        except:
            try:
                photos=meme(genre=genre)
            except:
                photos=meme(genre=genre)
            photos=meme(genre=genre)
        l=photos.split('////')
        
        keyboard=[[InlineKeyboardButton("Next → ", callback_data='meme_nxt////'+genre),
                   InlineKeyboardButton("Source", url=l[2]),]]
        reply_markup=InlineKeyboardMarkup(keyboard)
        
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=l[0], caption=l[1], reply_markup=reply_markup)
        
        first_name=str(user['first_name'])
        last_name=str(user['last_name'])
        user_name=str(user['username'])
        user_id=str(user['id'])
    
        if user_id not in user_dict:
            user_dict[user_id] = [user_id, update.message.chat_id, first_name]
        else:
            user_dict=user_dict
        
        if user_id not in user_list:
            user_list[user_id]=0
        else:
            user_list[user_id]=user_list[user_id]
        is_bot=str(user['is_bot'])
        language_code=str(user['language_code'])
        now = datetime.now()
        meme_count+=1
        user_list[user_id]+=1
        if user_id in user_list:
            fre=user_list[user_id]
        else:
            fre=0
        z=1
        if fre>=4 and z==1:
            user_list[user_id]=0
            #bot.send_photo(chat_id=update.effective_chat.id, photo="https://i.imgur.com/ji6XCUV.jpeg", caption=ad_msg1+ad_msg12, parse_mode='html')
            ad_status='ad shown'
            ad_msg1_count+=1
        elif fre>=4 and z==2:
            user_list[user_id]=0
            #bot.send_photo(chat_id=update.message.chat_id, photo=open("ad2.jpg", 'rb'), caption=ad_msg2+ad_msg22, parse_mode='html')
            ad_status='ad shown'
            ad_msg2_count+=1
        else:
            user_list[user_id]=user_list[user_id]
            ad_status='not now'
        
        print(str(now) + ", Ad_status: "+ad_status+", user_fre: "+str(fre)+", Frequency: " + str(meme_count) + ", Command: '/meme" + "' , Other : [FirstName:'" + first_name + "', LastName:'" + last_name + "', Username:'" + user_name + "', UserID:'" + user_id + "', IsBot:'" + is_bot + "', LanguageCode:'" + language_code + "']")

def vmeme_get(update: Update, context: CallbackContext):
    global vmeme_count
    global blocked_user
    global user_list
    global ad_msg1_count
    global ad_msg2_count
    global user_dict
    z=random.randint(1,2)
    try:
        genre=get_text(context)
    except:
        genre='random'
    user = update.message.from_user
    if str(user['id']) in blocked_user:
        reply="You are blocked by Administrators. Reason: '"+blocked_user[str(user['id'])].capitalize()+"'"
        update.message.reply_text(reply)
    else:
        try:
            videos=vmeme()
        except:
            try:
                videos=vmeme()
            except:
                videos=vmeme()
            videos=vmeme()
        l=videos.split('////')
        keyboard=[[InlineKeyboardButton("Next  → ", callback_data='vmeme_nxt////'+genre),
                   InlineKeyboardButton("Source", url=l[2]),]]
        reply_markup=InlineKeyboardMarkup(keyboard)
        
        if '.gif' in l[0]:
            bot.send_document(chat_id=update.message.chat_id, document=l[0], caption=l[1], reply_markup=reply_markup)
        else:
            try:
                
                bot.send_document(chat_id=update.message.chat_id, document=l[0]+"/DASH_360.mp4", caption=l[1], reply_markup=reply_markup)
            except:
                try:
                    bot.send_document(chat_id=update.message.chat_id, document=l[0]+"/DASH_360.mp4", caption=l[1], reply_markup=reply_markup)
                except:
                    bot.send_document(chat_id=update.message.chat_id, document=l[0]+"/DASH_360.mp4", caption=l[1], reply_markup=reply_markup)
                bot.send_document(chat_id=update.message.chat_id, document=l[0]+"/DASH_360.mp4", caption=l[1], reply_markup=reply_markup)
                
        first_name=str(user['first_name'])
        last_name=str(user['last_name'])
        user_name=str(user['username'])
        user_id=str(user['id'])

        if user_id not in user_dict:
            user_dict[user_id] = [user_id, update.message.chat_id, first_name]
        else:
            user_dict=user_dict
    
        if user_id not in user_list:
            user_list[user_id]=0
        else:
            user_list[user_id]=user_list[user_id]
        is_bot=str(user['is_bot'])
        language_code=str(user['language_code'])
        now = datetime.now()
        vmeme_count+=1
        user_list[user_id]+=1
        if user_id in user_list:
            fre=user_list[user_id]
        else:
            fre=0
        z=1
        if fre>=4 and z==1:
            user_list[user_id]=0
            #bot.send_photo(chat_id=update.effective_chat.id, photo="https://i.imgur.com/ji6XCUV.jpeg", caption=ad_msg1+ad_msg12, parse_mode='html')
            ad_status='ad shown'
            ad_msg1_count+=1
        elif fre>=4 and z==2:
            user_list[user_id]=0
            #bot.send_photo(chat_id=update.message.chat_id, photo=open("ad2.jpg", 'rb'), caption=ad_msg2+ad_msg22, parse_mode='html')
            ad_status='ad shown'
            ad_msg2_count+=1
        else:
            user_list[user_id]=user_list[user_id]
            ad_status='not now'
        
        print(str(now) + ", Ad_status: "+ad_status+", user_fre: "+str(fre)+", Frequency: " + str(vmeme_count) + ", Command: '/vmeme" + "' , Other : [FirstName:'" + first_name + "', LastName:'" + last_name + "', Username:'" + user_name + "', UserID:'" + user_id + "', IsBot:'" + is_bot + "', LanguageCode:'" + language_code + "']")

def joke_get(update: Update, context: CallbackContext):
    global joke_count
    global blocked_user
    global user_list
    global ad_msg1_count
    global ad_msg2_count
    global user_dict
    z=random.randint(1,2)
    user = update.message.from_user
    if str(user['id']) in blocked_user:
        reply="You are blocked by Administrators. Reason: '"+blocked_user[str(user['id'])].capitalize()+"'"
        update.message.reply_text(reply)
    else:
        try:
            joke=jokes()
        except:
            try:
                joke=jokes()
            except:
                joke=jokes()
            joke=jokes
            
        l=joke.split('////')
        
        keyboard=[[InlineKeyboardButton("Next  → ", callback_data='joke_nxt'),
                   InlineKeyboardButton("Source", url=l[2]),]]
        reply_markup=InlineKeyboardMarkup(keyboard)
        
        bot.send_message(chat_id=update.message.chat_id, text=l[0]+'\n\n'+l[1], reply_markup=reply_markup)
        
        first_name=str(user['first_name'])
        last_name=str(user['last_name'])
        user_name=str(user['username'])
        user_id=str(user['id'])
            
        if user_id not in user_dict:
            user_dict[user_id] = [user_id, update.message.chat_id, first_name]
        else:
            user_dict=user_dict
        
        if user_id not in user_list:
            user_list[user_id]=0
        else:
            user_list[user_id]=user_list[user_id]
        is_bot=str(user['is_bot'])
        language_code=str(user['language_code'])
        now = datetime.now()
        joke_count+=1
        user_list[user_id]+=1
        if user_id in user_list:
            fre=user_list[user_id]
        else:
            fre=0

        z=1
        
        if fre>=4 and z==1:
            user_list[user_id]=0
            #bot.send_photo(chat_id=update.effective_chat.id, photo="https://i.imgur.com/ji6XCUV.jpeg", caption=ad_msg1+ad_msg12, parse_mode='html')
            ad_status='ad shown'
            ad_msg1_count+=1
        elif fre>=4 and z==2:
            user_list[user_id]=0
            #bot.send_photo(chat_id=update.message.chat_id, photo=open("ad2.jpg", 'rb'), caption=ad_msg2+ad_msg22, parse_mode='html')
            ad_status='ad shown'
            ad_msg2_count+=1
        else:
            user_list[user_id]=user_list[user_id]
            ad_status='not now'
        
        print(str(now) + ", Ad_status: "+ad_status+", user_fre: "+str(fre)+", Frequency: " + str(joke_count) + ", Command: '/joke" + "' , Other : [FirstName:'" + first_name + "', LastName:'" + last_name + "', Username:'" + user_name + "', UserID:'" + user_id + "', IsBot:'" + is_bot + "', LanguageCode:'" + language_code + "']")

def policy_msg(update: Update, context: CallbackContext):
    global policy
    global policy_count
    global blocked_user
    global user_list
    global ad_msg1_count
    global ad_msg2_count
    global user_dict
    z=random.randint(1,2)
    user = update.message.from_user
    if str(user['id']) in blocked_user:
        reply="You are blocked by Administrators. Reason: '"+blocked_user[str(user['id'])].capitalize()+"'"
        update.message.reply_text(reply)
    else:
        update.message.reply_text(policy)
        first_name=str(user['first_name'])
        last_name=str(user['last_name'])
        user_name=str(user['username'])
        user_id=str(user['id'])
            
        if user_id not in user_dict:
            user_dict[user_id] = [user_id, update.message.chat_id, first_name]
        else:
            user_dict=user_dict
        
        if user_id not in user_list:
            user_list[user_id]=0
        else:
            user_list[user_id]=user_list[user_id]
        is_bot=str(user['is_bot'])
        language_code=str(user['language_code'])
        now = datetime.now()
        policy_count+=1
        user_list[user_id]+=1
        if user_id in user_list:
            fre=user_list[user_id]
        else:
            fre=0
        z=1
        if fre>=4 and z==1:
            user_list[user_id]=0
            #bot.send_photo(chat_id=update.effective_chat.id, photo="https://i.imgur.com/ji6XCUV.jpeg", caption=ad_msg1+ad_msg12, parse_mode='html')
            ad_status='ad shown'
            ad_msg1_count+=1
        elif fre>=4 and z==2:
            user_list[user_id]=0
            #bot.send_photo(chat_id=update.message.chat_id, photo=open("ad2.jpg", 'rb'), caption=ad_msg2+ad_msg22, parse_mode='html')
            ad_status='ad shown'
            ad_msg2_count+=1
        else:
            user_list[user_id]=user_list[user_id]
            ad_status='not now'
        
        print(str(now) + ", Ad_status: "+ad_status+", user_fre: "+str(fre)+", Frequency: " + str(policy_count) + ", Command: '/policy" + "' , Other : [FirstName:'" + first_name + "', LastName:'" + last_name + "', Username:'" + user_name + "', UserID:'" + user_id + "', IsBot:'" + is_bot + "', LanguageCode:'" + language_code + "']")

def teller(update: Update, context: CallbackContext):
    global user_dict
    bot.send_message(chat_id=1010298479, text=str(user_dict))

def sender(update: Update, context: CallbackContext):
    global user_df
    global ad_msg1
    bheek = "I will <b>DIE</b> on 28th November, 2022 due to lack of monetary support resulting to inability of admins to keep up the bot server. \nOnly your help can save me now. Contact @the_modern_prometheus or click the button below to save me"
    count=0
    passw=get_text(context)
    keyboard=[[InlineKeyboardButton("Help", url="https://t.me/the_modern_prometheus"),
                       InlineKeyboardButton("Donate", url="https://t.me/the_modern_prometheus"),]]
    reply_markup=InlineKeyboardMarkup(keyboard)
    if passw=='tanmayGOD':
        for i in range(len(user_df)):
            df2=user_df.iloc[i]
            try:
                bot.send_photo(chat_id=int(df2.chatID), photo="https://i.imgur.com/SL7V79f.png", caption=bheek, reply_markup = reply_markup, parse_mode='html')
                count+=1
                print(count)
            except:
                continue
        print('done')
    else:
        bot.send_message(chat_id=update.effective_chat.id, text="fuck off")

def queryHandler(update: Update, context: CallbackContext):
    global user_list
    global joke_count
    global meme_count
    global vmeme_count
    
    query=update.callback_query
    user = update.callback_query.from_user
    user_id=str(user['id'])
    first_name=user['first_name']
    try:
        fre=user_list[user_id]
    except:
        user_dict[user_id] = [user_id, query.message.chat_id, first_name]
        user_list[user_id]=0
        fre=0
    data=query.data
    keyboard=[]

    if 'meme_nxt' in data:
        genre=data.split('////')[1]
        user_list[user_id]=fre+1
            
        try:
            photos=meme(genre)
        except:
            try:
                photos=meme(genre)
            except:
                photos=meme(genre)
            photos=meme(genre)
        l=photos.split('////')
        
        keyboard=[[InlineKeyboardButton("Next  → ", callback_data='meme_nxt////'+genre),
                       InlineKeyboardButton("Source", url=l[2]),]]
        reply_markup=InlineKeyboardMarkup(keyboard)
        
        query.message.edit_media(media=InputMediaPhoto(media=l[0], caption=l[1]), reply_markup=reply_markup)
        meme_count+=1

    elif 'vmeme_nxt' in data:
        user_list[user_id]=fre+1
        genre=data.split('////')[1]
        try:
            videos=vmeme(genre)
        except:
            try:
                videos=vmeme(genre)
            except:
                videos=vmeme(genre)
            videos=vmeme(genre)
        l=videos.split('////')
        
        keyboard=[[InlineKeyboardButton("Next  → ", callback_data='vmeme_nxt////'+genre),
                       InlineKeyboardButton("Source", url=l[2]),]]
        reply_markup=InlineKeyboardMarkup(keyboard)

        query.message.edit_media(media=InputMediaPhoto(media=l[0], caption=l[1]), reply_markup=reply_markup)
        vmeme_count+=1

    elif 'joke_nxt' in data:
        user_list[user_id]=fre+1
        try:
            joke=jokes()
        except:
            try:
                joke=jokes()
            except:
                joke=jokes()
            joke=jokes
            
        l=joke.split('////')
        
        keyboard=[[InlineKeyboardButton("Next  → ", callback_data='joke_nxt'),
                       InlineKeyboardButton("Source", url=l[2]),]]
        reply_markup=InlineKeyboardMarkup(keyboard)

        query.edit_message_text(text=l[0]+'\n\n'+l[1], reply_markup=reply_markup)
        joke_count+=1

############################################### HANDLING FUNCS ###############################################

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', helper))
updater.dispatcher.add_handler(CommandHandler('meme', meme_get))
updater.dispatcher.add_handler(CommandHandler('vmeme', vmeme_get))
updater.dispatcher.add_handler(CommandHandler('joke', joke_get))
updater.dispatcher.add_handler(CommandHandler('policy', policy_msg))
updater.dispatcher.add_handler(CommandHandler('tell', teller))
updater.dispatcher.add_handler(CommandHandler('send', sender))
updater.dispatcher.add_handler(CallbackQueryHandler(queryHandler))
updater.start_polling()
updater.idle()    

############################################### HANDLERS ###############################################

