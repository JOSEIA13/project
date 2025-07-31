# import nltk
import nltk

# desde nltk descargar stopwords
from nltk.corpus import stopwords
nltk.download('stopwords')
lista_stopwords = stopwords.words('english')
# lista_stopwords = stopwords.words('spanish')

# imprimir la lista de stopwords
print(lista_stopwords)

