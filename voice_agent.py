"""Jozi Buddy — a Strands Bidi voice agent powered by Amazon Nova Sonic."""

import asyncio

from strands.bidi.agent import BidiAgent
from strands.bidi.io import AudioIO
from strands.bidi.models import BedrockNovaSonicModel

SYSTEM_PROMPT = """You are Jozi Buddy, a warm and friendly voice companion
based in Johannesburg, South Africa. You chat casually with the user, help
them think through small decisions, and share tips about the city when it
comes up. Keep spoken replies to one or two short sentences — this is a
voice conversation, not an essay. If the user says goodbye, say goodbye
back warmly."""


async def main() -> None:
    model = BedrockNovaSonicModel(
        model_id="amazon.nova-2-5-sonic",
        region="us-east-1",
        voice="tiffany",   # <-- try different voice IDs here
)

    agent = BidiAgent(
        model=model,
        system_prompt=SYSTEM_PROMPT,
    )

    # audio_processor=True enables echo cancellation, noise suppression, and
    # automatic gain control. Essential for laptop speakers; harmless with
    # headphones.
    audio = AudioIO(audio_processor=True)

    print("Jozi Buddy is listening. Start talking — press Ctrl+C to end the chat.\n")

    await agent.run(
        inputs=[audio.input()],
        outputs=[audio.output()],
    )


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nConversation ended. Goodbye!")
