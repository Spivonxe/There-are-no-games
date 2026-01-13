import splade_base_retrieval
import bm25_search
import splade_finetuned_retrieval

INPUT_CSV = "input_queries.csv"
OUTPUT_CSV = "queries_with_results.csv"
GAME_CSV = "steam_games_cleaned.csv"

BM25_SET_UP=0
SPLADE_LOCAL=0 #0 when running splade model on e.g google colab 1 when running locally
def main():
    if(SPLADE_LOCAL):
        splade_base_retrieval.main(INPUT_CSV, OUTPUT_CSV,GAME_CSV)
        splade_finetuned_retrieval.main(OUTPUT_CSV, OUTPUT_CSV,GAME_CSV)
        if(BM25_SET_UP):
            bm25_search.main(INPUT_CSV, OUTPUT_CSV)
    else:
        if(BM25_SET_UP):
            bm25_search.main(INPUT_CSV, OUTPUT_CSV)
if __name__ == "__main__":
    main()