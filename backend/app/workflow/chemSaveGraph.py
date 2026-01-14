from __future__ import annotations
from typing_extensions import TypedDic
from state import State
from langgraph.graph import END, START, StateGraph
from nodes.ocr_node import ocr_node
from agents.ocr_agent import OCRAgent

class ChemSaveGraph:
    def __init_(self):
        self.graph = StateGraph(State)
        
    def build_graph(self):
        #Defined nodes
        self.graph.add_node("OCR Extraction", ocr_node)
        #Defined edges
        self.graph.add_edge(START, "OCR Extraction")
        self.graph.add_edge("OCR Extraction", END)
        
        return self.graph.compile()
        
