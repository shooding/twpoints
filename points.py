#coding=utf-8
import networkx as nx
import matplotlib.pyplot as plt
import os, sys

# Create Directed Graph
G=nx.DiGraph()

G.add_nodes_from(["HappyGo","OpenPoint","UUPoint","Ponta","台新","玉山","花旗紅利","花旗現金回饋","花旗哩程","華南",
	"歐付寶","HamiPoint","亞洲萬里通","聯邦銀行","中國信託","LINE","PCHome","長榮","華航","樂天","第一銀行","國泰世華",
	"JAL","ANA","KrisFlyer","彰銀","台北富邦"])

edges = [
	("HappyGo","LINE",float(30)/200),
	("HappyGo","亞洲萬里通",float(100)/250),
	("HappyGo","長榮",float(125)/250),
	("HappyGo","PCHome",float(30)/150),	
	("OpenPoint","HamiPoint",float(25)/7500),
	("OpenPoint","PCHome",float(20)/6000),
	("OpenPoint","亞洲萬里通",float(100)/20000),	
	("OpenPoint","華航",float(100)/20000),	
	("OpenPoint","ANA",float(200)/53000),
	("OpenPoint","長榮",float(200)/45000),
	("華航","OpenPoint",float(90000)/3500),
	("ANA","OpenPoint",float(800000)/10000),
	("ANA","UUPoint",float(7200)/10000),
	("JAL","UUPoint",float(2000)/3000),
	("JAL","Ponta",float(14000)/3000),
	("長榮","OpenPoint",float(60000)/2000),
	("UUPoint","亞洲萬里通",float(100)/250),
	("UUPoint","JAL",float(125)/500),
	("UUPoint","ANA",float(220)/1000),
	("UUPoint","長榮",float(500)/1200),
	("UUPoint","樂天",float(20)/100),
	("UUPoint","歐付寶",float(25)/100),
	("UUPoint","PCHome",float(25)/100),
	("UUPoint","HamiPoint",float(6)/20),
	("UUPoint","LINE",float(25)/110),
	("Ponta","LINE",float(25)/750),
	("Ponta","JAL",float(50)/1000),
	("Ponta","長榮",float(250)/5000),
	("Ponta","歐付寶",float(10)/250),
	("Ponta","HamiPoint",float(30)/750),
	("Ponta","中油",float(400)/100),
	("台新","Ponta",float(1200)/1000),
	("台新","華航",float(10000)/50000),
	("台新","長榮",float(10000)/50000),
	("台新","亞洲萬里通",float(4500)/1000),
	("台新","UUPoint",float(15)/100),
	("台新","OpenPoint",float(8500)/500),
	("玉山","Ponta",float(650)/500),
	("玉山","UUPoint",float(100)/500),
	("玉山","OpenPoint",float(9000)/500),
	("玉山","HappyGo",float(80)/500),
	("玉山","華航",float(1250)/5000),
	("玉山","長榮",float(1500)/5000),
	("玉山","亞洲萬里通",float(2000)/5000),	
	("花旗紅利","亞洲萬里通",float(2000)/6000),
	("花旗紅利","華航",float(2000)/6000),
	("花旗紅利","長榮",float(2000)/6000),
	("花旗紅利","KrisFlyer",float(1000)/3000),
	("花旗紅利","ThaiRoyal",float(1000)/3000),
	("花旗紅利","HappyGo",float(300)/2200),
	("花旗紅利","OpenPoint",float(10000)/700),
	("花旗紅利","Ponta",float(2400)/2000),
	("花旗現金回饋","HappyGo",float(150)/300),
	("花旗現金回饋","Ponta",float(2500)/110),
	("花旗現金回饋","華航",float(1000)/500),	
	("花旗哩程","HappyGo",float(300)/900),
	("花旗哩程","Ponta",float(2800)/1000),
	("花旗哩程","亞洲萬里通",float(500)/500),
	("花旗哩程","華航",float(500)/500),
	("花旗哩程","長榮",float(500)/500),
	("花旗哩程","KrisFlyer",float(500)/500),
	("花旗哩程","ThaiRoyal",float(500)/500),
	("花旗哩程","Etihad",float(500)/500),
	("花旗哩程","Qatar",float(500)/500),
	("花旗哩程","Qantas",float(500)/500),
	("華南","Ponta",float(500)/500),
	("華南","HappyGo",float(120)/1000),
	("華南","OpenPoint",float(7500)/500),
	("歐付寶","亞洲萬里通",float(100)/65),
	("歐付寶","UUPoint",float(125)/45),
	("歐付寶","Ponta",float(250)/10),	
	("HamiPoint","UUPoint",float(20)/6), 
	("HamiPoint","Ponta",float(750)/30),
	("HamiPoint","LINE",float(25)/30),
	("HamiPoint","華航",float(100)/63),
	("HamiPoint","亞洲萬里通",float(100)/72),
	("HamiPoint","OpenPoint",float(7600)/35),
	("樂天","OpenPoint",float(90000)/300),
	("樂天","UUPoint",float(1300)/500),
	("樂天","亞洲萬里通",float(300)/200),
	("樂天","亞洲萬里通",float(300)/200),
	("亞洲萬里通","HamiPoint",float(700)/5000),
	("亞洲萬里通","LINE",float(650)/5000),
	("亞洲萬里通","PCHome",float(650)/5000),
	("亞洲萬里通","樂天",float(700)/5000),
	("亞洲萬里通","OpenPoint",float(168000)/5000),
	("亞洲萬里通","UUPoint",float(2000)/5000),
	("亞洲萬里通","HappyGo",float(1800)/5000),
	("聯邦銀行","HamiPoint",float(50)/1000),
	("聯邦銀行","長榮",float(1000)/10000),
	("聯邦銀行","華航",float(1000)/10000),
	("聯邦銀行","聯航",float(1000)/10000),
	("中國信託","HamiPoint",float(80)/1000),
	("中國信託","長榮",float(1)/6),
	("中國信託","華航",float(1)/6),
	("中國信託","亞洲萬里通",float(1)/3),
	("中國信託","KrisFlyer",float(1)/6),
	("中國信託","Ponta",float(1700)/1000),
	("中國信託","UUPoint",float(250)/1000),
	("中國信託","OpenPoint",float(11000)/500),	
	("中國信託","HappyGo",float(80)/600),	
	("LINE","HamiPoint",float(25)/30),
	("LINE","HappyGo",float(50)/30),
	("LINE","OpenPoint",float(8500)/30),
	("LINE","Ponta",float(600)/30),
	("LINE","UUPoint",float(125)/50),
	("LINE","亞洲萬里通",float(100)/70),
	("PCHome","HappyGo",float(50)/20),
	("PCHome","亞洲萬里通",float(90)/60),
	("PCHome","OpenPoint",float(12000)/40),
	("PCHome","UUPoint",float(125)/45),
	("長榮","HappyGo",float(360)/2000),
	("長榮","UUPoint",float(500)/1500),
	("長榮","Ponta",float(5000)/2000),
	("彰銀","HappyGo",float(10)/100),
	("彰銀","UUPoint",float(12)/100),
	("台北富邦","HappyGo",float(100)/1000),	
	("台北富邦","UUPoint",float(55)/500),	
	("第一銀行","UUPoint",float(75)/500),	
	("第一銀行","華航",float(2000)/15000),	
	("第一銀行","長榮",float(5000)/30000),	
	("國泰世華","OpenPoint",float(9000)/500),	
	("國泰世華","UUPoint",float(80)/500),	
	("國泰世華","華航",float(1000)/7000),	
	("國泰世華","長榮",float(1000)/5000),	
	("國泰世華","亞洲萬里通",float(2000)/8000),	
	("國泰世華","東方航空",float(5000)/10000),	
	("國泰世華","聯航",float(1000)/8500),	
	("國泰世華","Etihad",float(1000)/7500),
	("星展飛行積金","華航",float(1000)/1000),
	("星展飛行積金","長榮",float(1000)/1000),
	("星展飛行積金","亞洲萬里通",float(1000)/1000),
	("星展飛行積金","KrisFlyer",float(1000)/1000),
]

G.add_weighted_edges_from(edges)

cycles = list(nx.simple_cycles(G))

# https://stackoverflow.com/questions/47341773/algorithm-to-multiply-edges-of-a-networkx-graph

for cycle in cycles:
	cycle.append(cycle[0])	

for cycle in cycles:                       			# keep track of each path		    
        pairs = zip(cycle, cycle[1:])                             # get sequence of nodes
        product = 1                                       # reset product for this paths calculation
        for pair in pairs:                                # for each pair of nodes in this path
            an_edge = G.get_edge_data(pair[0], pair[1])   # get this edge's data
            product *= an_edge['weight']                  # multiply all weights
	if product > 0.8:		
		print '{} has product = {}'.format(str(cycle).decode('string_escape'),product)

# Build a graphviz file
f = open("pic.dot", "w")
f.write("digraph G {")
for edge in edges:	
	f.write('{}->{} [label="{}"]\n'.format(edge[0], edge[1], round(edge[2],2)))	
f.write("}")
f.close()

# on Mac: brew install graphviz
os.system("dot pic.dot -T png -o pic.png")
