# Building a Article Recommendation Engine using Word2vec and Stanford's GloVe

## Introduction

In this project, I created a simple yet effective article recommendation engine using Word2vec, a popular word embedding technique, and pre-trained word vectors from Stanford's GloVe project, based on a Wikipedia dataset. By leveraging these powerful tools, we can provide article recommendations based on semantic similarities in content.

## Methodology

1. Obtain pre-trained word vectors: I use the pre-trained word vectors from [Stanford's GloVe project](https://nlp.stanford.edu/projects/glove/) , which were trained on a Wikipedia corpus. These vectors will enable us to represent words in a high-dimensional space, capturing their semantic relationships.

2. Prepare the dataset: For this project, I utilize a collection of [BBC](http://mlg.ucd.ie/datasets/bbc.html) articles. After obtaining the dataset, I processed the text articles and organize them into a convenient table format (list of lists) for further analysis.

3. Compute document centroids: For each article, I calculate its centroid in the high-dimensional word vector space. The centroid is the sum of the word vectors of all words in the article divided by the total number of words. By doing this, we can represent the overall semantic meaning of the article.

4. Measure similarity: To find related articles, I compute the distance between the centroids of different documents. Articles with centroids close to each other in the high-dimensional space are considered semantically related or similar.

5. Build the web server: I develop a web server that displays a list of BBC articles. The server will be accessible at http://localhost:5000 for local testing or the IP address of an Amazon server for deployment.

6. Integrate the recommendation engine: The web server will use the recommendation engine to suggest similar articles based on the user's selection. When a user clicks on an article, the server will display a list of recommended articles with the closest centroids to the selected article. 

## Delivery

An example will look like this:

<img src=figures/articles.png width=200>

Clicking on one of those articles takes you to an article page that shows the text of the article as well as a list of five recommended articles:

<img src=figures/article1.png width=450>
<img src=figures/article2.png width=450>


Main functions of the algorithms are implemented in [doc2vec.py](https://github.com/hxu47/Article-Recommendation-Engine/main/doc2vec.py).

Walkthrough of the functions is in [walkthrough.ipynb](https://github.com/hxu47/Article-Recommendation-Engine/blob/main/walkthrough.ipynb).


## Reference:
[Standalone WSGI Containers](http://flask.pocoo.org/docs/1.0/deploying/wsgi-standalone/)

[Efficient Estimation of Word Representations in Vector Space](http://arxiv.org/pdf/1301.3781.pdf)

[Word similarity and relationships](https://github.com/parrt/msds501/blob/master/projects/wordsim.md)

[GloVe: Global Vectors for Word Representation](https://nlp.stanford.edu/projects/glove/)
