# Financial_AI_analyst_Agent

Multi-agent AI system for financial analysis using LLMs, web search, and automated reasoning.

## Features

- **Web Search Agent:** Uses DuckDuckGo to search the web and always includes sources.
- **Finance AI Agent:** Retrieves stock prices, analyst recommendations, fundamentals, and company news using YFinance.
- **Interactive Playground:** Web UI to interact with both agents.
- **LLM Powered:** Utilizes Groq Llama 3 model for advanced reasoning and responses.

## Requirements

- Python 3.8+
- [phi](https://github.com/phi-ai/phi)
- [fastapi](https://fastapi.tiangolo.com/)
- [uvicorn](https://www.uvicorn.org/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [openai](https://pypi.org/project/openai/)

## Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/Financial_AI_analyst_Agent.git
    cd Financial_AI_analyst_Agent
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv fenv
    fenv\Scripts\activate
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
    - Create a `.env` file in the project root.
    - Add your Groq API key:
      ```
      GROQ_API_KEY=your_groq_api_key_here
      ```

## Running the App

```sh
python playground.py
```
or (for auto-reload during development):
```sh
uvicorn playground:app --reload --port 7777
```

Visit [http://localhost:7777/](http://localhost:7777/) in your browser.

## Usage

- Interact with the **Web Search Agent** for general information and sources.
- Use the **Finance AI Agent** for financial data, analysis, and news.

## License

MIT License

---

*Built with [Phi](https://github.com/phi-ai/phi) and FastAPI.*
