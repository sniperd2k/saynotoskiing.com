import os
import re

def get_word_dict():
    unsorted_word_dict = {
    "Awesome (strong skill)":"lee high",
    "Awesome! (666)":"lel lel lel",
    "Bad ass":"new bee",
    "Chinese":"jong when",
    "Correct":"du way",
    "Do you have any questions?":"knee yo when tea mah",
    "Do you speak Chinese?":"knee way sho jong when mah",
    "Fun":"how wahn",
    "Hello":"knee how",
    "How are you?":"knee how mah",
    "I am ___":"wah shi",
    "Is it very fun?":"how wahn mah",
    "Goodbye":"zai jian",
    "Knee":"xee guy",
    "Left side":"zuo bian",
    "Look":"kahn",
    "Me":"wha",
    "Not good":"bu how",
    "Patience":"neigh xeen",
    "Right side":"yo bien",
    "Ski":"hwah sooyeh",
    "Slowly":"man manda",
    "Snow":"sue eh",
    "Snowboard":"dahn bahn",
    "Sorry":"dwi buh chee",
    "Thank you":"sieh sieh",
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