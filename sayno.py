import json

def main():
    top_html = get_top_html()
    bottom_html = get_bottom_html()
    word_dict = get_word_dict()
    middle_html = get_middle_html(word_dict)
    the_html = "".join([top_html, middle_html, bottom_html])
    print(the_html)
    with open("index.html", "w") as file:
        file.write(the_html)

def get_word_dict():
    unsorted_word_dict = {
    "Awesome (strong skill)":"lee high",
    "Awesome! (666)":'<a href="https://content-prod.drops-files.com/v33/sound/mp3/303a400de01d6209f452b29b2628e1a1d85c63d5.mp3">leo leo leo</a>',
    "Chinese":"jong when",
    "Do you have any questions?":"knee yo when tea ma",
    "Fun":"how wahn",
    "Hello":"knee how",
    "Hello, how are you?":"knee how mah",
    "I am ___":"wah shi",
    "Is it fun?":"how wahn mah",
    "Goodbye":"zai jian",
    "Knee":"xee guy",
    "Left side":"zuo bian",
    "Look":"kahn",
    "Me":"whoa",
    "Not good":"bu how",
    "Patience":"neigh xeen",
    "Right side":"yo bien",
    "Ski":"hwah sooyeh",
    "Slowly":"man manda",
    "Snowboard":"xee-a bahn",
    "Thank you":"sieh sieh",
    "What is your name?":"knee jeeow shehn mah",
    "You":"knee",
    "You're welcome":"buh kuh chee",
    "Very good":"hen how",                                
    }

    word_dict = dict(sorted(unsorted_word_dict.items()))
    return word_dict

def get_middle_html(word_dict):
    middle_html = ""
    for english, phonetic in word_dict.items():
        middle_html = "".join([middle_html, 
        '''
        <tr>
            <td class="english"><span style="font-size:3vw">''', english, '''</span></td>
            <td class="phonetic"><span style="font-size:3vw; margin-left: 16px;">''', phonetic, '''</span></td>
        </tr>
        '''])
    return middle_html        
        

def get_bottom_html():
    bottom_html = """
        </table>
    <hr/>
        <img src="qr_code.png" alt="saynotoskiing" style="max-width:100%;height:auto;">
    <hr/>
    <b>PPC</b>
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

                }

                .phonetic {

                }

                tr:nth-child(even) {
                    background-color: #f1f1f1;
                }

                .welcometo1985 {
                    width: 100%;
                    border-spacing: 0;
                }
            </style>
    </head>
    <body>
        <table class="welcometo1985">    
    """
    return top_html

if __name__ == '__main__':
    main()