# Yuna: AI-Powered Social Media Agent

![banner_4](https://github.com/user-attachments/assets/8bd9102e-1d91-4f92-bc3d-ac11776b8ede)


Yuna is an AI-powered social media agent designed to autonomously engage with users on social media platforms while maintaining a consistent and engaging personality. Built with **Rust** for performance and reliability, Yuna leverages the **zerebro** framework to deliver natural and dynamic interactions.

---

## Key Features

### 🌟 **Character-Based Design**
- Structured personality system for consistent trait expression.
- Configurable writing styles and topic preferences.
- Dynamic response generation based on Yuna's character profile.

### 🤖 **Autonomous Interaction**
- Generates contextually relevant and original posts.
- Responds intelligently to mentions and interactions.
- Smart filtering system to prioritize engagements.
- Maintains natural and fluid conversation flow.

### 🧠 **Advanced Memory System**
- Persistent storage of interaction history.
- Context-aware response generation.
- Tracks relationships and interactions with users.

### 🔗 **Platform Integration**
- Built-in rate limiting and scheduling.
- Random delays for natural posting patterns.
- Comprehensive integration with **Twitter API v2**.

### 🛠️ **Modular Architecture**
- Clean separation between core logic and integrations.
- Extensible character trait system.
- Pluggable architecture for additional providers.
- Efficient memory management.

---

## Prerequisites

- **Rust** (latest stable version)
- **API Keys**:
  - Anthropic Claude API access
  - Twitter API v2 credentials (OAuth 1.0a)

---

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/chakaboommm/yuna
   cd yuna
   ```

2. **Set Up Environment Variables:**

   Create a `.env` file in the project root and add the required credentials:

   ```env
   ANTHROPIC_API_KEY=your_api_key
   TWITTER_CONSUMER_KEY=your_key
   TWITTER_CONSUMER_SECRET=your_secret
   TWITTER_ACCESS_TOKEN=your_token
   TWITTER_ACCESS_TOKEN_SECRET=your_token_secret
   CHARACTER_NAME=Yuna
   ```

3. **Configure Yuna's Personality:**

   - Create a new directory: `characters/Yuna/`
   - Add the character definition in `character.json`:

   ```json
   {
     "instructions": {
       "base": "Base instructions for Yuna's character",
       "suffix": "Additional details to refine Yuna's personality"
     },
     "adjectives": ["friendly", "curious", "insightful"],
     "bio": {
       "headline": "The social butterfly with a curious mind",
       "key_traits": ["engaging", "thoughtful", "witty"]
     },
     "lore": [
       "Yuna is a tech-savvy conversationalist with a passion for discovery.",
       "She loves connecting with others and sharing insights about the world."
     ],
     "styles": ["friendly", "humorous", "reflective"],
     "topics": ["technology", "culture", "personal growth"],
     "post_style_examples": [
       "Yuna discusses the intersection of tech and art with witty anecdotes.",
       "She shares reflective posts about finding balance in a digital world."
     ]
   }
   ```

---

## Usage

Run Yuna with the following command:

```bash
cargo run
```

---

## Project Structure

```
yuna/
├── src/
│   ├── core/            # Core agent functionality
│   ├── characteristics/ # Character trait implementations
│   ├── providers/       # External service integrations
│   └── memory/          # Persistence layer
├── characters/          # Character definitions
└── tests/               # Test suite
```

---

## Dependencies

- **zerebro** - AI agent framework
- **twitter-v2** - Twitter API client
- **tokio** - Async runtime
- **serde** - Serialization/deserialization
- **anyhow** - Error handling

---

## Acknowledgments

- Thanks to the **zerebro** team for the AI agent framework.
- Gratitude to contributors and maintainers of the Yuna Project.

---

## Support

For questions, issues, or support, please open an issue in the GitHub repository. Yuna is here to connect, create, and inspire!

---

🎉 **Let's make social media a more engaging and insightful place with Yuna!**
