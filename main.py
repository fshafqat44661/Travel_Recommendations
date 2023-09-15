from fastapi import FastAPI, HTTPException
import openai
from pydantic import BaseModel
from decouple import config

app = FastAPI()

openai.api_key = config('OPEN_API_SECRET_KEY')


class RecommendationRequest(BaseModel):
    country: str
    season: str


@app.post("/recommendations/")
async def get_recommendations(request: RecommendationRequest):
    country = request.country
    season = request.season
    valid_seasons = ["spring", "summer", "autumn", "winter"]
    if season.lower() not in valid_seasons:
        raise HTTPException(status_code=400, detail="Invalid season")
    prompt = f"Recommend three things to do in {country} during {season}."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that recommends activities."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
        )

        recommendations = response['choices'][0]['message']['content']
        recommendation_list = recommendations.split('\n\n')
        recommendation_list = recommendation_list[:4]
        return {
            "country": country,
            "season": season,
            "recommendations": recommendation_list,
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
