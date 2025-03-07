import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout

taxonomy_graph = nx.DiGraph()

# Add Lassie's relationships
taxonomy_graph.add_edge("Animal","Mammal")
taxonomy_graph.add_edge("Mammal","Dog")
taxonomy_graph.add_edge("Mammal","Dolphin")
taxonomy_graph.add_edge("Dolphin","Flipper")
taxonomy_graph.add_edge("Dog", "Collie")
taxonomy_graph.add_edge("Collie","Lassie")
taxonomy_graph.add_edge("Dog", "Mixed-breed")
taxonomy_graph.add_edge("Mixed-breed","Benji")

ontology_graph = nx.DiGraph()
ontology_graph.add_edge( "Lassie","Eric Knight", relationship="created_by")
ontology_graph.add_edge("Lassie","Lassie Come-Home", relationship="character_in")
ontology_graph.add_edge("Lassie", "United States", relationship="country_of_origin")
ontology_graph.add_edge("Benji", "Joe Camp", relationship="created_by")
ontology_graph.add_edge( "Benji","Benji (1974 Film)", relationship="character_in")
ontology_graph.add_edge("Benji",  "United States", relationship="country_of_origin")
ontology_graph.add_edge("Flipper","Arthur Weiss", relationship="created_by")
ontology_graph.add_edge("Flipper","Flipper",relationship="character_in")
ontology_graph.add_edge("Flipper","United States",relationship="country_of_origin")


full_graph = nx.compose(taxonomy_graph, ontology_graph)
# Visualize Lassie's ontology
plt.figure(figsize=(8, 6))
pos = graphviz_layout(full_graph, prog="dot")
nx.draw(full_graph, pos, with_labels=True, node_size=2500, node_color="lightgreen", font_size=10)

edge_labels = {(u, v): d["relationship"]
				for u, v, d in full_graph.edges(data=True) 
				if "relationship" in d}
nx.draw_networkx_edge_labels(full_graph, pos, edge_labels=edge_labels)
plt.show()

dog_decendents = nx.descendants(full_graph,"Animal")
print(dog_decendents)
dog_characters = []
for node in dog_decendents:
	neighbors = full_graph.neighbors(node)
	for neighbor in neighbors:
		if full_graph[node][neighbor].get("relationship", "")== "character_in" and full_graph[node].get("attribures", {}).get("creation_year",0)>1960:
			dog_characters.append(node)
print(dog_characters)