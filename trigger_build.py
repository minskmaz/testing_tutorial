#!/usr/bin/env python

import requests

base = 'http://localhost:8010'
cred = {'username':'pyflakes', 'passwd':'pyflakes'}
data = {'forcescheduler':'force', 'reason':'force+build'}

s = requests.session()
s.post(base + '/login', data=cred, allow_redirects=False)
s.post(base + '/builders/runtests/force', data=data)


