# FWD-summer-keywordextraction


## Step 1: Extract different topic corpus from arXiv dataset. (cs/math/phy corpus)
download arXiv dataset from https://www.kaggle.com/Cornell-University/arxiv

In Step1_input_corpus.py, extract target domain abstract corpus.
## Step 2: Using the corpus from Step1 as the input for Autophrases, and get the result, which includes a list of important terms and their important scores.
download Autophrases method from https://github.com/shangjingbo1226/AutoPhrase

Add the result file from Step1_input_corpus.py to AutoPhrase/data/EN/

In AutoPhrase/auto_phrase.sh, near line 24, change DEFAULT_TRAIN=${DATA_DIR}/EN/DBLP.txt to DEFAULT_TRAIN=${DATA_DIR}/EN/step1_result.txt (name of txt is based on how you name the step1 result)

Run ./auto_phrase.sh in the terminal to get important terms with important score

After running, go to AutoPhrase-master/models/DBLP/AutoPhrase.txt to download the result


## Step 3: Using the list of important terms from Step2 as the input query for Domain-relevance measurement, choosing the certain domain to measure(cs/math/phy) and get the relevance score for each important term.
## Step 4: Mix important scores and relevance scores with different coefficients, and then reorder all the terms based on the new mixing score.
## Step 5: Extract terms in different levels (top1000/top5000/1000-2000/…) from the result of step4 and calculate the precision rate based on the keyword list in specific fields (CS/MATH).

