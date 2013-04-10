server_list = {}
server_allow = [
    'blog.163.com',
    'diandian.com',
    'iteye.com',
    'sinaapp.com',
]
server_filter = []
for x in open('filter_sort.txt').readlines():
    server_filter.append(x[:-1])
def check( x ):
    for y in server_allow:
        if x.find(y) != -1: return False
    for y in server_filter:
        if x.find(y) != -1: return True
    return False

for x in open('server.txt').readlines():
    if check(x): continue
    server = x[:x.find('/',7)]
    server_list[server] = server_list.get(server, 0) + 1
server_list = server_list.items()
server_list.sort(key = lambda d: -d[1])
for x in server_list:
    print x[0]

