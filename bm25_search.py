from opensearchpy import OpenSearch, helpers
import os
from dotenv import load_dotenv
import pandas as pd 

# ----------------------------
# Opensearch
# ----------------------------

host = 'localhost'
port = 9200
INDEX_NAME = "steam_bm25"
NUM_RESULTS_PER_GAME=5
# Create the osearch with SSL/TLS enabled, but hostname verification disabled.


load_dotenv()
PASSWORD = os.getenv("OPENSEARCH_PASSWORD")
osearch = OpenSearch(
    hosts = [{'host': host, 'port': port}],
    http_compress = True, # enables gzip compression for request bodies
    http_auth = ('admin',PASSWORD),
    use_ssl = True,
    verify_certs = False,
    ssl_assert_hostname = False,
    ssl_show_warn = False,
)

def bm25_search(query, size=10):
    response = osearch.search(
        index=INDEX_NAME,
        size=size,
        body={
        "query": {
            "match": {
                "text": query
            }
        }
    }
    )

    results = []
    for hit in response["hits"]["hits"]:
        src = hit["_source"]
        results.append({
            "appid": src["appid"],
            "name": src["name"],
            "score": hit["_score"]
        })

    return results

#print("\nSample query:")
#results = bm25_search("underwater base builder")

# for r in results:
#     print(f"{r['name']} (appid={r['appid']}, score={r['score']:.2f})")

def main(input_csv, output_csv):
    queries = pd.read_csv(output_csv)
    results = []
    for query in queries['query']:
        top_games = bm25_search(query, size=NUM_RESULTS_PER_GAME)
        
        results.append(", ".join([game['name'] for game in top_games]))

    queries['results_bm25'] = results
    queries.to_csv(output_csv, index=False)

if __name__ == "__main__":
    main()