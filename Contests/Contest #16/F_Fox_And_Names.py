from collections import *
import sys
from functools import reduce
from itertools import *
from heapq import *
from math import *
from collections import defaultdict
from sys import setrecursionlimit
from threading import stack_size
import threading


dirs4 = [[1, 0], [-1, 0], [0, 1], [0, -1]]
dirs8 = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
def _input(): return sys.stdin.readline().rstrip("\r\n")
def I(): return int(_input())
def II(): return _input()
def III(): return map(int, _input().split())
def IV(): return list(map(int, _input().split()))
def V(): return sorted(list(map(int, _input().split())))
def out(var): sys.stdout.write(str(var) + "\n")
    

def main():
    N = I()
    graph = defaultdict(list)
    array = []
    for _ in range(N):
        array.append(II())
    for i in range(1, N):
        Min = min(len(array[i]), len(array[i - 1]))
        flag = False
        for j in range(Min):
            if array[i][j] != array[i - 1][j]:
                graph[array[i - 1][j]].append(array[i][j])
                flag = True
                break
        if not flag and len(array[i]) < len(array[i-1]):
            print("Impossible") 
            return

    colors = [0]*26
    answer = []

    def dfs(current):
        char = ord(current)-97
        if colors[char] == 2:
            return True

        if colors[char] == 1:
            return False
        
        colors[char] = 1
   
        for node in graph[current]:            
            if not dfs(node):
                return False
            
        answer.append(current)
        colors[char] = 2
        return True
    
    for num in list(graph.keys()):
        if not dfs(num):
            print("Impossible")
            return
    answer.reverse()
    rest = []
    for i in range(97, 123):
        if chr(i) not in answer:
            rest.append(chr(i))
    answer.extend(rest)
    print("".join(answer))


setrecursionlimit(1<<30)
stack_size(1<<27)

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()