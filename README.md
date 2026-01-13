# There-are-no-games
AI ML powered game recommender for AIR Group25

# Setup

Firstly set up a virtual python environment, followed by installing the packages from our requirements.txt file. 

## Preprocessing
If not already using our preprocesssed Dataset (steam_games_cleaned.csv), first download the applications.csv file from kaggle (https://www.kaggle.com/datasets/crainbramp/steam-dataset-2025-multi-modal-gaming-analytics/data) and execute the csv_shortener.py file. 
This will remove unneeded entries and filter the dataset as mentioned in our report.

## Using BM25
To use this project with BM25 first set up and install OpenSearch and set the OPENSEARCH_PASSWORD environment variable. 
After activating OpenSearch it should be running on Port 9200. 
If you have it running on another port change the address in `bm25_search.py` and `index_data.py`. 
To prepare the data for use in OpenSearch, run `index_data.py` at least once.
To test the BM25 retrieval use the query_runner.py script and set the BM25_SET_UP variable to 1, do note that the `query_runner.py` will always run the splade models as well. 
To just test the BM25 retrieval use the `bm25_search.py` file and provide a csv file containing the queries and a csv file for outputs.

## Without BM25
If `BM25_SET_UP` is set to 0 the query_runner will only run the splade models.


## Splade

To run the splade models a hugging face account is required. 
Please set a hugging face token with the  ```hf auth login´´´ command.

### Using provided encodings

Since we ran the models and fine-tuning locally on a RTX 2080 Super we sadly can't provide a google colab jupyter notebook. 
However our encodings will be available from the links section of this readme. 
If using the provided encodings the query_runner.py as well as the `splade_base_retrieval` and `splade_finetuned_retrieval` can be run locally when using atleast a RTX 3060 Ti. 
The retrieval files do also expect to be provided input and output `.csv` files. The query_runner does work with only a single input csv file. 
The code for query_runner with only splade enabled and the splade retrieval files should still work on google colab.

### Generating encodings locally

If generating and the encodings locally and or running the fine-tuning locally we do recommend using atleast a 2080 Super as the encoding step ran out of ram on a PC with 16GB of ram and an 3060Ti. 
First run the encode file, wait for this step to finish, which will also generate files for every 5000 entries. 
To condense these files into one use the `merge_encodings` file, which will combine the small files into one and delete the previously generated encoding files. 
This split was done to save on RAM. 
After the encodings are generated the process is the same as when using the provided encodings.

## Evaluation
To use our queries for manual evaluations set the input file of the query_runner to our csv containing our queries. 
To run the automatic evaluation please use the `steam_model_eval.py` script, as this will generate the metrics of both splade models including MRR, ndcg and recall. 
To calculate some metrics from the manual grading, use one of the `manual_eval_*.csv` files with `calc_eval_metrics_manual.py`.


# Links
dataset
base encoding
fine_tuned encoding
model on huggingface
our queries
