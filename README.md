# Carbon Footprint AI 🌱

An AI-powered web application to help users estimate and reduce their digital carbon footprint.

## Features 🚀

- Estimate digital carbon footprint based on device usage
- Get personalized recommendations for reduction
- Interactive visualization of impact factors
- Support for multiple device types and regions
- AI-powered predictions using machine learning

## Tech Stack 💻

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: FastAPI
- **ML Model**: Scikit-learn/XGBoost
- **Data Visualization**: Chart.js
- **Model Explainability**: SHAP (optional)

## Project Structure 📁

```
carbon-footprint-ai/
├── backend/
│   ├── model/
│   │   └── model.pkl                 # Trained ML model
│   ├── app.py                        # FastAPI backend
│   └── utils.py                      # Helper functions
├── frontend/
│   ├── index.html                    # Main interface
│   ├── result.html                   # Results page
│   ├── static/
│   │   └── style.css                # Styling
│   └── scripts/
│       └── app.js                    # Frontend logic
├── requirements.txt
├── README.md
└── carbon_emission_model.ipynb       # Model training
```

## Setup Instructions 🛠️

1. Clone the repository:
```bash
git clone https://github.com/yourusername/carbon-footprint-ai.git
cd carbon-footprint-ai
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Start the backend server:
```bash
cd backend
uvicorn app:app --reload
```

5. Open the frontend in your browser:
- Navigate to the `frontend` directory
- Open `index.html` in your web browser

## API Endpoints 🔌

- `POST /predict`: Get carbon footprint estimation
- `GET /recommendations`: Get personalized recommendations
- `GET /shap-plot`: Get SHAP feature importance visualization (optional)

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

## License 📝

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments 🙏

- SHAP library for model explainability
- Scikit-learn for machine learning capabilities
- FastAPI for the backend framework 