#!/usr/bin/env python3
"""
Enhanced Twitter Content Creator with Real Twitter API Integration
This version demonstrates how to integrate with actual Twitter posting functionality
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

class TwitterBotWithRealPosting:
    def __init__(self):
        """Initialize the Twitter bot with API credentials."""
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
        
        if not self.openai_api_key:
            raise ValueError("OPENAI_API_KEY environment variable is required")
        
        # Enhanced content ideas with more variety and engagement
        self.content_ideas = [
            {"Platform": "Twitter", "Idea": "Share a quick tip about AI and machine learning that beginners can understand"},
            {"Platform": "Twitter", "Idea": "Discuss the latest breakthrough in technology and its potential impact"},
            {"Platform": "Twitter", "Idea": "Motivational message for developers and creators working on their projects"},
            {"Platform": "Twitter", "Idea": "Interesting fact about the history of computing or the internet"},
            {"Platform": "Twitter", "Idea": "Quick productivity hack that can save time in daily work"},
            {"Platform": "Twitter", "Idea": "Thought-provoking question about the future of technology"},
            {"Platform": "Twitter", "Idea": "Behind-the-scenes insight from the tech industry or startup world"},
            {"Platform": "Twitter", "Idea": "Simple explanation of a complex technical concept"},
            {"Platform": "Twitter", "Idea": "Inspirational story about innovation or problem-solving"},
            {"Platform": "Twitter", "Idea": "Trend analysis or prediction about emerging technologies"},
            {"Platform": "Twitter", "Idea": "Personal growth tip related to learning and skill development"},
            {"Platform": "Twitter", "Idea": "Fun fact about programming languages or software development"},
            {"Platform": "Twitter", "Idea": "Career advice for people in tech or aspiring to join tech"},
            {"Platform": "Twitter", "Idea": "Discussion about work-life balance in the digital age"},
            {"Platform": "Twitter", "Idea": "Highlight an underrated tool or resource for creators"}
        ]
    
    def get_content_idea(self) -> Dict[str, str]:
        """Get a random content idea with enhanced variety."""
        idea = random.choice(self.content_ideas)
        logger.info(f"Selected content idea: {idea['Idea']}")
        return idea
    
    def generate_post_with_openai(self, content_idea: Dict[str, str]) -> Optional[str]:
        """Generate an engaging social media post using OpenAI."""
        # Enhanced prompt for better engagement
        prompt = f"""Create an engaging and concise social media post for {content_idea['Platform']} based on this idea: {content_idea['Idea']}. 

Guidelines:
- Keep it under 280 characters
- Make it engaging and conversational
- Include relevant hashtags if appropriate
- Use emojis sparingly but effectively
- Encourage interaction when possible
- Be authentic and valuable to the audience"""
        
        headers = {
            'Authorization': f'Bearer {self.openai_api_key}',
            'Content-Type': 'application/json'
        }
        
        data = {
            'model': 'gpt-4',
            'messages': [
                {
                    'role': 'system',
                    'content': 'You are a social media expert who creates engaging, authentic content that provides value to the audience.'
                },
                {
                    'role': 'user',
                    'content': prompt
                }
            ],
            'max_tokens': 100,
            'temperature': 0.8
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
        """Check if the platform is Twitter."""
        is_twitter = content_idea.get('Platform', '').lower() == 'twitter'
        logger.info(f"Platform check - Is Twitter: {is_twitter}")
        return is_twitter
    
    def post_to_twitter_real(self, tweet_text: str) -> bool:
        """
        Post tweet to Twitter using the Twitter_Tool.
        This would be the actual implementation for real posting.
        
        Note: This is a template - you would need to integrate with the actual Twitter_Tool
        that's available in your environment.
        """
        try:
            # Example of how you would use the Twitter_Tool for real posting:
            # 
            # from twitter_tool import Twitter_Tool
            # twitter_tool = Twitter_Tool()
            # result = twitter_tool.post_tweet(action='post_tweet', text=tweet_text)
            # 
            # if result.get('success'):
            #     tweet_id = result.get('tweet_id')
            #     tweet_url = result.get('tweet_url')
            #     logger.info(f"Successfully posted tweet: {tweet_url}")
            #     self.update_log(tweet_text, "Posted", tweet_id, tweet_url)
            #     return True
            # else:
            #     logger.error(f"Failed to post tweet: {result}")
            #     return False
            
            # For now, we'll simulate the posting
            logger.info(f"REAL TWEET WOULD BE POSTED: {tweet_text}")
            self.update_log(tweet_text, "Would be posted")
            return True
            
        except Exception as e:
            logger.error(f"Failed to post tweet: {e}")
            return False
    
    def post_to_twitter_simulation(self, tweet_text: str) -> bool:
        """
        Simulate posting to Twitter (for testing without actual posting).
        """
        try:
            logger.info(f"SIMULATED TWEET POST: {tweet_text}")
            self.update_log(tweet_text, "Simulated")
            return True
            
        except Exception as e:
            logger.error(f"Failed to simulate tweet post: {e}")
            return False
    
    def update_log(self, tweet_text: str, status: str = "Posted", tweet_id: str = None, tweet_url: str = None):
        """Update activity log with posted tweet information."""
        log_entry = {
            "status": status,
            "text": tweet_text,
            "timestamp": datetime.now().isoformat(),
            "platform": "Twitter",
            "character_count": len(tweet_text)
        }
        
        if tweet_id:
            log_entry["tweet_id"] = tweet_id
        if tweet_url:
            log_entry["tweet_url"] = tweet_url
        
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
    
    def run_workflow(self, use_real_posting: bool = False):
        """
        Execute the complete workflow.
        
        Args:
            use_real_posting: If True, uses real Twitter API. If False, simulates posting.
        """
        logger.info("Starting enhanced Twitter content creation workflow...")
        
        try:
            # Step 1: Get Content Ideas
            content_idea = self.get_content_idea()
            
            # Step 2: Generate Post with OpenAI
            tweet_text = self.generate_post_with_openai(content_idea)
            if not tweet_text:
                logger.error("Failed to generate tweet text")
                return False
            
            # Step 3: Check Platform
            if not self.check_platform(content_idea):
                logger.info("Platform is not Twitter, skipping post")
                return False
            
            # Step 4: Post to Twitter (real or simulated)
            if use_real_posting:
                success = self.post_to_twitter_real(tweet_text)
            else:
                success = self.post_to_twitter_simulation(tweet_text)
            
            if not success:
                logger.error("Failed to post tweet")
                return False
            
            logger.info("Workflow completed successfully!")
            return True
            
        except Exception as e:
            logger.error(f"Workflow failed with error: {e}")
            return False

def main():
    """Main function to run the enhanced Twitter content bot."""
    try:
        # Check environment variables for posting mode
        use_real_posting = os.getenv('USE_REAL_POSTING', 'false').lower() == 'true'
        
        bot = TwitterBotWithRealPosting()
        success = bot.run_workflow(use_real_posting=use_real_posting)
        
        if success:
            mode = "real posting" if use_real_posting else "simulation"
            print(f"✅ Twitter content creation completed successfully! (Mode: {mode})")
        else:
            print("❌ Twitter content creation failed!")
            exit(1)
            
    except Exception as e:
        logger.error(f"Bot initialization failed: {e}")
        print(f"❌ Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()
