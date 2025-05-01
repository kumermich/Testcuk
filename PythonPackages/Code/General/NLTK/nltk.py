import nltk 
from nltk.tokenize import word_tokenize  
from nltk.corpus import stopwords  
from nltk.stem import PorterStemmer  

# Download NLTK data (if not already downloaded)  
nltk.download('punkt')  
nltk.download('stopwords') 

# Example text  
text = "NLTK is a powerful package for natural language processing." 

# Tokenization  
tokens = word_tokenize(text)  
print("Tokens:", tokens)  

# Removing stopwords  
stop_words = set(stopwords.words('english'))  
filtered_tokens = [token for token in tokens if token.lower() not in stop_words]  
print("Filtered Tokens:", filtered_tokens)  

# Stemming  
stemmer = PorterStemmer()  
stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]  
print("Stemmed Tokens:", stemmed_tokens)