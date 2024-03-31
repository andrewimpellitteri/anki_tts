# anki_utils.py

def parse_anki_deck(deck_path):
    deck_data = []
    with open(deck_path, 'r', encoding='utf-8') as deck_file:
        lines = deck_file.readlines()
        question = ""
        answer = ""
        card_id = 1
        for line in lines:
            line = line.strip()
            if line.startswith("Q:"):
                if question and answer:
                    deck_data.append({
                        'id': card_id,
                        'question': question,
                                'answer': answer
                    })
                    card_id += 1
                    question = line[2:].strip()
                    answer = ""
            elif line.startswith("A:"):
                answer = line[2:].strip()
            else:
                if question:
                    answer += " " + line

        # Add the last card
        if question and answer:
            deck_data.append({
                'id': card_id,
                'question': question,
                'answer': answer
            })

    return deck_data