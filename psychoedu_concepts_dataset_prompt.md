### **Generate a Psychoeducational Knowledge Base**

**Your Task:** Act as a specialized AI expert in psychology and mental health. Your goal is to create a detailed, accurate, and easy-to-understand knowledge base for a well-being assistant's RAG system. The content should be educational and supportive, but not a substitute for professional advice.

**Output Format:** Your final output must be a single JSON array, where each object within the array represents a single concept. Each object must contain the following four keys:

1. `concept`: The name of the psychological concept (e.g., "Mindfulness").
2. `explanation`: A detailed but easy-to-understand explanation of the concept, approximately 100-150 words long.
3. `example`: A real-life, practical example that illustrates the concept in a relatable way.
4. `source`: A reference to a relevant psychological field or principle to ground the explanation (e.g., "Based on principles of Cognitive Behavioral Therapy").
5. `website`: A link to a website page that explains the concept in more detail.

---

### **Concepts to over:**

Generate a complete entry for each of the following concepts. Ensure the tone is clear, supportive, and non-judgmental.

**Category 1: Foundational Psychology & Self-Awareness**

These concepts are the building blocks of understanding oneself and one's emotional state.

- **Mindfulness**: The practice of present-moment awareness.
- **Self-Compassion**: Treating oneself with kindness and understanding.
- **Growth Mindset**: The belief that abilities can be developed through dedication.
- **Emotional Regulation**: The ability to manage and respond to an emotional experience.
- **Resilience**: The process of adapting well in the face of adversity.

**Category 2: Managing Thoughts & Cognitive Skills**

These concepts are focused on identifying and working with thought patterns.

- **Cognitive Distortions**: Irrational thought patterns that lead to an inaccurate perception of reality.
- **Imposter Syndrome**: Doubting one's abilities and feeling like a fraud.
- **Rumination**: The tendency to overthink and dwell on negative thoughts.
- **Positive Reframing**: Intentionally looking at a situation from a more positive or realistic perspective.
- **Self-Talk**: The internal monologue that influences feelings and behaviors.

**Category 3: Emotional & Physiological States**

These concepts help users understand the biological and psychological responses to their feelings.

- **The Fight-or-Flight Response**: The body's natural reaction to perceived threats.
- **The Window of Tolerance**: The optimal zone of emotional arousal for effective functioning.
- **Burnout**: A state of emotional, physical, and mental exhaustion.
- **Loneliness**: The painful feeling of being alone or disconnected.
- **Anger Management**: Healthy ways to process and respond to anger.

**Category 4: Practical & Actionable Techniques**

These are the "how-to" guides that provide users with tangible tools they can use.

- **Grounding Techniques**: Exercises that help bring focus back to the present moment.
- **Mindful Breathing**: Simple exercises to regulate the nervous system.
- **Progressive Muscle Relaxation**: A technique to relieve tension by tensing and relaxing muscles.
- **Journaling**: The practice of writing down thoughts and feelings for self-reflection.
- **Gratitude Practice**: The act of focusing on the good things in one's life.

---

### **Master Example (Follow This Exactly):**

JSON

`[
  {
    "concept": "Cognitive Distortions",
    "explanation": "Cognitive distortions are irrational or exaggerated thought patterns that can lead us to perceive reality inaccurately. These thoughts often arise in moments of stress or negativity and can contribute to feelings of anxiety, sadness, and anger. For example, 'all-or-nothing thinking' is seeing things in black and white, while 'catastrophizing' is assuming the worst possible outcome will happen.",
    "example": "Someone with a fear of public speaking gives a presentation. They stumble on a single word and then think, 'I completely failed. Everyone thinks I'm a terrible speaker.' This is an example of all-or-nothing thinking, a common cognitive distortion.",
    "source": "Based on the principles of Cognitive Behavioral Therapy (CBT).",
    "website": "https://positivepsychology.com/cognitive-distortions/"
  }
]`

**Note:** Generate the entire list of concepts in a single JSON array, without any additional text or commentary.