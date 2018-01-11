# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 20:32:28 2018

@author: DELL
"""

if __name__ == "__main__":
	
	graph, in_deg = {}, {}
	auth_old, auth_new = {}, {}
	hub_old, hub_new = {}, {}
	with open(input("\nNetwork file name : "), "r") as f:
		for i in iter(f):
			l = i.strip("\n").split("\t")
			if l[0] not in graph.keys():
				graph[l[0]] = [l[1]]
			else:
				graph[l[0]].append(l[1])
			if l[1] not in graph.keys():
				graph[l[1]] = []
			if l[1] not in in_deg.keys():
				in_deg[l[1]] = [l[0]]
			else:
				in_deg[l[1]].append(l[0])
			if l[0] not in in_deg.keys():
				in_deg[l[0]] = []
	vertices = list(graph.keys())
	for i in vertices:
		auth_old[i] = hub_old[i] = float(1)
		auth_new[i] = hub_new[i] = float(0)
	k = int(input("\nNumber of iterations : "))
	for i in range(1, k + 1):
		auth_sum = float(0)
		hub_sum = float(0)
		for j in vertices:
			auth_new[j] = float(0)
			for l in in_deg[j]:
				auth_new[j] += hub_old[l]
			auth_sum += auth_new[j]
			hub_new[j] = float(0)
			for l in graph[j]:
				hub_new[j] += auth_old[l]
			hub_sum += hub_new[j]
		for j in vertices:
			auth_new[j] /= auth_sum
			auth_old[j] = auth_new[j]
			hub_new[j] /= hub_sum
			hub_old[j] = hub_new[j]
	with open(input("Authority file : "), "w") as f:
		for i in auth_old.keys():
			f.writelines(str(i) + "\t" + str(auth_old[i]) + "\n")
	with open(input("Hubs file : "), "w") as f:
		for i in hub_old.keys():
			f.writelines(str(i) + "\t" + str(hub_old[i]) + "\n")
