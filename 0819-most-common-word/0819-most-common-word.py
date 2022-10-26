class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.replace('.',' ')
        paragraph = paragraph.replace(',',' ')
        paragraph = paragraph.replace('!',' ')
        paragraph = paragraph.replace('?',' ')
        paragraph = paragraph.replace(';',' ')
        paragraph = paragraph.replace("'",' ')
        paragraph = paragraph.lower()
        count_word = collections.defaultdict(int)
        for word in paragraph.split():
            if word in banned:
                continue
            count_word[word] += 1

        return max(count_word, key=count_word.get)