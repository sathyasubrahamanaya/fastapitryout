from fastapi import FastAPI
from prediction import predict_price,get_city_map

app = FastAPI()

@app.get("/api/predict")
def predict(size,total_sqft,bath,balcony,location):
     price =list(predict_price(size,total_sqft,bath,balcony,location))[0]
     return {"message":"Success","Data":{"predicted_price":price},"ErrorCode":0}


@app.get("/api/citylist")
def get_cit_map_api():
    city_map = get_city_map()
    return {"message":"Success","Data":city_map,"ErrorCode":0}