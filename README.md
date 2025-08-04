# 🌤️ Weather Tracking Automation

An automated weather data collection system that tracks weather conditions for major Indian cities and logs the data to a GitHub repository using GitHub Actions. This project helps maintain an active contribution graph while collecting valuable weather data.

## 📊 Tracked Cities

The system monitors weather conditions for the following Indian cities:
- **Mumbai** - Financial capital
- **Hyderabad** - IT hub
- **Delhi** - National capital
- **Chennai** - Gateway to South India
- **Kolkata** - Cultural capital

## 🚀 Features

- **Automated Data Collection**: Runs 5 times daily via GitHub Actions
- **Real-time Weather Data**: Fetches current weather using OpenWeatherMap API
- **Structured Data Storage**: Logs data in CSV format with timestamps
- **Contribution Graph Updates**: Creates meaningful commits for GitHub profile
- **Error Handling**: Graceful handling of API failures and network issues
- **Metric Units**: Temperature in Celsius for consistency

## 📋 Data Structure

The weather data is stored in `weather_log.csv` with the following columns:

| Column | Description | Example |
|--------|-------------|---------|
| `timestamp` | Date and time of data collection | `2024-01-15 14:30:00` |
| `city` | City name | `Mumbai` |
| `temperature` | Temperature in Celsius | `28.5` |
| `weather` | Weather condition | `Clouds` |
| `description` | Detailed weather description | `scattered clouds` |

## ⚙️ Setup Instructions

### Prerequisites

1. **OpenWeatherMap API Key**: Get a free API key from [OpenWeatherMap](https://openweathermap.org/api)
2. **GitHub Repository**: This project should be in a GitHub repository

### Installation

1. **Clone or create the repository** with the following files:
   - `log_weather.py` - Main weather logging script
   - `.github/workflows/weather.yml` - GitHub Actions workflow
   - `requirements.txt` - Python dependencies
   - `.gitignore` - Git ignore rules

2. **Get OpenWeatherMap API Key**:
   - Sign up at [OpenWeatherMap](https://openweathermap.org/api)
   - Get your free API key (takes 2-4 hours to activate)
   - Keep your API key secure and never commit it to the repository

3. **Set up GitHub Secrets**:
   - Go to your repository → Settings → Secrets and variables → Actions
   - Add a new repository secret:
     - **Name**: `WEATHER_API_KEY`
     - **Value**: Your OpenWeatherMap API key

4. **Enable GitHub Actions**:
   - The workflow will automatically start running on the scheduled times
   - You can also manually trigger it from the Actions tab

### Manual Testing

To test the script locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variable (replace with your actual API key)
# Windows PowerShell:
$env:WEATHER_API_KEY="your_api_key_here"

# Linux/Mac:
export WEATHER_API_KEY="your_api_key_here"

# Run the script
python log_weather.py
```

## 🕐 Schedule

The automation runs **5 times daily** at the following times (IST):
- **6:00 AM** - Morning weather check
- **10:00 AM** - Mid-morning update
- **2:00 PM** - Afternoon conditions
- **6:00 PM** - Evening weather
- **10:00 PM** - Night conditions

*Note: Times are converted to UTC for GitHub Actions scheduling*

## 📁 Project Structure

```
Weather_Repo/
├── log_weather.py              # Main weather logging script
├── requirements.txt            # Python dependencies
├── .gitignore                 # Git ignore rules
├── README.md                  # This file
├── weather_log.csv            # Generated weather data (auto-created)
└── .github/
    └── workflows/
        └── weather.yml        # GitHub Actions workflow
```

## 🔧 Configuration

### Adding More Cities

To add more cities, edit the `CITIES` list in `log_weather.py`:

```python
CITIES = [
    {"name": "Mumbai", "country": "IN"},
    {"name": "Hyderabad", "country": "IN"},
    {"name": "Delhi", "country": "IN"},
    {"name": "Chennai", "country": "IN"},
    {"name": "Kolkata", "country": "IN"},
    {"name": "Bangalore", "country": "IN"},  # Add new cities here
]
```

### Changing Schedule

To modify the schedule, edit the cron expression in `.github/workflows/weather.yml`:

```yaml
schedule:
  - cron: '30 0,4,8,12,16 * * *'  # Current: 5 times daily
  # Format: minute hour day month day-of-week
```

## 📈 Contribution Graph Impact

This automation creates meaningful commits that:
- Update your GitHub contribution graph
- Show consistent activity patterns
- Demonstrate automated data collection skills
- Provide valuable weather tracking data

## 🔒 Security

- **API Key Protection**: Never commit your API key to the repository
- **Environment Variables**: Use GitHub Secrets for production deployment
- **Local Testing**: Use environment variables for local development
- **Key Rotation**: Regularly update your API keys for security

## 🛠️ Troubleshooting

### Common Issues

1. **API Key Not Set**: Ensure `WEATHER_API_KEY` is properly configured in GitHub Secrets
2. **API Key Not Activated**: New OpenWeatherMap API keys take 2-4 hours to activate
3. **Workflow Not Running**: Check if GitHub Actions are enabled for the repository
4. **No Commits Being Made**: The workflow only commits when there are actual changes to the CSV file
5. **API Rate Limits**: OpenWeatherMap free tier has limits; consider upgrading if needed

### Debugging

- Check the Actions tab in your GitHub repository for workflow logs
- The script provides detailed console output for debugging
- Failed API calls are logged but don't stop the entire process

## 📊 Data Analysis

The collected weather data can be used for:
- Weather pattern analysis
- Temperature trend visualization
- Seasonal weather comparisons
- Data science projects
- API integration examples

## 🤝 Contributing

Feel free to contribute to this project by:
- Adding more cities
- Improving error handling
- Enhancing data visualization
- Adding new weather metrics
- Optimizing the automation schedule

## 🙏 Acknowledgments

- [OpenWeatherMap](https://openweathermap.org/) for providing the weather API
- GitHub Actions for enabling automated workflows
- The open-source community for inspiration and tools

---

**Happy Weather Tracking! 🌤️📊** 