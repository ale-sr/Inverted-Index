import os
import json
import errno

input_directory = "dataset\\data_elecciones"
curpath = os.path.abspath(os.curdir)

def gerenate_clean_tweets():
    for filename in os.listdir(input_directory):
        if filename.endswith(".json") : 
            with open(input_directory + '\\' + filename, 'r', encoding='utf-8') as all_tweets:
                all_tweets_dictionary = json.load(all_tweets)
                result = {}
                for tweet in all_tweets_dictionary:
                    result[tweet["id"]] = tweet["text"]
                file = "dataset_clean\\"+filename
                if not os.path.exists(os.path.dirname(file)):
                    try:
                        os.makedirs(os.path.dirname(file))
                    except OSError as exc: # Guard against race condition
                        if exc.errno != errno.EEXIST:
                            raise
                with open(file, "w", encoding='utf-8') as clean_file:
                    clean_file.write(json.dumps(result)) 


    