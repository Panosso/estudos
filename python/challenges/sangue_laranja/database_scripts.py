import sqlite3


def create_database():
    sqlite3.connect('database_name')
    con = sqlite3.connect('sangue_laranja')
    cur = con.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS user
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(200) NOT NULL,
            email VARCHAR(250) NOT NULL,
            company VARCHAR(100)
        )
        ''')
    
    con.commit()

    cur.close()
    con.close()

    con = sqlite3.connect('sangue_laranja')
    cur = con.cursor()

    websites = ['google.com', 'youtube.com', 'facebook.com', 'twitter.com',
                'instagram.com', 'baidu.com', 'wikipedia.org', 'yandex.ru',
                'yahoo.com', 'whatsapp.com', 'amazon.com', 'yahoo.co.jp',
                'live.com', 'netflix.com', 'reddit.com',
                'tiktok.com', 'docomo.ne.jp', 'linkedin.com', 'office.com',
                'samsung.com', 'turbopages.org', 'vk.com', 'weather.com',
                'twitch.tv', 'mail.ru', 'naver.com', 'discord.com',
                'bing.com', 'roblox.com', 'bilibili.com',
                'microsoftonline.com', 'pinterest.com', 'zoom.us', 'qq.com']
   
    for site in websites:
        cur.execute('''
            INSERT INTO websites (website) VALUES ("%s")
        ''' % (site,))

        con.commit()

    cur.close()
    con.close()


def populate_database_user():
    pass
