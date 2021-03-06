import random
import copy
import os
from flask import Flask
from flask import render_template
from flask import request
from flask import send_from_directory
import ranzen_assets as ra

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():

    Band = ra.Band
    Artist = ra.Artist
    Member = ra.Member
    Band2 = ra.Band2
    Date = ra.Date
    Inspiration = ra.Inspiration
    Adverb = ra.Adverb
    Song_Title = ra.Song_Title
    Style1 = ra.Style1
    Style2 = ra.Style2
    Adjective = ra.Adjective
    Location = ra.Location
    Country = ra.Country

    Band = copy.deepcopy(Band)
    Artist = copy.deepcopy(Artist)
    Member = copy.deepcopy(Member)
    Band2 = copy.deepcopy(Band2)
    Date = copy.deepcopy(Date)
    Inspiration = copy.deepcopy(Inspiration)
    Adverb = copy.deepcopy(Adverb)
    Song_Title = copy.deepcopy(Song_Title)
    Style1 = copy.deepcopy(Style1)
    Style2 = copy.deepcopy(Style2)
    Adjective = copy.deepcopy(Adjective)
    Location = copy.deepcopy(Location)
    Country = copy.deepcopy(Country)

    random.shuffle(Band)
    My_Band = "{} {} {}".format(Band.pop().title(),Band.pop().title(),Band.pop().title())
    random.shuffle(Band2)
    My_Band2 = "{} {} {}".format(Band.pop(),Band2.pop(),Band.pop()) 

    random.shuffle(Member)
    MyMember = Member.pop()

    random.shuffle(Date)
    MyDate = Date.pop()

    random.shuffle(Style1)
    random.shuffle(Style2)
    MyStyle = "{} {} {}".format(Style1.pop(), Style2.pop(), Style2.pop())
    random.shuffle(Style1)
    random.shuffle(Style2)
    MyStyle2 = "{} {} {}".format(Style1.pop(), Style2.pop(), Style2.pop())
    random.shuffle(Style1)
    random.shuffle(Style2)
    MyStyle3 = Style2.pop()
    random.shuffle(Style2)
    MyStyle4 = Style2.pop()
    random.shuffle(Style2)
    MyStyle5 = Style2.pop()
    random.shuffle(Style2)
    MyStyle6 = "{} {} {}".format(Style1.pop(), Style2.pop(), Style2.pop())
    random.shuffle(Style2)
    MyStyle3 = Style2.pop()
    MyStyle7 = "{} {} {}".format(Style1.pop(), Style2.pop(), Style2.pop())
    random.shuffle(Style2)
    MyStyle3 = Style2.pop()

    random.shuffle(Adverb)
    MyAdverb = Adverb.pop()
    random.shuffle(Adverb)
    MyAdverb2 = Adverb.pop()

    random.shuffle(Inspiration)
    MyInspiration = Inspiration.pop()

    random.shuffle(Adjective)
    MyAdjective = Adjective.pop()
    random.shuffle(Adjective)
    MyAdjective2 = Adjective.pop().title()
    random.shuffle(Adjective)
    MyAdjective3 = Adjective.pop()
    random.shuffle(Adjective)
    MyAdjective4 = Adjective.pop()
    random.shuffle(Adjective)
    MyAdjective5 = Adjective.pop()
    random.shuffle(Adjective)
    MyAdjective6 = Adjective.pop()
    random.shuffle(Adjective)
    MyAdjective7 = Adjective.pop()
    random.shuffle(Adjective)
    MyAdjective8 = Adjective.pop()
    random.shuffle(Adjective)
    MyAdjective9 = Adjective.pop()
    random.shuffle(Adjective)
    MyAdjective10 = Adjective.pop()
    random.shuffle(Adjective)
    MyAdjective11 = Adjective.pop()
    random.shuffle(Adjective)
    MyAdjective12 = Adjective.pop()
    
    random.shuffle(Artist)
    MyArtist = "{} {}".format(Artist.pop(), Artist.pop())

    random.shuffle(Song_Title)
    MySong_Title = "{0} {1}".format(Song_Title.pop(), Song_Title.pop())
    random.shuffle(Song_Title)
    MySong_Title = "{0} {1}".format(MySong_Title, Song_Title.pop())

    random.shuffle(Location)
    MyLocation = Location.pop()

    random.shuffle(Country)
    MyCoutry1 = Country.pop()
    random.shuffle(Country)
    MyCoutry2 = Country.pop()
    random.shuffle(Country)
    MyCoutry3 = Country.pop()
    
    ranzen_title = f"{My_Band}"
    meno_text_1 = f"""
     A "{My_Band2}" nev?? {MyAdjective3} sz??l??projektb??l ismert {MyArtist}
     {MyDate} ind??totta ??tj??ra a {My_Band} nev?? form??ci??t.
     {MyAdjective2} zenei vil??g??val {MyAdverb2} felh??vta mag??ra a figyelmet.
     St??lusa {MyAdjective6} kever??ke a {MyStyle} ??s {MyStyle2} m??fajoknak,
     de {MyAdverb} egy kis {MyAdjective7} {MyStyle3} vagy ??ppen 
     {MyAdjective8} {MyStyle4} is f??szerezi {MyAdjective} zenei alkot??sait."""
     
    meno_text_2 = f"""
     A f??k??nt {MyInspiration} ihlette {MyStyle5} elemek egym??sra hat??s??b??l ??p??tkez??, valamint 
     {MyAdjective4} dalszerkezetekkel ??s {MyAdjective5} elsz??ll??sokkal oper??l?? zen??szre 
     nagy hat??ssal volt a korai {MyStyle6} {MyAdjective10} hangz??svil??ga.      
     Az "{MySong_Title}" c??m?? els?? kislemezdal, illetve a hozz?? k??sz??lt {MyAdjective12} self-made videoklip 
     t??bb {MyLocation} lej??tsz??si list??ban is szerepelt."""
     
    meno_text_3 = f"""
     Az elm??lt ??vekben frissen facsart {MyStyle7} el??adok mellett t??lt??tte meg a 
     {MyAdjective9} klubokat.
     A lemezr??l csupa j??t ??rtak a {MyAdjective11} {MyLocation} oldalak, a sz??mok a mai napig el??fordulnak
     eur??pai ??s tengerent??li webr??di??k playlistjein, az el??ad?? pedig turn??zott 
     {MyCoutry1}, {MyCoutry2} ??s {MyCoutry3}, viszont B??nkon m??g soha nem j??tszott. 
     Most ??jra fog??
    """
    return render_template('index.html', 
    meno_text_1=meno_text_1,
    meno_text_2=meno_text_2,
    meno_text_3=meno_text_3,
    ranzen_title=ranzen_title)
    
if __name__ == "__main__":
	app.run()   
