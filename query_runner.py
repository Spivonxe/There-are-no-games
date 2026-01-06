import splade_base_retrieval
import bm25_search
import splade_finetuned_retrieval

INPUT_CSV = "queries.csv"
OUTPUT_CSV = "queries_with_results.csv"
GAME_CSV = "steam_games_cleaned.csv"

BM25_SET_UP=1

def main():
    splade_base_retrieval.main(INPUT_CSV, OUTPUT_CSV,GAME_CSV)
    splade_finetuned_retrieval.main(OUTPUT_CSV, OUTPUT_CSV,GAME_CSV)
    if(BM25_SET_UP == 0):
        bm25_search.main(OUTPUT_CSV, OUTPUT_CSV)

if __name__ == "__main__":
    main()