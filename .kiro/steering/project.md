# Jozi Voice Buddy — Project Steering

## What this is
A local voice AI agent that runs on the user's laptop. It uses the microphone and speakers for real-time bidirectional audio conversation.

## Tech stack
- **Framework:** Strands Bidi Agents (bidirectional streaming)
- **Model:** `amazon.nova-2-5-sonic` via Amazon Bedrock, region `us-east-1`
- **Runtime:** Local Python environment (`.venv` present)

## Agent personality
- Name: **Jozi Buddy**
- Tone: Friendly, casual, warm — like a local Johannesburg mate
- Capabilities: General chat + recommendations for things to do in Johannesburg (restaurants, events, neighbourhoods, activities)
- Language: Conversational South African English; light local flavour is welcome but keep it accessible

## Deployment target
GitHub Pages — the final deliverable will be publishable there. Keep web-compatible assets and export-friendly outputs in mind.

## Key decisions to preserve
- Audio I/O is local (microphone + speakers), not browser-based WebRTC
- Model ID and region must not be changed without explicit instruction
- Personality and city focus (Johannesburg) are core — don't generalise away from them
