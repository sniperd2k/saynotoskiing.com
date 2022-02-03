def get_word_dict():
    unsorted_word_dict = {
    "Awesome (strong skill)":"lee high",
    "Awesome! (666)":'<audio id="" src="http://saynotoskiing.com/sounds/six.mp3" />lel lel lel</a>',
    "Bad ass":"new bee",
    "Chinese":"jong when",
    "Correct":'<audio id="" src="http://saynotoskiing.com/sounds/correct.mp3" />du way</a>',
    "Do you have any questions?":"knee yo when tea mah",
    "Do you speak Chinese?":"knee way sho jong when mah",
    "Fun":"how wahn",
    "Hello":"knee how",
    "How are you?":'knee how mah <button class="testButton1"><img src="images/qr_code.png" alt="">Car</button> <input type="button" value="knee how mah" onclick="play()"><audio id="audio" src="http://saynotoskiing.com/sounds/how_are_you.mp3" /></audio>',
    "I am ___":"wah shi",
    "Is it very fun?":"how wahn mah",
    "Goodbye":"zai jian",
    "Knee":"xee guy",
    "Left side":"zuo bian",
    "Look":"kahn",
    "Me":'<audio id="" src="http://saynotoskiing.com/sounds/me.mp3" />wha</a>',
    "Not good":"bu how",
    "Patience":"neigh xeen",
    "Right side":"yo bien",
    "Ski":"hwah sooyeh",
    "Slowly":"man manda",
    "Snow":'<audio id="" src="http://saynotoskiing.com/sounds/snow.mp3" />sue eh</a>',
    "Snowboard":"dahn bahn",
    "Sorry":"dwi buh chee",
    "Thank you":"sieh sieh",
    "What is your name?":"knee jeeow shehn mah",
    "You":"knee",
    "You're welcome":'<audio id="" src="http://saynotoskiing.com/sounds/you_are_welcome.mp3" />buh kuh chee</a>',
    "Very good":"hen how",     
    "Tired":"late let",
    }

    word_dict = dict(sorted(unsorted_word_dict.items()))
    return word_dict
    
def get_better_word_dict():
    unsorted_word_dict = {
        "Awesome (strong skill)": ["lee high", "", ""],
        "Awesome! (666)": ["lel lel lel", "six.mp3", "uniqueId"]
    }
    
def get_better_middle_html(word_dict):
    middle_html = ""
    for english, values in word_dict.items():
        phonetic = values[0]
        mp3 = values[1]
        audioId = values[2]
        
        if mp3 == "" and audioId == "":
            middle_html = "".join([middle_html, 
            '''
            <tr>
                <td class="english"><span>''', english, '''</span></td>
                <td class="phonetic"><span class="leftPad">''', phonetic, '''</span></td>
                </tr>
            '''])
        else:
            middle_html = "".join([middle_html, 
            '''
            <tr>
                <td class="english"><span>''', english, '''</span></td>
                <td class="phonetic" onclick="play(\'''',audioId,'''\')">
                    <span class="leftPad">''', phonetic, ''' <img src="images/play.jpeg" class="play" />
                    <audio id="''',audioId,'''" src="http://saynotoskiing.com/sounds/''',mp3,'''" />
                    </span>
                </td>
            </tr>
            '''])
    return middle_html

def main():
    top_html = get_top_html()
    bottom_html = get_bottom_html()
    word_dict = get_word_dict()
    middle_html = get_middle_html(word_dict)
    the_html = "".join([top_html, middle_html, bottom_html])
    print(the_html)
    with open("index.html", "w") as file:
        file.write(the_html)

def get_middle_html(word_dict):
    middle_html = ""
    for english, phonetic in word_dict.items():
        middle_html = "".join([middle_html, 
        '''
        <tr>
            <td class="english"><span>''', english, '''</span></td>
            <td class="phonetic"><span class="leftPad">''', phonetic, '''</span></td>
        </tr>
        '''])
    return middle_html        
        

def get_bottom_html():
    bottom_html = """
        </table>
    <hr/>
     <div class="gocenter">
        <img src="images/qr_code.png" alt="saynotoskiing" style="max-width:100%;height:auto;">
    </div>
    <hr/>
    <div class="goright">
        <b>PPC</b>
    </div>
    </body>
</html>"""
    return bottom_html

def get_top_html():
    top_html = """
<html>
    <head>
        <title>PPC fun first</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                * {
                    box-sizing: border-box;
                }

                .english {
                    font-size:3vw;
                }

                .phonetic {
                    font-size:3vw;
                }

                tr:nth-child(even) {
                    background-color: #f1f1f1;
                }

                .welcometo1985 {
                    width: 100%;
                    border-spacing: 0;
                }
                div.goright {
                    text-align: right;
                }
                div.gocenter {
                    text-align: center;
                }
				.play {
					vertical-align: middle;
					margin-bottom: 8px;
					width: 44px;
					height: 44px;
				}
				
				.leftPad {
					margin-left: 16px;
				}
            </style>
            <!-- Global site tag (gtag.js) - Google Analytics -->
            <script async src="https://www.googletagmanager.com/gtag/js?id=G-Q2436XH6X2"></script>
            <script>
              window.dataLayer = window.dataLayer || [];
              function gtag(){dataLayer.push(arguments);}
              gtag('js', new Date());

              gtag('config', 'G-Q2436XH6X2');
            </script>
            <script>
              function play(audioId) {
                var audio = document.getElementById(audioId);
                audio.play();
              }
            </script>
    </head>
    <body>
        <table class="welcometo1985">    
    """
    return top_html

if __name__ == '__main__':
    main()