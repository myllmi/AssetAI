# 🚀 Asset AI

**Asset AI** is a powerful and modular tool that leverages **Artificial Intelligence** to streamline integration with external APIs. It provides a seamless interface for understanding, interacting with, and testing APIs using natural language — turning complex API workflows into intuitive chat-driven experiences.

---

## 🧠 How It Works

Asset AI is divided into **three core modules**, each playing a critical role in transforming API specs into a conversational interface:

### 1. 📦 Loader

- Reads, parses, and validates the **OpenAPI specification** of any external API.
- Converts API definitions into structured data, ready for AI processing.
- Ensures all API operations are indexed and understandable.

### 2. 🔧 Back-End

- Receives chat requests from the front-end.
- Uses **LLMs** and **embedding models** to interpret user intent.
- Maps natural language to API operations, formulates requests, and returns structured responses.
- Built using **Python**, **Flask**, and **Langchain**.

### 3. 💬 Front-End

- A modern **Angular**-based interface with a conversational UI.
- Users can interact via chat to query, explore, and test APIs.
- Displays formatted responses, status codes, and more.

---

## 🛠 Technologies Used

| Component     | Technology                                    |
|---------------|-----------------------------------------------|
| LLMs & Embeddings | Used for natural language understanding and similarity search |
| Vector Search | MongoDB with **Vector Search** for fast semantic querying |
| Back-End      | **Python**, **Flask**, **Langchain**         |
| Front-End     | **Angular** with chat-based UI               |
| Data Storage  | **MongoDB** with native vector support        |

---

## 🧪 Use Cases

- Explore any OpenAPI-compatible API without writing a single line of code
- Automatically generate valid API requests from simple text prompts
- Integrate and test third-party APIs with natural language
- Build and debug workflows without switching between docs and tools

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.9+
- Node.js & npm
- MongoDB with Vector Search enabled

### 📥 Clone the Repository

```bash
git clone https://github.com/myllmi/AssetAI.git
cd asset-ai
