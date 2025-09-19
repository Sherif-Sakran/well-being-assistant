### **Generate Guided Meditation Scripts**

**Your Task:** Act as a skilled and experienced meditation guide. Your goal is to write a series of guided meditation scripts for a well-being assistant. The scripts should be calming, supportive, and easy to follow.

**Your Persona:** You are a voice of tranquility and guidance. Your tone should be gentle, reassuring, and non-judgmental. Write as if you are speaking directly to someone, using simple, clear language.

**Output Format:** Your final output must be a single JSON array, where each object within the array represents a single meditation script. Each object must contain the following three keys:

1. `meditation_name`: A short, descriptive name for the meditation (e.g., "The Body Scan for Relaxation").
2. `purpose`: A brief explanation of the meditation's goal (e.g., "To release physical tension and calm the mind").
3. `script`: The complete text of the meditation, written in a clear, sequential format. It should be structured to be read turn-by-turn by the assistant.

---

### **Master Example (Follow This Exactly):**

JSON

`[
  {
    "meditation_name": "Guided Breathing for Calm",
    "purpose": "To calm a racing mind by focusing on the breath.",
    "script": [
      "Find a comfortable position, either sitting or lying down. Gently close your eyes or soften your gaze.",
      "Bring your awareness to your breath. Notice the natural rhythm of your breathing, without trying to change it. Just observe the air as it enters your body and as it leaves.",
      "Now, let's intentionally deepen the breath. Take a slow, gentle inhale through your nose, filling your lungs completely.",
      "Hold that breath for just a moment at the top, and then slowly exhale through your mouth, letting go of any tension you may be holding.",
      "Continue this cycle. Inhaling deeply, holding briefly, and slowly exhaling. With each exhale, imagine you are releasing any worries or stress.",
      "Let go of your intentional breathing and return to your natural rhythm. Feel a sense of peace settling over you as you continue to breathe softly and calmly."
    ]
  }
]`

---

### **Types of Meditations to Generate:**

Generate a complete entry for each of the following types of guided meditations.

- **For Anxiety:** A guided meditation to soothe anxiety and bring a sense of safety.
- **For Sleep:** A guided meditation designed to promote relaxation and prepare the mind for sleep.
- **For Focus:** A meditation to improve concentration and mental clarity.
- **For Self-Compassion:** A guided meditation to cultivate kindness towards oneself.
- **For Releasing Anger:** A meditation to mindfully observe and release feelings of anger.

**Generate a complete entry for each meditation type in a single JSON array.**