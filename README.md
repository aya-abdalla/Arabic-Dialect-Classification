# Arabic-Dialect-Classification
In this Project Two Main Models Have been Used To deffrentiate between Arabic Dislects 


# The Data Fetching :
  Data is fetched 10000 by 1000 line from an API through IDs

# The Data Pre Processing :
 1- clean data from any English char, emoticons, underscore, and repeated charachters 
 2- clean the data from arabic diac like fatHa, Damma, kasra, shaddah, ...
 3- Normalize ALEF WITH MADDA ABOVE, with LETTER ALEF , 
              ALEF WITH MADDA ABOVE, with LETTER ALEF ,
              HAMZA below, with LETTER ALEF 
 4- Normalize  taa' marbuuTa, with haa',
               yaa' with 'alif maqSuura  (at the end of the text)
 5- removing any non arabic unicode
 
 6-eliminate_single_char_words 
 
 
# the  Multinomial Naive Bayes Model , 
The First Model is classical one , it is suitable for Text classification and easy in implementation, in this Classification the model only depends on the words that forms each sentence, it does't take into account the similarity between words


# LSTM model Classification (Deep Learning Model)

to get mush good results , the data is transformed first to word2vec representation so we could
    1-have insights about such words contexts,
    2-know which words are close to each other (the distance between two words) 
    
 The Two Models are implemented and trained in the Model Training Notebook
 You Can also see the results of testing both Models
 
 

 
