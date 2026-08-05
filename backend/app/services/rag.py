from app.rag.retriever import RAGRetriever


class RAGService:
    """Document ingestion and retrieval service placeholder."""

    def __init__(self) -> None:
        self.retriever = RAGRetriever()

    def index_text(self, text: str, source: str) -> dict:
        self.retriever.add_document(text, source)
        return {"status": "indexed", "source": source}

    def answer_question(self, question: str) -> dict:
        return self.retriever.ask(question)
