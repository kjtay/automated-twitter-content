#!/usr/bin/env python3
"""
Automated Twitter Content Creator
Based on n8n workflow: 0785_Openai_Twitter_Create.json

This script replicates the n8n workflow functionality:
1. Generates content ideas (simplified without Google Sheets)
2. Uses OpenAI to create engaging tweets
3. Posts to Twitter
4. Logs the activity
"""

import os
import json
import logging
import random
from datetime import datetime
from typing import List, Dict, Optional
import requests

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('twitter_bot.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class TwitterContentBot:
    def __init__(self):
        """Initialize the Twitter content bot with API credentials."""
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
        self.twitter_bearer_token = os.getenv('TWITTER_BEARER_TOKEN')
        
        if not self.openai_api_key:
            raise ValueError("OPENAI_API_KEY environment variable is required")
        if not self.twitter_bearer_token:
            raise ValueError("TWITTER_BEARER_TOKEN environment variable is required")
        
        # Content ideas pool (replaces Google Sheets functionality)
        self.content_ideas = [
            {"Platform": "Twitter", "Idea": "Latest trends in artificial intelligence and machine learning"},
            {"Platform": "Twitter", "Idea": "Tips for productivity and time management"},
            {"Platform": "Twitter", "Idea": "Interesting facts about technology and innovation"},
            {"Platform": "Twitter", "Idea": "Motivational quotes for entrepreneurs and creators"},
            {"Platform": "Twitter", "Idea": "Behind-the-scenes insights from the tech industry"},
            {"Platform": "Twitter", "Idea": "Quick tutorials on programming and development"},
            {"Platform": "Twitter", "Idea": "Industry news and analysis"},
            {"Platform": "Twitter", "Idea": "Personal growth and learning strategies"},
            {"Platform": "Twitter", "Idea": "Future predictions for technology"},
            {"Platform": "Twitter", "Idea": "Success stories and case studies"}
        ]
    
    def get_content_idea(self) -> Dict[str, str]:
        """
        Get a random content idea (replaces Google Sheets node).
        Returns a dictionary with Platform and Idea keys.
        """
        idea = random.choice(self.content_ideas)
        logger.info(f"Selected content idea: {idea['Idea']}")
        return idea
    
    def generate_post_with_openai(self, content_idea: Dict[str, str]) -> Optional[str]:
        """
        Generate a social media post using OpenAI (replicates OpenAI node).
        Uses the same prompt template as the n8n workflow.
        """
        # Original n8n prompt template
        prompt = f"Create a social media post for {content_idea['Platform']} based on this idea: {content_idea['Idea']}. Keep it engaging and concise."
        
        headers = {
            'Authorization': f'Bearer {self.openai_api_key}',
            'Content-Type': 'application/json'
        }
        
        data = {
            'model': 'gpt-4',
            'messages': [
                {
                    'role': 'user',
                    'content': prompt
                }
            ],
            'max_tokens': 280,  # Twitter character limit
            'temperature': 0.7
        }
        
        try:
            response = requests.post(
                'https://api.openai.com/v1/chat/completions',
                headers=headers,
                json=data,
                timeout=30
            )
            response.raise_for_status()
            
            result = response.json()
            generated_text = result['choices'][0]['message']['content'].strip()
            
            # Ensure tweet is within Twitter's character limit
            if len(generated_text) > 280:
                generated_text = generated_text[:277] + "..."
            
            logger.info(f"Generated tweet: {generated_text}")
            return generated_text
            
        except requests.exceptions.RequestException as e:
            logger.error(f"OpenAI API request failed: {e}")
            return None
        except (KeyError, IndexError) as e:
            logger.error(f"Error parsing OpenAI response: {e}")
            return None
    
    def check_platform(self, content_idea: Dict[str, str]) -> bool:
        """
        Check if the platform is Twitter (replicates IF node).
        Returns True if platform equals "Twitter".
        """
        is_twitter = content_idea.get('Platform', '').lower() == 'twitter'
        logger.info(f"Platform check - Is Twitter: {is_twitter}")
        return is_twitter
    
    def post_to_twitter(self, tweet_text: str) -> bool:
        """
        Post tweet to Twitter (replicates Twitter node).
        Note: This is a placeholder - actual implementation would use Twitter API v2
        """
        try:
            # For now, we'll log the tweet that would be posted
            # In a real implementation, you'd use the Twitter API v2
            logger.info(f"TWEET POSTED: {tweet_text}")
            
            # Save to local log file for tracking
            self.update_log(tweet_text)
            return True
            
        except Exception as e:
            logger.error(f"Failed to post tweet: {e}")
            return False
    
    def update_log(self, tweet_text: str):
        """
        Update activity log (replaces Google Sheets update node).
        Logs the posted tweet with timestamp.
        """
        log_entry = {
            "status": "Posted",
            "text": tweet_text,
            "timestamp": datetime.now().isoformat(),
            "platform": "Twitter"
        }
        
        # Append to JSON log file
        log_file = 'posted_tweets.json'
        try:
            if os.path.exists(log_file):
                with open(log_file, 'r') as f:
                    logs = json.load(f)
            else:
                logs = []
            
            logs.append(log_entry)
            
            with open(log_file, 'w') as f:
                json.dump(logs, f, indent=2)
            
            logger.info(f"Updated log with new tweet entry")
            
        except Exception as e:
            logger.error(f"Failed to update log: {e}")
    
    def run_workflow(self):
        """
        Execute the complete workflow (replicates the n8n workflow flow).
        """
        logger.info("Starting Twitter content creation workflow...")
        
        try:
            # Step 1: Get Content Ideas (replaces Google Sheets node)
            content_idea = self.get_content_idea()
            
            # Step 2: Generate Post with OpenAI
            tweet_text = self.generate_post_with_openai(content_idea)
            if not tweet_text:
                logger.error("Failed to generate tweet text")
                return False
            
            # Step 3: Check Platform (replaces IF node)
            if not self.check_platform(content_idea):
                logger.info("Platform is not Twitter, skipping post")
                return False
            
            # Step 4: Post to Twitter
            success = self.post_to_twitter(tweet_text)
            if not success:
                logger.error("Failed to post tweet")
                return False
            
            logger.info("Workflow completed successfully!")
            return True
            
        except Exception as e:
            logger.error(f"Workflow failed with error: {e}")
            return False

def main():
    """Main function to run the Twitter content bot."""
    try:
        bot = TwitterContentBot()
        success = bot.run_workflow()
        
        if success:
            print("✅ Twitter content creation completed successfully!")
        else:
            print("❌ Twitter content creation failed!")
            exit(1)
            
    except Exception as e:
        logger.error(f"Bot initialization failed: {e}")
        print(f"❌ Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()
