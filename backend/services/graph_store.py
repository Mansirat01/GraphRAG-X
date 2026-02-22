from neo4j import GraphDatabase
import os

class GraphStore:
    def __init__(self):
        self.driver = GraphDatabase.driver(
            os.getenv("NEO4J_URI"),
            auth=(
                os.getenv("NEO4J_USERNAME"),
                os.getenv("NEO4J_PASSWORD")
            )
        )

    def store_document_with_chunks(self, filename, chunks):
        with self.driver.session() as session:
            # Create document node
            session.run(
                """
                MERGE (d:Document {name: $filename})
                """,
                filename=filename
            )

            # Create chunk nodes and relationships
            for i, chunk in enumerate(chunks):
                session.run(
                    """
                    MATCH (d:Document {name: $filename})
                    CREATE (c:Chunk {
                        id: $chunk_id,
                        text: $chunk_text
                    })
                    MERGE (d)-[:HAS_CHUNK]->(c)
                    """,
                    filename=filename,
                    chunk_id=f"{filename}_{i}",
                    chunk_text=chunk
                )