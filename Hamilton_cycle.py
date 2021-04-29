#!/usr/bin/env python
#Simple Code developed by wr4th using backtracking
N=int(input("No of vertices:-\n"))
print("\nEnter the edges connected")
graph=[]  #adjacent graph
for i in range(N):
	graph.append(list(map(int,input().split())))
m=len(graph)
path=[0]*m
path[0]=0   #initial path or starting path
def is_safe(v,pos):
	#check if current vertex and last vertex 
	#in path are adjacent
	if graph[path[pos-1]][v]==0:
		return False
	for vertex in path: #Check if current vertex not already in path
		if vertex==v:
			return False
	return True 

def print_path(path):
	print(path)

def ham_cycle(pos):
	#best case: if all vertices are 
	# included in path
	if pos==m:
		#Last vertex should be adjacent to firrst 
		#vertex in path to make cycle 
		if graph[path[pos-1]][path[0]]==1:
			return True
		return False
	#Try different vertices as a starting point in a path
	for v in range(1,m):
		if is_safe(v,pos)==True:
			path[pos]=v #print current vertex
			if ham_cycle(pos+1):return True #Try for different vertices
			path[pos]=0  # backtrack to lead a solution
	return False
print("Number of Hamilton cycle are:->")
if ham_cycle(1):
	print_path(path)
else:
	print("NO SOLUTION")



