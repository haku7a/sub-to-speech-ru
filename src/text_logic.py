import difflib


class TextStreamProcessor:
    def __init__(self, similarity_threshold):
        self.similarity_threshold = similarity_threshold
        self.last_lines = []

    def get_new_content(self, current_text):
        if not current_text:
            return None

        current_lines = [line.strip() for line in current_text.split('\n') if line.strip()]

        if not current_lines:
            return None

        if not self.last_lines:
            self.last_lines = current_lines
            return " ".join(current_lines)
        
        overlap_count = 0
        
        max_possible_overlap = min(len(self.last_lines), len(current_lines))
        
        for i in range(max_possible_overlap, 0, -1):
            old_slice = self.last_lines[-i:]
            curr_slice = current_lines[:i]
            
            if self.are_blocks_similar(old_slice, curr_slice):
                overlap_count = i
                break

        new_lines = current_lines[overlap_count:]
        
        if not new_lines:

            if len(current_lines) > len(self.last_lines):
                 self.last_lines = current_lines
            return None

        if overlap_count == 0:
            full_old_str = "".join(self.last_lines)
            full_new_str = "".join(current_lines)
            matcher = difflib.SequenceMatcher(None, full_old_str, full_new_str)
            if matcher.ratio() > 0.8:
                return None

        self.last_lines = current_lines
        
        return " ".join(new_lines)

    def are_blocks_similar(self, lines1, lines2):
        if len(lines1) != len(lines2):
            return False
            
        text1 = "".join(lines1)
        text2 = "".join(lines2)
        
        matcher = difflib.SequenceMatcher(None, text1, text2)
        return matcher.ratio() >= self.similarity_threshold