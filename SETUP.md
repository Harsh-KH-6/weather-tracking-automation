# 🚀 Quick Setup Guide

## Prerequisites

1. **OpenWeatherMap API Key**: Get a free key from [OpenWeatherMap](https://openweathermap.org/api)
2. **GitHub Account**: To host the repository and use GitHub Actions

## Step-by-Step Setup

### 1. Get Your API Key
- Visit [OpenWeatherMap](https://openweathermap.org/api)
- Sign up for a free account
- Navigate to "API keys" section
- Copy your API key (it looks like: `1234567890abcdef1234567890abcdef`)

### 2. Push to GitHub
```bash
# Initialize git repository (if not already done)
git init

# Add all files
git add .

# Commit the initial setup
git commit -m "Initial weather tracking automation setup"

# Add your GitHub repository as remote
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Push to GitHub
git push -u origin main
```

### 3. Configure GitHub Secrets
1. Go to your GitHub repository
2. Click **Settings** tab
3. Click **Secrets and variables** → **Actions**
4. Click **New repository secret**
5. **Name**: `WEATHER_API_KEY`
6. **Value**: Paste your OpenWeatherMap API key
7. Click **Add secret**

### 4. Test the Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Set your API key as environment variable
export WEATHER_API_KEY="your_actual_api_key_here"

# Run the test script
python test_weather.py

# If test passes, run the main script
python log_weather.py
```

### 5. Verify GitHub Actions
1. Go to your repository's **Actions** tab
2. You should see the "Weather Data Logger" workflow
3. The workflow will run automatically at scheduled times
4. You can also manually trigger it using the "Run workflow" button

## Expected Results

✅ **Immediate**: Test script should pass all checks
✅ **Within minutes**: Manual workflow run should create commits
✅ **Daily**: 5 automated weather updates with meaningful commits
✅ **Ongoing**: Growing weather_log.csv with historical data

## Troubleshooting

### API Key Issues
- Ensure the API key is correctly copied (no extra spaces)
- Check that the secret name is exactly `WEATHER_API_KEY`
- Verify your OpenWeatherMap account is active

### Workflow Not Running
- Check if GitHub Actions are enabled for the repository
- Verify the cron schedule in `.github/workflows/weather.yml`
- Look for any error messages in the Actions tab

### No Commits Being Made
- The workflow only commits when there are actual changes
- Check the workflow logs for any errors
- Verify the CSV file is being updated

## Next Steps

1. **Monitor**: Check the Actions tab to see workflow runs
2. **Customize**: Add more cities or change the schedule
3. **Analyze**: Use the collected data for weather analysis
4. **Share**: Show off your automated weather tracking project!

---

**Need help?** Check the main README.md for detailed documentation. 