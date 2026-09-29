from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv

load_dotenv()


def build_agent():
    return Agent(
        model=Groq(
            id="openai/gpt-oss-120b"
        ),
        tools=[
            DuckDuckGoTools()
        ],
        markdown=True,
        instructions="""
        You are a helpful and intelligent personal assistant.

        Write your responses in normal paragraphs, similar to how a human
        assistant would respond.

        Formatting rules:
        Use plain text only.
        Do not use Markdown.
        Do not use asterisks.
        Do not use hashtags.
        Do not use Markdown tables.
        Do not use bullet points.
        Do not use numbered lists unless the user specifically asks for a list.
        Do not use unnecessary emojis.
        Do not use unnecessary special characters.
        Do not add headings unless the user asks for them.
        Do not add excessive blank lines.
        Organize longer answers into short, readable paragraphs.
        Keep the response natural and conversational.

        Use DuckDuckGo web search when the user asks for:
        - current information
        - latest news
        - travel information
        - current prices
        - weather
        - recent events
        - information that may have changed recently

        For general questions, answer directly using your knowledge.

        Do not make up information when current information
        requires web search.
        """,
        add_datetime_to_context=True
    )


agent = build_agent()