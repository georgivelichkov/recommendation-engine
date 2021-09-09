import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics.pairwise import cosine_similarity

bookDF = pd.read_csv('data/books.csv')
bookDF = bookDF.drop(['small_image_url', 'title', 'best_book_id', 'isbn', 'isbn13'], axis=1)
ratingsDF = pd.read_csv('data/ratings.csv')

listOfDictionaries = []
indexMap = {}
reverseIndexMap = {}
ptr = 0
testdf = ratingsDF
testdf = testdf[['user_id', 'rating']].groupby(testdf['book_id'])
for groupKey in testdf.groups.keys():
    tempDict = {}

    groupDF = testdf.get_group(groupKey)
    for i in range(0, len(groupDF)):
        tempDict[groupDF.iloc[i, 0]] = groupDF.iloc[i, 1]
    indexMap[ptr] = groupKey
    reverseIndexMap[groupKey] = ptr
    ptr = ptr + 1
    listOfDictionaries.append(tempDict)

dictVectorizer = DictVectorizer(sparse=True)
vector = dictVectorizer.fit_transform(listOfDictionaries)
pairwiseSimilarity = cosine_similarity(vector)


def print_book_details(book_id):
    print("Title:", bookDF[bookDF['id'] == book_id]['original_title'].values[0])
    print("Author:", bookDF[bookDF['id'] == book_id]['authors'].values[0])
    print("Printing Book-ID:", book_id)
    print("=================++++++++++++++=========================")


def get_book_id_by_title(book_title):
    return bookDF[bookDF['original_title'] == book_title]['id'].values[0]


def get_book_by_id(book_id):
    return bookDF[bookDF['id'] == book_id]


def recommend_books(title):
    books = pd.DataFrame(columns=['title', 'year'])
    book_id = get_book_id_by_title(title)
    row = reverseIndexMap[book_id]
    print("------INPUT BOOK--------")
    print_book_details(book_id)
    print("-------RECOMMENDATIONS----------")
    for i in np.argsort(pairwiseSimilarity[row])[-7:-2][::-1]:
        book = get_book_by_id(indexMap[i])
        return_df = pd.DataFrame(columns=['title', 'year', 'image_url'])
        return_df['title'] = book["original_title"]
        return_df['year'] = book["original_publication_year"]
        return_df['image_url'] = book["image_url"]
        books = books.append(return_df)

    return books
