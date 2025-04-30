from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Dict
import joblib
import os
from utils import preprocess_input, generate_recommendations, calculate_emission_metrics

app = FastAPI(title="Carbon Footprint AI",
             description="AI-powered digital carbon footprint estimation")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with actual frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the ML model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model", "model.pkl")

# We'll load the model once it's available
model = None
# try:
#     model = joblib.load(MODEL_PATH)
# except:
#     print("Warning: Model file not found. Predictions will use a simplified calculation.")

class PredictionInput(BaseModel):
    device_type: str
    data_usage: float
    streaming_hours: float
    energy_source: str
    region: str

class PredictionOutput(BaseModel):
    emission_metrics: Dict[str, float]
    recommendations: List[Dict[str, str]]

@app.get("/")
async def root():
    return {"message": "Carbon Footprint AI API is running"}

@app.post("/predict", response_model=PredictionOutput)
async def predict(input_data: PredictionInput):
    try:
        # Preprocess input data
        processed_data = preprocess_input(
            input_data.device_type,
            input_data.data_usage,
            input_data.streaming_hours,
            input_data.energy_source,
            input_data.region
        )

        # If model is available, use it for prediction
        if model is not None:
            emission = float(model.predict(processed_data)[0])
        else:
            # Simplified calculation if model is not available
            emission = (
                processed_data['device_factor'].iloc[0] *
                processed_data['data_usage_gb'].iloc[0] * 0.1 +
                processed_data['streaming_hours'].iloc[0] * 0.2
            ) * processed_data['energy_factor'].iloc[0] * processed_data['region_factor'].iloc[0]

        # Generate recommendations
        recommendations = generate_recommendations(
            input_data.device_type,
            input_data.data_usage,
            input_data.streaming_hours,
            input_data.energy_source,
            emission
        )

        # Calculate additional metrics
        emission_metrics = calculate_emission_metrics(emission)

        return PredictionOutput(
            emission_metrics=emission_metrics,
            recommendations=recommendations
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 