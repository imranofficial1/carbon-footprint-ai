// API Configuration
const API_URL = 'http://localhost:8000';

// DOM Elements
const form = document.getElementById('footprint-form');
const resultsSection = document.getElementById('results');
const loadingSection = document.getElementById('loading');
const errorMessage = document.getElementById('error-message');
const metricsContainer = document.getElementById('metrics-container');
const recommendationsContainer = document.getElementById('recommendations-container');

// Helper Functions
const showLoading = () => {
    loadingSection.classList.add('active');
    resultsSection.classList.remove('active');
    errorMessage.classList.remove('active');
};

const hideLoading = () => {
    loadingSection.classList.remove('active');
};

const showError = (message) => {
    errorMessage.textContent = message;
    errorMessage.classList.add('active');
    hideLoading();
};

const showResults = () => {
    resultsSection.classList.add('active');
    hideLoading();
};

const createMetricCard = (title, value, unit) => {
    return `
        <div class="metric-card">
            <h3>${title}</h3>
            <div class="metric-value">${value} ${unit}</div>
        </div>
    `;
};

const createRecommendationCard = (recommendation) => {
    return `
        <div class="recommendation-card">
            <h3>${recommendation.title}</h3>
            <p>${recommendation.description}</p>
            <span class="impact-badge impact-${recommendation.impact.toLowerCase()}">
                ${recommendation.impact} Impact
            </span>
        </div>
    `;
};

const displayResults = (data) => {
    // Display Metrics
    const metrics = data.emission_metrics;
    const metricsHTML = `
        ${createMetricCard('Daily Carbon Emission', metrics.daily_emission, 'kg CO₂')}
        ${createMetricCard('Monthly Carbon Emission', metrics.monthly_emission, 'kg CO₂')}
        ${createMetricCard('Yearly Carbon Emission', metrics.yearly_emission, 'kg CO₂')}
        ${createMetricCard('Trees Needed', metrics.trees_needed, 'trees/year')}
    `;
    metricsContainer.innerHTML = metricsHTML;

    // Display Recommendations
    const recommendationsHTML = data.recommendations
        .map(recommendation => createRecommendationCard(recommendation))
        .join('');
    recommendationsContainer.innerHTML = recommendationsHTML;

    showResults();
};

// Form Submission Handler
form.addEventListener('submit', async (e) => {
    e.preventDefault();
    showLoading();

    const formData = {
        device_type: form.device_type.value,
        data_usage: parseFloat(form.data_usage.value),
        streaming_hours: parseFloat(form.streaming_hours.value),
        energy_source: form.energy_source.value,
        region: form.region.value
    };

    try {
        const response = await fetch(`${API_URL}/predict`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        });

        if (!response.ok) {
            throw new Error('Failed to get prediction');
        }

        const data = await response.json();
        displayResults(data);
    } catch (error) {
        showError('An error occurred while calculating your carbon footprint. Please try again.');
        console.error('Error:', error);
    }
});

// Form Input Validation
const numericInputs = form.querySelectorAll('input[type="number"]');
numericInputs.forEach(input => {
    input.addEventListener('input', (e) => {
        const value = parseFloat(e.target.value);
        if (value < 0) {
            e.target.value = 0;
        }
    });
}); 