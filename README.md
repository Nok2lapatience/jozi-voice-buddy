# Jozi Voice Buddy

A local voice AI agent you can have a real conversation with — no typing required.

## What it does

Jozi Buddy listens through your laptop microphone and responds through your speakers in real time. It's a friendly Johannesburg-based voice companion that chats casually, helps you think through small decisions, and shares tips about the city. The conversation flows naturally — you can speak while it's talking and it'll pick up your interruption without missing a beat.

## How it works

The agent uses [Strands Bidi Agents](https://strandsagents.com) to maintain a persistent, full-duplex streaming connection with [Amazon Nova Sonic](https://aws.amazon.com/bedrock/nova/) (`amazon.nova-2-5-sonic`) on Amazon Bedrock. Audio goes in from your microphone and comes back out through your speakers with no intermediate speech-to-text step. Echo cancellation is handled automatically via WebRTC so open laptop speakers work fine.

## Prerequisites

- Python 3.12 or later
- [PortAudio](http://www.portaudio.com/) installed on your system (needed by PyAudio)
  - macOS: `brew install portaudio`
  - Ubuntu/Debian: `sudo apt install portaudio19-dev`
  - Windows: install via a pre-built PyAudio wheel or [pipwin](https://pypi.org/project/pipwin/)
- An AWS account with Amazon Bedrock access in `us-east-1`
- Model access enabled for **Amazon Nova Sonic** in the Bedrock console

## Setup

```bash
# 1. Clone the repo
git clone https://github.com/your-username/jozi-voice-buddy.git
cd jozi-voice-buddy

# 2. Create and activate a virtual environment
python -m venv .venv

# macOS / Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure AWS credentials
aws configure
# Enter your Access Key ID, Secret Access Key, region (us-east-1), and output format.
```

### Enable Nova Sonic in Amazon Bedrock

1. Open the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/) and switch to **us-east-1**.
2. Go to **Model access** in the left sidebar.
3. Find **Amazon Nova Sonic** and request access if it isn't already enabled.
4. Wait for the status to show **Access granted** before running the agent.

## Run

```bash
python voice_agent.py
```

Jozi Buddy will print a short message and start listening straight away. Just speak.

## End the chat

Press **Ctrl+C** at any time. The agent will say goodbye and exit cleanly.

## Project Demo





## Make it your own

Open `voice_agent.py` and find the `SYSTEM_PROMPT` string near the top. That's all you need to edit to give your agent a completely different personality, location, or focus area. For example:

```python
SYSTEM_PROMPT = """You are Cape Town Carl, a relaxed and witty voice companion
based in Cape Town, South Africa. You love talking about the ocean, the mountains,
and the best spots for a sundowner. Keep replies to one or two short sentences."""
```

Save the file and run it again — no other changes needed.
