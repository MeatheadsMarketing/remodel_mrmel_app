# PHASE_2_FILE: Uses GPT to identify and tag room/zone types from transcript text
# Origin: Blueprint Phase 2 — GPT VOICE INTELLIGENCE
# Role: Parse transcript phrases and output structured room zones and spatial tags

import os
import json
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def tag_zones(transcript_path):
    with open(transcript_path, "r", encoding="utf-8") as f:
        transcript_data = json.load(f)

    prompt_intro = "Extract spatial zones and room names mentioned in this transcript. Output JSON like: [{'zone':'kitchen','start':10.3,'end':23.5}, ...]"

    full_text = transcript_data.get("text", "")
    if not full_text:
        print("[ERROR] Transcript is empty or missing.")
        return None

    prompt = f"{prompt_intro}

Transcript:
{full_text[:4000]}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a zone-tagging assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )

        parsed = response['choices'][0]['message']['content']
        output_dir = "layout_test/parsed_commands"
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "zone_tags.json")

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(parsed)

        return output_path
    except Exception as e:
        print(f"[ERROR] GPT tagging failed: {e}")
        return None
