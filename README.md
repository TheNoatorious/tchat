# tchat

This project is a case study of using a conversational model

## Theory

LLM stands for **Large Language Model**. It is an algorithm that generates an amount of text and there are many different models out there.

**Most LLM’s follow a completion style of text generation:**

When the input is “_I’m a comedian who jokes about taxes. Have you ever noticed how taxes_”, the LLM will finish the sentence by itself by using the first sentence as context in this case. It can be thought of an advanced auto-complete.

**Other LLM’s have been adjusted to use a conversational style of generation**, e.g. as seen in ChatGPT.

OpenAI and LangChain use different terminology which is important to understand:

| OpenAI Terminology | LangChain Terminology |
| ------------------ | --------------------- |
| System Message     | System Message        |
| User Message       | Human Message         |
| Assistant Message  | AI Message            |

-   **System Message**: Tell how the AI should reply e.g. happy, angry, sad etc.
-   **User Message**: Prompt by the user..
-   **Assistant Message**: Answer by the AI

ChatGPT is still an LLM, but in LangChain it’s categorised as `chat_models` instead of `llm`.
