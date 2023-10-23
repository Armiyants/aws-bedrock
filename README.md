# 🚀 Bedrock Buddy: Your Playful Guide to Amazon Bedrock & AWS Lambda!

Hello friend! 🌍 
Here I've set up a playground for you to explore Amazon Bedrock with AWS Lambda. 
Amazon Bedrock is a fully managed service that provides access to FMs from third-party providers and Amazon; available via an API. With Bedrock, you can choose from a variety of models to find the one that’s best suited for your use case.

My example app discovers cool things like career paths for history students. If you like experimenting new things and especially generative AI You're in the right place!

## 🎈 What's Bedrock Buddy All About?
My little project is a stepping stone for you to get inspired, play around, and create something amazing of your own!

## Getting Started

### Prerequisites
- MAKE SURE YOU REQUESTED AND WAS GIVEN MODEL ACCESS IN AWS BEDROCK CONSOLE ! 
- AWS CLI set up with Admin powers.
- AWS SAM CLI ready to go (Make sure it's v1.94.0 or newer! Use `sam --version`).
- Python 3.9 installed.

### How to Deploy

**First Time Setup**:
```
sam build
sam deploy -g
```

If asked about functions without authorization, give a thumbs up with (y)es. Just remember: this will make those functions open to everyone, so keep it live only as long as you're playing around.

For Future Updates:

```
sam build && sam deploy
```

To test:

```
aws lambda invoke --region us-east-1 --function-name <function-name> --cli-binary-format raw-in-base64-out --payload file://event.json response.json
```

To delete the app:

```
sam delete
```


