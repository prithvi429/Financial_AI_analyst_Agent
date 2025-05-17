import openai
from phi.agent import Agent
import phi.api
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
from phi.model.groq import Groq

import os
import phi
from phi.playground import Playground, serve_playground_app
from fastapi.responses import RedirectResponse

# Load environment variables from .env file
load_dotenv()

phi.api=os.getenv("GROQ_API_KEY")

## web search agent
web_search_agent=Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["Alway include sources"],
    show_tools_calls=True,
    markdown=True,

)

## Financial agent
finance_agent=Agent(
    name="Finance AI Agent",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
                      company_news=True),
    ],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,

)

app=Playground(agents=[finance_agent,web_search_agent]).get_app()

@app.get("/")
def redirect_to_playground():
    return RedirectResponse(url="/playground")

if __name__=="__main__":
    print("Starting server at http://localhost:7777")
    serve_playground_app(app, reload=True)
