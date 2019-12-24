#!/usr/bin/env python3
# -*- coding: utf-8 -*
import json
import random
import time
import html

class Wall:
    USERS = 'cgi-bin/cookie/users.json'
    WALL = 'cgi-bin/cookie/wall.json'
    COOKIES = 'cgi-bin/cookie/cookies.json'

    def __init__(self):
        try:
            with open(self.USERS, 'r', encoding='utf-8'):
                pass
        except FileNotFoundError:
            with open(self.USERS, 'w', encoding='utf-8') as f:
                json.dump({}, f)

        try:
            with open(self.WALL, 'r', encoding='utf-8'):
                pass
        except FileNotFoundError:
            with open(self.WALL, 'w', encoding='utf-8') as f:
                json.dump({"posts":[]}, f)


        try:
            with open(self.COOKIES, 'r', encoding='utf-8'):
                pass
        except FileNotFoundError:
            with open(self.COOKIES, 'w', encoding='utf-8') as f:
                json.dump({}, f)

    def register(self, user, password):
        if self.find(user):
            return False
        with open(self.USERS, 'r', encoding='utf-8') as f:
            users = json.load(f)
        users[user] = password
        with open(self.USERS, 'w', encoding='utf-8') as f:
            json.dump(users, f)
        return True

    def set_cookie(self, user):
        with open(self.COOKIES, 'r', encoding='utf-8') as f:
            cookies = json.load(f)
        cookie = str(time.time()) + str(random.randrange(10**14))
        cookies[cookie] = user
        with open(self.COOKIES, 'w', encoding='utf-8') as f:
            json.dump(cookies, f)
        return cookie

    def find_cookie(self, cookie):
        with open(self.COOKIES, 'r', encoding='utf-8') as f:
            cookies = json.load(f)
        return cookies.get(cookie)

    def find(self, user, password=None):
        with open(self.USERS, 'r', encoding='utf-8') as f:
            users = json.load(f)
        if user in users and (password is None or password == users[user]):
            return True
        return False

    def publish(self, user, text):
        with open(self.WALL, 'r', encoding='utf-8') as f:
            wall = json.load(f)
        wall['posts'].append({'user': user, 'text': text})
        with open(self.WALL, 'w', encoding='utf-8') as f:
            json.dump(wall, f)

    def html_list(self):
        with open(self.WALL, 'r', encoding='utf-8') as f:
            wall = json.load(f)
        posts = []
        text = ""
        for post in wall['posts']:
            content = post['user'] + ' : ' + post['text']
            text += '<br>' + content
        return text

    


    
            
