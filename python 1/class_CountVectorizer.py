
class CountVectorizer():
    def __init__(self, lowercase=True):
        self.lowercase = lowercase
        self.corpus = []

    def fit_transform(self, data):
        if self.lowercase:
            self.corpus = [string.lower() for string in data]
        else:
            self.corpus = data

        word_list = self.get_feature_names()
        count_matrix = [[0 for col in range(len(word_list))] for row in range(len(self.corpus))]
        for row in range(len(self.corpus)):
            words_string = self.corpus[row].split()
            for word in words_string:
                col = word_list.index(word)
                count_matrix[row][col] += 1
        return count_matrix

    def get_feature_names(self):
        feature_names = list()
        for string in self.corpus:
            words_string = string.split()
            for word in words_string:
                if word not in feature_names:
                    feature_names.append(word)
        return feature_names



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)

    print(vectorizer.get_feature_names())
    # Out: ['crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro',
    #       'fresh', 'ingredients', 'parmesan', 'to', 'taste']

    print(count_matrix)
    # Out: [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
