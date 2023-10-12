#############################################PROJET FORTUENEO########################################################
#                            TP_realiser en groupe_cours IA                                                         #
#              Realiser par :                                                                                       #
#                                                                                                                   #
#                                                                                                                   #
#                                                                                                                   #
#                                                                                                                   #
#                                                                                                                #
#####################################################################################################################
import pickle
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

# Charger le modèle
from starlette.middleware.cors import CORSMiddleware

with open('Data_Fortuneo.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

app = FastAPI()

# Activer CORS (Cross-Origin Resource Sharing)
origins = [ "http://localhost:63342", ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# class pour les requettes

class RequestBody(BaseModel):
    campaign: float
    duration: float
    pdays: float
    housing: float
    poutcome: float


# appel et traiteemnt des donnée

@app.post("/fit")  # local : http://127.0.0.1:8000 /fit
def fit_model():
    return {"message": "Modèle ajusté avec succès!"}


@app.post("/predict")  # local : http://127.0.0.1:8000 /predict
def predict(data: RequestBody):
    try:
        dataframe = pd.DataFrame(
            {"campaign": [data.campaign],
             "duration": [data.duration],
             "pdays": [data.pdays],
             "housing": [data.housing],
             "poutcome": [data.poutcome]}
        )

        prediction = model.predict(dataframe)

        return {"predictions": prediction.tolist()}
    except Exception as e:
        return {"error": str(e)}


@app.post("/record")  # local : http://127.0.0.1:8000 /record
def record_data():
    """
    conn = create_connection('Fortuneo.db')
    create_table(conn)
    insert_data(conn, data)
    conn.close()

    create_table(conn)
    insert_data(conn, data)
    conn

    create_table(conn)
    insert_data

    create_table

    """

    return {"message": "Données enregistrées avec succès!"}
