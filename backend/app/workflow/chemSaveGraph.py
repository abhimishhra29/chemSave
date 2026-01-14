from .state import State
from .nodes.ocr_node import ocr_node
from langgraph.graph import END, START, StateGraph
from .nodes.ocr_node import ocr_node
from app.agents.ocr_agent import OCRAgent
from .nodes.search_manufacturer import search_manufacturer_node
from .nodes.search_sds import search_sds_node
from .nodes.validation_node import validate_sds_node

class ChemSaveGraph:

    def __init__(self):
        self.graph = StateGraph(State)
        
    def build_graph(self):
        #Defined nodes
        self.graph.add_node("OCR Extraction", ocr_node)
        self.graph.add_node("Search Manufacturer", search_manufacturer_node)
        self.graph.add_node("Search SDS", search_sds_node)
        self.graph.add_node("Validate SDS", validate_sds_node)

        #Defined edges
        self.graph.add_edge(START, "OCR Extraction")
        self.graph.add_edge("OCR Extraction", "Search Manufacturer")
        self.graph.add_edge("Search Manufacturer", "Search SDS")
        self.graph.add_edge("Search SDS", "Validate SDS")
        self.graph.add_edge("Validate SDS", END)
        
        return self.graph.compile()
        
