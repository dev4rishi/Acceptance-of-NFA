

Q = input("Enter States separated by commas:   ").split(',')
sigma = input("Enter inputs separated by commas:   ").split(',')
final = input("Enter final states separated by commas:   ").split(',')
links = {}
for i in Q:
    name = {}
    for j in sigma:
        print("For {} enter the states when input is {}".format(i,j))
        name[j] = input().split(',')
        print(name)
    links[i] = name

lang = input("Enter the list of input strings:  ").split(',')
flag = 0

def trav(state , lang):
    
    if len(lang) >0 and state != '':
        routes = links[state][lang[0]]
        #print("Routes:", routes)
        for i in routes:
            trav(i,lang[1:])
    if state in final:
        global flag
        flag = 1
        return
    else:
        return

for i in lang:
    trav(Q[0],i)
    
    if(flag == 1):
        print(i, " is Accepted")
    else:
        print(i," is Rejected")


