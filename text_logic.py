import difflib


class TextStreamProcessor:
    def __init__(self, similarity_threshold):
        self.last_text = ''
        self.threshold = similarity_threshold
    
    def get_new_content(self, current_text):
        if not current_text:
            return None
        
        similarity = difflib.SequenceMatcher(None, self.last_text, current_text).ratio()
        if self.last_text and similarity >= self.threshold:
            self.last_text = current_text
            return None
        
        text_to_speak = current_text

        if self.last_text and similarity < self.threshold:
            end_index = len(self.last_text)
            if len(current_text) > end_index:
                text_to_speak = current_text[end_index:].strip()
            else:
                text_to_speak = current_text

        self.last_text = current_text

        return text_to_speak if text_to_speak.strip() else None