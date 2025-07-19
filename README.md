# Automated Twitter Content Creator

This project automates Twitter content creation based on the n8n workflow `0785_Openai_Twitter_Create.json`. It replicates the workflow functionality using Python and GitHub Actions for daily scheduling.

## Workflow Overview

The original n8n workflow consists of these nodes:
1. **Get Content Ideas** - Retrieves content ideas from Google Sheets
2. **Generate Post with OpenAI** - Uses GPT-4 to create engaging social media posts
3. **Check Platform** - Verifies if the target platform is Twitter
4. **Post to Twitter** - Publishes the generated content to Twitter
5. **Update Google Sheet** - Logs the posted content with timestamp

## Python Implementation

The `automated_twitter_bot.py` script replicates this workflow:

- **Content Ideas**: Uses a predefined pool of content topics (replaces Google Sheets)
- **OpenAI Integration**: Calls GPT-4 API with the same prompt template
- **Platform Check**: Ensures content is targeted for Twitter
- **Twitter Posting**: Posts generated content (currently logs output)
- **Activity Logging**: Maintains JSON log of all posted tweets

## Setup Instructions

### 1. Environment Variables

Set up the following secrets in your GitHub repository:

- `OPENAI_API_KEY`: Your OpenAI API key
- `TWITTER_BEARER_TOKEN`: Your Twitter API Bearer Token

### 2. GitHub Secrets Configuration

1. Go to your repository Settings → Secrets and variables → Actions
2. Add the required secrets:
   - `OPENAI_API_KEY`
   - `TWITTER_BEARER_TOKEN`

### 3. Twitter API Setup

To get Twitter API credentials:
1. Apply for Twitter Developer access at https://developer.twitter.com/
2. Create a new app in the Twitter Developer Portal
3. Generate Bearer Token for API v2 access
4. Add the Bearer Token to GitHub Secrets

### 4. OpenAI API Setup

1. Sign up at https://platform.openai.com/
2. Generate an API key
3. Add the API key to GitHub Secrets

## Scheduling

The GitHub Actions workflow runs daily at 1:00 PM UTC. You can:

- Modify the cron schedule in `.github/workflows/daily_tweet.yml`
- Trigger manually using the "Run workflow" button in GitHub Actions
- Adjust timezone by changing the cron expression

## Content Customization

Edit the `content_ideas` list in `automated_twitter_bot.py` to customize:

- Content topics and themes
- Industry-specific ideas
- Seasonal or trending topics
- Brand-specific messaging

## Monitoring and Logs

The system provides comprehensive logging:

- **Console logs**: Real-time execution status
- **File logs**: Persistent logging in `twitter_bot.log`
- **Tweet history**: JSON log of all posted tweets in `posted_tweets.json`
- **GitHub Actions artifacts**: Downloadable logs for each run

## Original n8n Workflow

This implementation is based on the n8n workflow found at:
`https://github.com/Zie619/n8n-workflows/blob/main/workflows/0785_Openai_Twitter_Create.json`

### Key Features Replicated:

- ✅ OpenAI GPT-4 integration with same prompt template
- ✅ Platform-specific content generation
- ✅ Conditional logic for Twitter posting
- ✅ Activity logging and tracking
- ✅ Error handling and monitoring
- ✅ Daily scheduling automation

## Usage

### Local Testing

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables
export OPENAI_API_KEY="your-openai-key"
export TWITTER_BEARER_TOKEN="your-twitter-token"

# Run the bot
python automated_twitter_bot.py
```

### Production Deployment

1. Push the code to your GitHub repository
2. Configure the required secrets
3. The workflow will run automatically based on the schedule
4. Monitor execution in GitHub Actions tab

## Extending the System

You can enhance this system by:

- Adding actual Twitter API v2 posting functionality
- Integrating with Google Sheets for dynamic content ideas
- Adding image generation and posting
- Implementing engagement tracking
- Adding multiple social media platforms
- Creating a web dashboard for monitoring

## Security Notes

- Never commit API keys to the repository
- Use GitHub Secrets for all sensitive credentials
- Regularly rotate API keys
- Monitor API usage and costs
- Review generated content before posting (if manual approval needed)

## License

This project is open source and available under the MIT License.
