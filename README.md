# CrewAI YouTube Video Blog Writer

This project uses [CrewAI](https://www.crewai.com/) to autonomously research a specific topic across a target YouTube channel and generate a comprehensive blog post based on the video transcripts.

## Features

- **YouTube Channel Search**: Utilizes `crewai-tools` to fetch and search through a YouTube channel's most recent videos using Retrieval-Augmented Generation (RAG).
- **Multi-Agent System**:
  - **Blog Researcher**: Extracts video transcripts and gathers detailed information on the target topic.
  - **Blog Writer**: Synthesizes the research into an engaging, accessible blog narrative.

## Setup

1. **Ensure you have Python installed** (preferably 3.10 or higher).
2. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Variables**:
   Create a `.env` file in the root of the project and add your OpenAI API key (and optionally your Gemini key if modifying the LLM setup):
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

1. Open `crew.py` to change the topic if desired (currently set to `"machine learning"`).
2. Open `tools.py` to change the target YouTube channel by updating the `youtube_channel_handle`.
3. Run the main script to orchestrate the AI agents:
   ```bash
   python crew.py
   ```
4. The agents will collaborate to research the channel and write a new markdown blog post, outputting the final result to `output-new-blog-post.md`.
