import webbrowser, sys

sys.argv # ['mapit.py', '870', 'Valencia', 'St.']

if len(sys.argv) > 1:
    # ['mapit.py', '870', 'Valencia', 'St.'] -> '870 Valencia St.'
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

https://www.google.com/search?q=870+valencia+st+san+francisco+ca+94110&sca_esv=22db317853775bed&rlz=1C1RXQR_enUS1122US1122&sxsrf=ADLYWIK-tP1w8QSl37q4EhfZGftKImRZQw%3A1733545874297&ei=ks9TZ7frEeT_ptQP4LqfkQ8&oq=870+Valencia+St.+san&gs_lp=Egxnd3Mtd2l6LXNlcnAiFDg3MCBWYWxlbmNpYSBTdC4gc2FuKgIIADIGEAAYFhgeMggQABiABBiiBDIIEAAYogQYiQUyCBAAGIAEGKIESL8NUFlY5QZwAXgBkAEAmAFMoAGdAqoBATS4AQHIAQD4AQGYAgWgAqoCwgIKEAAYsAMY1gQYR8ICCxAAGIAEGIYDGIoFmAMAiAYBkAYCkgcBNaAHgws&sclient=gws-wiz-serp
webbrowser.open('https://www.google.com/search?q=870+valencia+st+san+francisco+ca+94110' + address)
    

