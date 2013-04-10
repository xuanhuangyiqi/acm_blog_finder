#coding: utf-8


INDEX_PATTERNS = [
    ('/archives/', 0),      #wordpress
    ('?p=', 0),             #wordpress
    ('blog.163.com', 12),   #163
    ('/article/details/',0),#csdn
    ('diandian.com', 12),   #diandian
    ('item', 0),            #baidu
]
#all_servers = ['http://collingwoodguy.com/']
all_servers = open('server.txt').readlines()
allow_servers = open('server_allow.txt').readlines()

indexs = {}
for x in all_servers:
    # in allow_servers
    allow = False
    for y in allow_servers:
        if x.find(y[:-1]) != -1: allow = True
    if not allow: continue
    
    index = ''
    # wordpress
    pos = x.find('/archives/')
    if pos != -1:
        index = x[:pos]
    # wordpress
    pos = x.find('?p=')
    if pos != -1:
        index = x[:pos]
    # wordpress
    pos = x.find('?aid=')
    if pos != -1:
        index = x[:pos]
    # 163
    pos = x.find('blog.163.com')
    if pos != -1:
        index = x[:pos+12]
    # CSDN
    pos = x.find('blog.csdn.net')
    if pos != -1:
        index = x[:x.find('/',pos+14)]
    # diandian
    pos = x.find('diandian.com')
    if pos != -1:
        index = x[:pos+12]
    # baidu
    pos = x.find('hi.baidu.com')
    if pos != -1:
        index = x[:x.find('/',pos+13)]
    #cppblog
    pos = x.find('www.cppblog.com')
    if pos != -1:
        end = x.find('/',pos+16)
        if end != -1:
            index = x[:end]   
    #cnblog
    pos = x.find('www.cnblogs.com')
    if pos != -1:
        index = x[:x.find('/',pos+16)]
    #index
    wenhao = x.count('?')
    xiegang = x.count('/')
    if x[-1] == '/': xiegang -= 1
    if wenhao == 0 and xiegang == 2:
        index = x

    if index == '':
        print 'error', x
        #pass
    else:
        indexs[index] = True

'''
for x in indexs:
    print x
print len(indexs)
'''
