from neo4j import GraphDatabase

URI = "neo4j+s://7a4afa70.databases.neo4j.io"
USERNAME = "7a4afa70"
PASSWORD = "b5WkCYRpoSTut9kqRedOtDftiMHldUU9lfhF7NdUB6g"

driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))

def test_connection():
    with driver.session() as session:
        result = session.run("RETURN 'Connection successful' AS message")
        print(result.single()["message"])

if __name__ == "__main__":
    test_connection()