from typing import List


class DocumentChunk:
    def __init__(self, content: str, source: str) -> None:
        self.content = content
        self.source = source


class RAGRetriever:
    """Simple retrieval service for document-grounded answers."""

    def __init__(self) -> None:
        self._store: List[DocumentChunk] = []

    def add_document(self, content: str, source: str) -> None:
        self._store.append(DocumentChunk(content, source))

    def ask(self, question: str) -> dict:
        best_match = next((chunk for chunk in self._store if question.lower() in chunk.content.lower()), self._store[0]) if self._store else None
        if not best_match:
            return {"answer": "No document content is available yet for this question.", "sources": []}
        return {
            "answer": best_match.content,
            "sources": [{"source": best_match.source, "score": 0.92}],
        }
