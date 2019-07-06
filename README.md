# Tweet Generator


> [Deployment](https://philosopher-gen.herokuapp.com/)

This project was used to explore data sctructures, specifically dictionaries and hashtables, as well as working on algorithm analysis. After analyzing a large corpus of text, I was able to create a dictionary of dictionaries containing histograms of word frequencies. By randomly sampling words based on frequency, we can create sentences sounding similar to what the original text might sound like, but are actually completely generated. Check out [Markov Chains](https://en.wikipedia.org/wiki/Markov_chain) for more information on the algorithm used. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Install all requirements

```
pip install -r requirements.txt
```

Create .txt file for the corpus you would like to analyze

```
vim buddha.txt
```

### Installing

A step by step series of examples that tell you how to get a development env running

Activate virtual environment

```
source venv/bin/activate
```

Run locally

```
python3 app.py
```

## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used
* [Pip](https://pypi.org/project/pip/) - Dependency Management

## Authors

* **Connor Oswold** - *Initial work* - [Coswold](https://github.com/Coswold)
