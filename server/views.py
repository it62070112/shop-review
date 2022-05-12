from django.http import HttpResponse
from django.shortcuts import render

import pickle

def classify(text):
    string_returning_field = ''

    # load classifier
    clf_filename = './server/naive_bayes_classifier.pkl'
    nb_clf = pickle.load(open(clf_filename, 'rb'))

    # vectorize the new text
    vec_filename = './server/count_vectorizer.pkl'
    vectorizer = pickle.load(open(vec_filename, 'rb'))

    pred = nb_clf.predict(vectorizer.transform([text]))
    
    string_returning_field += str(pred[0])

    array_of_response = [
        "Thanks for your appreciation so much!",
        "Thanks for your liking on our product",
        "Thanks for your honest response!, we're so sorry that something bother you",
        "We're so sorry that we can't impress you with our products, please contact us with how we can help you further more.",
        "We're so sorry to know this, if you want to return this product please directly contanct us"
    ]

    return array_of_response[5 - int(string_returning_field)]

def say_hello(request):
    if request.POST:
        new_doc = request.POST["msg"]
        return render(request, 'index.html', { 'name': classify(new_doc) })
    return render(request, 'index.html', { 'name': '' })