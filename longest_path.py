'''
Created on 18-Apr-2015

@author: meghana m reddy
'''
import build_graph
import time
import sys
longest_paths_dict = {}
predecessor_graph = {}

def topolgical_sort(original_graph):
    '''
    Function takes a graph as a parameter and returns a list of vertices in topologically sorted order.
    Here, original_graph is a graph represented as a hash table, and the list sorted_graph[] is the required list
    '''
    sorted_graph = []
    while original_graph:
        for node, adjacent_edges in original_graph.items():
            for edge in adjacent_edges:
                if edge in original_graph:
                    break
            else:
                del original_graph[node]
                sorted_graph.append(node)
                
    return sorted_graph

def get_predecessor_graph(original_graph):
    to_graph = {}
    for node, adjacent_edges in original_graph.items():
        to_graph[node] =  []
        
    for node, adjacent_edges in original_graph.items():
        for edge in adjacent_edges:
            to_graph[edge].append(node)
            
    return to_graph

def get_longest(to_node):
    if to_node in longest_paths_dict:
        return longest_paths_dict[to_node]

    max_length = 0
    for from_node in predecessor_graph[to_node]:
        max_length = max(max_length, get_longest(from_node) + 1)
        
    longest_paths_dict[to_node] = max_length
    return max_length

def longest_path(original_graph):
    all_nodes = topolgical_sort(original_graph)
    arr = []
    for to_node in all_nodes:
        arr.append(get_longest(to_node))
    
    generate_graph(all_nodes[arr.index(max(arr))])
    print "Max length in given graph is: %d" % max(arr)
    
def generate_graph(to_node):
    word = to_node
    word_list = []
    while predecessor_graph[word] != []:
        l = []
        for t_word in predecessor_graph[word]:
            l.append(longest_paths_dict[t_word])
        max_val = max(l)
        index = l.index(max_val)
        word_list.append(predecessor_graph[word][index])
        word = predecessor_graph[word][index]
        
    word_list.reverse()
    word_list.append(to_node)
    
    for word in word_list:
        print word
    print
        
if __name__ == "__main__":
    tstart = time.clock()
    if len(sys.argv) > 1:
        ip_file = sys.argv[1]
    else:
        ip_file = "testcase4"
    original_graph = build_graph.buildGraph(ip_file)
    copy_graph = dict(original_graph)
    predecessor_graph = get_predecessor_graph(copy_graph)
    longest_path(original_graph)
    tend = time.clock()
    print "Running time: " ,tend - tstart
