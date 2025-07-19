#!/usr/bin/env python3
"""
Demo Twitter Content Creator
This demonstrates the workflow without requiring actual API keys
"""

import json
import logging
import random
from datetime import datetime
from typing import Dict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DemoTwitterBot:
    def __init__(self):
        """Initialize the demo Twitter bot."""
        # Content ideas pool (replaces Google Sheets functionality)
        self.content_ideas = [
            {"Platform": "Twitter", "Idea": "Latest trends in artificial intelligence and machine learning"},
            {"Platform": "Twitter", "Idea": "Tips for productivity and time management"},
            {"Platform": "Twitter", "Idea": "Interesting facts about technology and innovation"},
            {"Platform": "Twitter", "Idea": "Motivational quotes for entrepreneurs and creators"},
            {"Platform": "Twitter", "Idea": "Behind-the-scenes insights from the tech industry"}
        ]
    
    def get_content_idea(self) -> Dict[str, str]:
        """Get a random content idea (replaces Google Sheets node)."""
        idea = random.choice(self.content_ideas)
        logger.info(f"✅ Selected content idea: {idea['Idea']}")
        return idea
    
    def generate_post_with_openai_demo(self, content_idea: Dict[str, str]) -> str:
        """Demo version of OpenAI post generation."""
        # Simulate different generated tweets based on the idea
        demo_tweets = {
            "Latest trends in artificial intelligence and machine learning": 
                "🤖 AI is reshaping how we work and live! From GPT models to computer vision, machine learning continues to break new ground. What AI trend excites you most? #AI #MachineLearning #Tech",
            
            "Tips for productivity and time management":
                "⏰ Productivity tip: Try the 2-minute rule - if a task takes less than 2 minutes, do it immediately instead of adding it to your to-do list. Small actions compound into big results! #Productivity #TimeManagement",
            
            "Interesting facts about technology and innovation":
                "💡 Did you know? The first computer bug was an actual bug - a moth trapped in a Harvard computer in 1947! Grace Hopper coined the term when she found it. #TechHistory #Innovation #Programming",
            
            "Motivational quotes for entrepreneurs and creators":
                "🚀 'The way to get started is to quit talking and begin doing.' - Walt Disney. Every great creation started with someone taking that first step. What are you building today? #Motivation #Entrepreneurship",
            
            "Behind-the-scenes insights from the tech industry":
                "🔍 Behind the scenes: Most successful startups pivot at least once. Twitter started as a podcast platform, Instagram was a check-in app. Sometimes the best ideas come from unexpected directions! #Startup #TechInsights"
        }
        
        # Get the demo tweet for this idea, or generate a generic one
        tweet_text = demo_tweets.get(content_idea['Idea'], 
            f"Exploring {content_idea['Idea'].lower()} - always fascinating to see how technology evolves! #Tech #Innovation")
        
        logger.info(f"✅ Generated tweet: {tweet_text}")
        return tweet_text
    
    def check_platform(self, content_idea: Dict[str, str]) -> bool:
        """Check if the platform is Twitter (replicates IF node)."""
        is_twitter = content_idea.get('Platform', '').lower() == 'twitter'
        logger.info(f"✅ Platform check - Is Twitter: {is_twitter}")
        return is_twitter
    
    def post_to_twitter_demo(self, tweet_text: str) -> bool:
        """Demo version of Twitter posting."""
        logger.info(f"✅ DEMO TWEET POSTED: {tweet_text}")
        self.update_log_demo(tweet_text)
        return True
    
    def update_log_demo(self, tweet_text: str):
        """Demo version of activity logging."""
        log_entry = {
            "status": "Demo Posted",
            "text": tweet_text,
            "timestamp": datetime.now().isoformat(),
            "platform": "Twitter",
            "character_count": len(tweet_text)
        }
        
        logger.info(f"✅ Updated log with new tweet entry")
        print(f"\n📝 Log Entry:")
        print(json.dumps(log_entry, indent=2))
    
    def run_workflow_demo(self):
        """Execute the complete demo workflow."""
        print("\n🚀 Starting Twitter Content Creation Workflow Demo...")
        print("=" * 60)
        
        try:
            # Step 1: Get Content Ideas (replaces Google Sheets node)
            print("\n📋 Step 1: Getting Content Ideas")
            content_idea = self.get_content_idea()
            
            # Step 2: Generate Post with OpenAI (demo version)
            print("\n🤖 Step 2: Generating Post with AI")
            tweet_text = self.generate_post_with_openai_demo(content_idea)
            
            # Step 3: Check Platform (replaces IF node)
            print("\n🔍 Step 3: Checking Platform")
            if not self.check_platform(content_idea):
                logger.info("Platform is not Twitter, skipping post")
                return False
            
            # Step 4: Post to Twitter (demo version)
            print("\n📤 Step 4: Posting to Twitter")
            success = self.post_to_twitter_demo(tweet_text)
            
            if success:
                print("\n✅ Workflow completed successfully!")
                print("=" * 60)
                return True
            else:
                print("\n❌ Workflow failed!")
                return False
            
        except Exception as e:
            logger.error(f"Workflow failed with error: {e}")
            return False

def main():
    """Main function to run the demo Twitter content bot."""
    print("🐦 Twitter Content Creator - Demo Mode")
    print("This demonstrates the n8n workflow replication without requiring API keys")
    
    try:
        bot = DemoTwitterBot()
        success = bot.run_workflow_demo()
        
        if success:
            print("\n🎉 Demo completed! This shows how the automated system would work.")
            print("\n📚 Next steps:")
            print("1. Set up OpenAI API key in GitHub Secrets")
            print("2. Configure Twitter API credentials")
            print("3. The system will run automatically daily at 1:00 PM UTC")
        else:
            print("\n❌ Demo failed!")
            
    except Exception as e:
        print(f"❌ Demo error: {e}")

if __name__ == "__main__":
    main()
