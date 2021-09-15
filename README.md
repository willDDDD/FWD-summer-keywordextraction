# FWD-summer-keywordextraction

## See introduction and details in (FWD 2021 SUMMER report.pdf)

## Section 1: Baseline
### Step 1: Extract different topic corpus from arXiv dataset. (cs/math/phy corpus)
download arXiv dataset from https://www.kaggle.com/Cornell-University/arxiv

in Step1_input_corpus.py, extract target domain abstract corpus and store result in step1_result.txt
### Step 2: Using the corpus from Step1 as the input for Autophrases, and get the result, which includes a list of important terms and their important scores.
download Autophrases method from https://github.com/shangjingbo1226/AutoPhrase

add step1_result.txt under AutoPhrase/data/EN/ as the input for Autophrases.

open the file AutoPhrase/auto_phrase.sh, near line 24, change DEFAULT_TRAIN=${DATA_DIR}/EN/DBLP.txt to DEFAULT_TRAIN=${DATA_DIR}/EN/step1_result.txt (name of txt is based on how you name the step1 result)

run (./auto_phrase.sh) in the terminal under Autophrase to get important terms with important score

after running, open AutoPhrase/models/DBLP/AutoPhrase.txt to download the result

### Step 3: Using the list of important terms from Step2 as the input query for Domain-relevance measurement, choosing the certain domain to measure(cs/math/phy) and get the relevance score for each important term.
in Step3_cleanUpStep2Result.py to clean up the result from step2, excluding the terms including symbols. Store result in cleanUpStep2.txt.

in Step3_extractKeyphrases_from_cleanUpStep2Result.py, extract keyphrases from cleanUpStep2.txt, and store result in keyphrasesFromAutophrases.txt. (as the input for domain relevance measure)

download domain relevance measure method from https://github.com/jeffhj/domain-relevance, and follow the instructions in domain-relevance/README.md to download additional resource

copy the content from keyphrasesFromAutophrases.txt, open domain-relevance/query.py, near line 128, paste the content from keyphrasesFromAutophrases.txt into query_terms.

run (python3 query.py --domain cs --method cfl) in the terminal to get the result (here, cs the target domain to measure relevance, you can change to other target domain such as math and phy)

To notice: the output of domain relevance will not be automatically saved to file. You can run (script -f output.txt) before running the previous order to record the output into output.txt. After running, press Ctrl+D to end the recording.

delete extra information in output.txt, only keep keywords and corresponding relevance scores
### Step 4: Mix important scores and relevance scores with different coefficients, and then reorder all the terms based on the new mixing score.
in Step4_joinTwoScore.py, combine important score with relevance score, storing result in joinTwoScore.txt.

in Step4_rankByMixingScore.py, mixing two scores according to different parameters and rank terms based on this new score, storing result in test.txt
### Step 5: Extract terms in different levels (top1000/top5000/1000-2000/…) from the result of step4 and calculate the precision rate based on the keyword list in specific fields (CS/MATH).
in Step5_calculatePrecision.py, calculating precision rate for different rank


## Section 2: result for different situation
different input corpus + different domain for relevance score

CS+CS

Math+Math

Phy+Math

CS+Math

Phy+CS

see section2_result folder

## Section 3: Visualize result in Section 2
see section3_result folder

## Section 4: Relationship between important score and relevance score
see section4 folder

for section4, all files are in html format. Download and open it.
