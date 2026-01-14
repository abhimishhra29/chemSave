from __future__ import annotations
from typing_extensions import TypedDict
from langgraph.graph import END, START, StateGraph

class ChemSaveGraph(TypedDict):
    def __init_(self):
        self.graph = StateGraph()

    def build_graph(self):
        #Defined nodes
        self.graph.add_node("OCR Extraction")

        #Defined edges
        self.graph.add_edge(START, "OCR Extraction")
        self.graph.add_edge("OCR Extraction", END)

        return self.graph
        
