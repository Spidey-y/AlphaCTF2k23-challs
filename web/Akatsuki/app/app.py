from flask import Flask,render_template,request,session,render_template_string,abort

application= Flask(__name__)
SECRETKEY="T1M3_h34ls_n0th1ng_1t_just_t34chs_us_h0w_t0_liv3_w1th_p4in"
application.config["SECRET_KEY"]=SECRETKEY
application.config['DEBUG']=True
application.config['ENV'] = 'development'

memberlist=[
"Nagato was a shinobi of Amegakure and descendant of the Uzumaki clan. Forming Akatsuki alongside his friends (and fellow war orphans) Yahiko and Konan, Nagato dreamed of bringing peace to the violent shinobi world. However, following Yahiko's death, Nagato adopted the alias of Pain and, along with Konan, began leading a new Akatsuki — one that would force the world into peace using any means necessary. ",
"Obito Uchiha was a member of Konohagakure's Uchiha clan. He was believed to have died during the Third Shinobi World War, his only surviving legacy being the Sharingan he gave to his teammate, Kakashi Hatake. In truth, Obito was saved from death and trained by Madara, but the events of the war left Obito disillusioned with reality, and he inherited Madara's plan to create an ideal world. Resurfacing under the names of Tobi and Madara Uchiha himself, Obito subtly took control of the Akatsuki, using them as a means to advance his machinations, eventually going public and starting the Fourth Shinobi World War. However, towards the war's conclusion, Obito had a change of heart and, as atonement, sacrificed his life to save the same world he sought to replace",
"Itachi Uchiha was a shinobi of Konohagakure's Uchiha clan who served as an Anbu Captain. He later became an international criminal after murdering his entire clan, sparing only his younger brother, Sasuke. He afterwards joined the international criminal organisation known as Akatsuki, whose activity brought him into frequent conflict with Konoha and its ninja — including Sasuke who sought to avenge their clan by killing Itachi. Following his death, Itachi's motives were revealed to be more complicated than they seemed and that his actions were only ever in the interest of his brother and village, making him remain a loyal shinobi of Konohagakure to the very end",
"Kisame Hoshigaki feared as the Monster of the Hidden Mist, was a shinobi of Kirigakure's Hoshigaki Clan. After joining the Seven Ninja Swordsmen of the Mist, he became an S-rank missing-nin and was partnered with Itachi Uchiha when the latter joined Akatsuki.",
"Deidara was an S-rank missing-nin from Iwagakure. During his time in the village, he was a member of the Explosion Corps. After defecting from the village, he was forced into Akatsuki and was its youngest member. There, Deidara was partnered with Sasori until the latter's death, and later with Tobi before his own death.",
"Sasori renowned as Sasori of the Red Sand, was an S-rank missing-nin from Sunagakure's Puppet Brigade and a member of Akatsuki, where he was partnered with Orochimaru and later Deidara.",
"Kakuzu was an S-rank missing-nin from Takigakure and a member of Akatsuki who was partnered with Hidan.",
"Konan was a kunoichi from Amegakure and a founding member of the original Akatsuki. After Yahiko's death, she was partnered with Nagato, who had since taken control of Akatsuki, and was the only member to call him by his name. After Nagato's death, Konan defected from Akatsuki and became the de facto village head of Amegakure. ",
"Hidan is an S-rank missing-nin who defected from Yugakure and later joined the Akatsuki, and a worshipper of Jashin. There, he was partnered with Kakuzu, despite the two's somewhat mutual dislike of each other. He was also the second newest member of Akatsuki at the time of Tobi's introduction.",
"Black Zetsu is the physical manifestation of Kaguya Ōtsutsuki's will. Having been created to secure its creator's revival, it secretly instigated many events that shaped the shinobi world,[4] during which it posed as Madara Uchiha's manifested will, leading to it being partnered with White Zetsu to become half of the Akatsuki member known simply as Zetsu ",
"White Zetsu was half of the Akatsuki member Zetsu, the other being Black Zetsu. He was one of the first victims of Kaguya Ōtsutsuki's Infinite Tsukuyomi, and was eventually pulled from the Demonic Statue of the Outer Path by Black Zetsu,and infused with the DNA of Hashirama Senju by Madara Uchiha.",
]


@application.route('/',methods=["GET","POST"])
def index():
    try:
        member=request.form.get("member")
        array = request.form.get("array")
        session["user"]="guest"
        if request.method == "GET":
            return render_template('index.html',member_infos=eval("memberlist[0]"))
        elif request.method == "POST":
            if member.isdigit() and array.isalpha():
                member_infos=eval("%s[%s]" % (array,member))
                return render_template('index.html',member_infos=member_infos)
            else:
                abort(400)
    except:
        abort(400)


@application.route('/admin',methods=["GET"])
def admin():
    if session.get('user') == "admin":
        return render_template_string(open("flag.txt").read())
    else:
        abort(403)




if __name__ == "__main__":  
    application.run(host='0.0.0.0', port='8080',debug=True)