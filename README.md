# Setup for missing-value-predictions [NA]

-explore missing values in MaxQuant label-free-quantification[http://www.mcponline.org/cgi/pmidlookup?view=long&pmid=24942700] values in proteinGroups.txt output
-predict pooled sample values

```bash
python3 -m pip install flask
flask run
```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```bash
curl -d '{"LFQ intensity 4_TK9_apim1": 21.943673,"LFQ intensity 5_TK9_apim_2": 0.000000,"LFQ intensity 6_TK9_apim_3": 22.097802}' -H "Content-Type: application/json" -X POST http://localhost:5000
```
127.0.0.1 - - [08/Mar/2020 20:35:38] "POST / HTTP/1.1" 200 -
{"NA":"961975.0588898719"}



# Zero to Production

> It is not recommended to deploy your production models as shown here. This is just an end-to-end example to get started quickly.

[Read the complete guide](https://www.curiousily.com/posts/deploy-keras-deep-learning-project-to-production-with-flask/)

This guide shows you how to:

- build a Deep Neural Network that predicts Airbnb prices in NYC (using scikit-learn and Keras)
- build a REST API that predicts prices based on the model (using Flask and gunicorn)
- deploy the model to production on Google App Engine

# Quick start

Requirements:

- Python 3.7
- Google Cloud Engine account
- [Google Cloud SDK](https://cloud.google.com/sdk/install)

Clone this repository:

```bash
git clone git@github.com:curiousily/End-to-End-Machine-Learning-with-Keras.git
cd End-to-End-Machine-Learning-with-Keras
```

Install libraries:

```bash
pip install -r requirements.txt
```

## Start local server

```bash
flask run
```

## Make predictions

```bash
curl -d '{"neighbourhood_group": "Brooklyn", "latitude": 40.64749, "longitude": -73.97237, "room_type": "Private room", "minimum_nights": 1, "number_of_reviews": 9, "calculated_host_listings_count": 6, "availability_365": 365}' -H "Content-Type: application/json" -X POST http://localhost:5000
```

## Deploy to Google App Engine

```bash
gcloud app deploy
```

[Read the complete guide](https://www.curiousily.com/posts/deploy-keras-deep-learning-project-to-production-with-flask/)
