'''
Created on 18-Apr-2015

@author: meghana m reddy
'''
#import time

def buildGraph(wordFile):
    d = {}
    m = {}
    graph = {}
    wfile = open(wordFile,'r')

    # create buckets of words that differ by one letter
    for line in wfile:
        word = line[:-1].lower()
        graph[line[:-1]] = []

    # Add every work to its corresponding bucket
    for word in graph:    
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
            
            del_word = word[:i] + word[i+1:]
            if del_word in graph:
                m[word] = del_word
    
    # sort the buckets
    for k in d:
        d[k].sort()
        for i in range(0, len(d[k])):
            for j in range(i, len(d[k])):
                if d[k][i]!=d[k][j]:
                    graph[d[k][i]].append(d[k][j])
                    
    # build the graph based on the sorted buckets
    for k in m:
        if(m[k] < k):
            graph[m[k]].append(k)
        else:
            graph[k].append(m[k])
        
    
    return graph

