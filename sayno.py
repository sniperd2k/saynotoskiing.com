import os
import re

def get_word_dict():
    unsorted_word_dict = {
    "Awesome (strong skill)":"lee high",
    "Awesome! (666)":"leo leo leo",
    "Bad ass":"new bee",
    "Cheers":"gun bay",
    "Chinese":"jong when",
    "Correct":"du way",
    "Do you have any questions?":"knee yo when tea mah",
    "Do you speak Chinese?":"knee way sho jong when mah",
    "Fun":"how wahn",
    "Hello":"knee how",
    "Help":"baong mong",
    "How are you?":"knee how mah",
    "I am called ___":"wah jiao",
    "Is it very fun?":"how wahn mah",
    "Garbage":"la ztee",
    "Goodbye":"zai jian",
    "Knee":"xee guy",
    "Left side":"zuo bian",
    "Look":"kahn",
    "Look up":"tai toe",
    "Me/I":"wah",
    "Not good":"bu how",
    "Need":"she yao",
    "Patience":"neigh xeen",
    "Push":"tway",
    "Right side":"yo bien",
    "Ski":"hwah bahn",
    "Slowly":"man manda",
    "Snow":"sue eh",
    "Snowboard":"dahn bahn",
    "So-So (horse horse tiger tiger)":"mama who who",
    "Sorry":"dwi buh chee",
    "Thank you":"sieh sieh",
    "There":"nah lee",
    "What is your name?":"knee jow shehn mah",
    "You":"knee",
    "You're welcome":"buh kuh chee",
    "Very good":"hen how",     
    "Tired":"late let",
    }

    word_dict = dict(sorted(unsorted_word_dict.items()))
    return word_dict
    
def get_middle_html(word_dict):
    middle_html = ""
    for english, phonetic in word_dict.items():
        file_name = "".join([re.sub("[^A-Za-z0-9]", "", english), ".mp3"]).lower()
        if os.path.isfile("".join(["sounds/", file_name])):
            button_id = file_name + "button"
            middle_html = "".join([middle_html, 
            '''
            <tr>
                <td class="english"><span>''', english, '''</span></td>
                <td class="phonetic" onclick="toggleAudio(\'''',file_name,'''\')">
                    <span class="leftPad">''', phonetic, '''</span>
                    <div class="audio-player">
                        <div class="controls">
                            <audio id="''', file_name, '''" src="./sounds/''', file_name, '''" onended="audioEnded(\'''',button_id,'''\')"></audio>
                            <button id="''',button_id,'''" class="player-button">
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="#3D3132">
                                    <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd" />
                                </svg>
                            </button>
                        </div>
                    </div>
                </td>
            </tr>
            '''])
        else:
            middle_html = "".join([middle_html, 
            '''
            <tr>
                <td class="english"><span>''', english, '''</span></td>
                <td class="phonetic"><span class="leftPad">''', phonetic, '''</span></td>
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

def get_bottom_html():
    bottom_html = """
        </table>
    <hr/>
    <div class="gocenter">
    	<img src="images/grabs.jpg" alt="saynotoskiing" style="max-width:100%;height:auto;">
    </div>
    <hr/>
    
    <div>
        <li style="color:green;">green - never ever</li>
            <ul>
                <li>introduce self and ask names</li>
                <li>introduce board/bindings</li>
                <li>go over stance/bindings</li>
                <li>skating/gliding</li>
                <li>straight glides</li>
                <li>one footed sideslips</li>
                <li>one footed stopping</li>
                <li>one footed j-turns</li>
            </ul>
        <li style="color:green;">green plus - has been introduced to snowboarding</li>
            <ul>
                <li>two footed side slipping to directional change</li>
                <li>garlands progressing to j-turns</li>
                <li>j-turns with traverse, beginning to link</li>
                <li>comfortable on surface lifts</li>
            </ul>
        <li>white - advanced beginner</li>
            <ul>
                <li>single C turns from toe to heel and heel to toe</li>
                <li>basic S turns using crossover movements</li>
                <li><b>up to here for AASI level 1</b></li>
                <li>start playing with flat spins 180s and 360s</li>
                <li>introduce chair lift</li>
                <li>refine turn shape using rotary movements/very turn size and shape</li>
                <li>introduce early edge engagement</li>
                <li>introduce nose press and tail press</li>
            </ul>
        <li style="color:#FFD700;">yellow - beginner/intermediate</li>
            <ul>
                <li>introduce blue terrian/revist twist/maximum extention at edge change</li> 
                <li>introduce carving</li>
                <li>introduce basic switch</li>
                <li>introduce bumps</li>
                <li>introduce ollies/nollies</li>
                <li>introduce park boxes/rails</li>   
            </ul> 
        <li style="color:blue;">blue - advanced intermediate</li>
            <ul>
                <li>introduce maximum flexion at edge change in skidded turns</li>
                <li>introduce maximum flexion at edge change in carved turns</li>
                <li>up unweighting/down unweighting</li>
                <li>introduce fore/aft</li>
                <li>refine switch on green</li>
                <li>refine switch on green</li>                
                <li>introduce glades</li>
                <li>180s nose rolls/tail rolls</li>
                <li>straight airs</li>
            </ul>         
        <li>black - advanced</li>
            <ul>
                <li>introduct black terrain</li>
                <li>refine skidded turn being most flexed at edge change</li>
                <li>refine turns with maximum flexion at edge change</li>
                <li>refine bumps with maximum flexion at edge change</li>
                <li>refine active and passive absorbtion in bumps</li>
                <li>introduce active retraction</li>
                <li>refine switch on blue terrain</li>
                <li>introduce switch with maximum flexion at edge change</li>
                <li>introduce switch carving</li>
                <li>refine glade riding</li>
                <li>practice varying turn radius and rythem on black terrain</li>
                <li>introduce skidded turn with active retraction at edge change</li>
                <li>intorduce turns with active retraction while being most flexed at edge change</li>
                <li>introduce switch riding on black terrain</li>
                <li>introduce turns in bumps with active retraction and maximum flexion at edge change</li>
                <li>refine turns with actve retraction and maximum flexion at edge change</li>
                <li>introduce switch with active retraction and maximum flexion at edge change</li>
                <li>refine switch carving with active retraction</li>
                <li>refine switch bump riding using active retraction</li>    
            </ul>                              
    </div>
    <hr/>
        
    <div>
        <li>Technical</li>
            <ul>        
                <li>Control the relationship of the center of mass to the base of support to direct pressure along the length of the board</li>
                <li>Control the relationship of the center of mass to the base of support to direct pressure along the width of the board</li>
                <li>Control the magnitude of pressure created through the board/surface interaction</li>
                <li>Control the board's pivot through flexion/extension and rotation of the body</li>
                <li>Control the board's tilt through a combination of inclination and angulation</li> 
                <li>Control torsional flex (twist) of the board using flexion/extension and rotation of the body</li>
            </ul>
        <li>People</li>
            <ul>        
                <li>Develop relationships based on trust</li>
                <li>Engage in meaningful two-way communication</li>
                <li>Identify, understand, and manage your emotions and actions</li>
                <li>Recognize and influence the behaviors, motivations, and emotions of others</li>
            </ul>
        <li>Teaching</li>
            <ul>        
                <li>Collaborate on long-term goals and short-term objectives</li>
                <li>Manage information, activities, terrain selection, and pacing</li>
                <li>Promote play, experimentation, and exploration</li>
                <li>Facilitate the learner's ability to reflect upon experiences and sensations</li>
                <li>Adapt to the changing needs of the learner</li>
                <li>Manage emotional and physical risk</li>
            </ul>
        <li>Professional</li> 
            <ul>
                <li>Convey and apply accurate technical information</li>
                <li>Observe, evaluate, and prescribe (through movement analysis)</li>
            </ul>   
    </div>

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
        <link rel="icon" type="image/x-icon" href="images/favicon.ico">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                * {
                    box-sizing: border-box;
                }

                .english { font-size:3vw; } 
                
                .phonetic { font-size:3vw; } 
                
                tr:nth-child(even) { background-color: #f1f1f1; } 
                
                .welcometo1985 { width: 100%; border-spacing: 0; }
                
                div.goright { text-align: right; } 
                
                div.gocenter { text-align: center; } 
                
                .play { vertical-align: middle; margin-bottom: 8px; width: 44px; height: 44px; }
				
				.leftPad { margin-left: 16px; }

                .audio-player { display: inline-block; width: 1em; height: 1em; }

                .controls { display: flex; flex-direction: row; align-items: center; width: 100%; }

                .player-button { background-color: transparent; border: 0; cursor: pointer; padding: 0; width: 3em; height: 3em; }

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
                const playIcon = `
                	          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="#3D3132">
                	      <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd" />
                	    </svg>
                	        `,
                	        pauseIcon = `
                	          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="#3D3132">
                	    <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zM7 8a1 1 0 012 0v4a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v4a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
                	  </svg>
                	        `;
                function toggleAudio (audioId) {
                    var audio = document.getElementById(audioId);
        			var playerButton = document.getElementById(audioId+"button")
                    if (audio.paused) {
                        audio.play();
                        playerButton.innerHTML = pauseIcon;
                    } else {
                        audio.pause();
                        playerButton.innerHTML = playIcon;
                    }
                }
                
                function audioEnded (buttonId) {
                    var playerButton = document.getElementById(buttonId)
                    playerButton.innerHTML = playIcon;
                } 
            </script>
    </head>
    <body>
        <table class="welcometo1985">    
    """
    return top_html

if __name__ == '__main__':
    main()