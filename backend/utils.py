from typing import List, Dict
import pandas as pd
import numpy as np

# Constants for carbon footprint calculations
ENERGY_FACTORS = {
    "Renewable": 0.1,
    "Non-renewable": 1.0,
    "Mixed": 0.5
}

REGION_FACTORS = {
    "North America": 1.2,
    "Europe": 1.0,
    "Asia": 1.1,
    "South America": 0.9,
    "Africa": 0.8,
    "Oceania": 1.1
}

DEVICE_FACTORS = {
    "Desktop": 1.5,
    "Laptop": 1.0,
    "Smartphone": 0.5,
    "Tablet": 0.7,
    "Smart TV": 1.2
}

def preprocess_input(
    device_type: str,
    data_usage: float,
    streaming_hours: float,
    energy_source: str,
    region: str
) -> pd.DataFrame:
    """
    Preprocess the input data for model prediction.
    """
    data = {
        'device_factor': DEVICE_FACTORS.get(device_type, 1.0),
        'data_usage_gb': data_usage,
        'streaming_hours': streaming_hours,
        'energy_factor': ENERGY_FACTORS.get(energy_source, 1.0),
        'region_factor': REGION_FACTORS.get(region, 1.0)
    }
    return pd.DataFrame([data])

def generate_recommendations(
    device_type: str,
    data_usage: float,
    streaming_hours: float,
    energy_source: str,
    emission: float
) -> List[Dict[str, str]]:
    """
    Generate personalized recommendations based on user input and predicted emissions.
    """
    recommendations = []
    
    # Streaming-related recommendations
    if streaming_hours > 4:
        recommendations.append({
            "category": "Streaming",
            "title": "Reduce streaming time",
            "description": "Consider limiting video streaming to 4 hours per day to reduce emissions.",
            "impact": "High"
        })
        recommendations.append({
            "category": "Streaming",
            "title": "Lower video quality",
            "description": "Use standard definition when high resolution isn't necessary.",
            "impact": "Medium"
        })

    # Data usage recommendations
    if data_usage > 50:
        recommendations.append({
            "category": "Data",
            "title": "Optimize data usage",
            "description": "Compress files before uploading and use offline mode when possible.",
            "impact": "Medium"
        })

    # Energy source recommendations
    if energy_source == "Non-renewable":
        recommendations.append({
            "category": "Energy",
            "title": "Switch to green energy",
            "description": "Consider switching to a renewable energy provider.",
            "impact": "High"
        })

    # Device-specific recommendations
    if device_type == "Desktop":
        recommendations.append({
            "category": "Device",
            "title": "Power settings optimization",
            "description": "Enable sleep mode and power-saving features on your device.",
            "impact": "Medium"
        })

    # General recommendations
    recommendations.append({
        "category": "General",
        "title": "Regular digital cleanup",
        "description": "Delete unnecessary files and emails to reduce storage energy usage.",
        "impact": "Low"
    })

    return recommendations[:5]  # Return top 5 most relevant recommendations

def calculate_emission_metrics(emission: float) -> Dict[str, float]:
    """
    Calculate additional metrics based on the predicted emission.
    """
    return {
        "daily_emission": round(emission, 2),
        "monthly_emission": round(emission * 30, 2),
        "yearly_emission": round(emission * 365, 2),
        "trees_needed": round(emission * 365 / 21, 2)  # One tree absorbs ~21kg CO2 per year
    } 