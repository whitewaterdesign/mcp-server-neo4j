from typing import LiteralString, List, Dict

from neo4j import GraphDatabase, RoutingControl, Query

from app import mcp
from app.config import get_config


config = get_config()

driver = GraphDatabase.driver(
    config.neo4j_uri,
    auth=(config.neo4j_username, config.neo4j_password)
)


@mcp.tool()
def get_schema():
    """
    Returns the database schema (labels, relationship types, properties, constraints/indexes, and optionally sample counts).

    :return: Schema visualization records
    """
    query: LiteralString = r"CALL db.schema.visualization();"

    return run_cypher_query(query)


@mcp.tool()
def run_cypher_query(query: LiteralString | Query, parameters: Dict[str, str | int | bool] | None = None):
    """
    Executes a Cypher query and returns rows and metadata (and errors if any).

    :param query: LiteralString | Query - Cypher query string or Query object
    :param parameters: Dict[str, str] - Additional parameters for the query
    :return: Any - Query results
    """
    kwargs = parameters or {}

    records, _, _ = driver.execute_query(
        query,
        database_=config.db_name,
        routing_= RoutingControl.READ,
        **kwargs
    )

    return records


# @mcp.tool()
def get_movies_by_actor(actor_name: str) -> List[str]:
    """
    Retrieve movies acted by a specific actor.

    :param actor_name: str - Name of the actor
    :return: List[str] - List of movie titles
    """
    query = Query(r"""
        MATCH (p:Person)-[:ACTED_IN]->(m) 
        WHERE toLower(p.name) CONTAINS toLower($actor_name) 
        RETURN m.title AS title 
        ORDER BY title
    """)
    records = run_cypher_query(query, actor_name=actor_name)
    return [record['title'] for record in records]


if __name__ == "__main__":
    print(run_cypher_query("MATCH (p:Person {name: $name})-[:ACTED_IN]->(m:Movie) RETURN count(DISTINCT m) AS filmCount", name="Tom Hanks"))
    # print(get_movies_by_actor("Tom Hanks"))
    # print(get_schema())
    # print(run_cypher_query(r"""
    #     MATCH (:Person {name: 'Tom Hanks'})-[:ACTED_IN]->(m:Movie)<-[:ACTED_IN]-(coActor:Person)
    #     WHERE coActor.name <> 'Tom Hanks'
    #     RETURN DISTINCT coActor.name AS actor
    #     ORDER BY actor;
    # """))