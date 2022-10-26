class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.replace('.',' ')
        paragraph = paragraph.replace(',',' ')
        paragraph = paragraph.replace('!',' ')
        paragraph = paragraph.replace('?',' ')
        paragraph = paragraph.replace(';',' ')
        paragraph = paragraph.replace("'",' ')

        print(paragraph)
        paragraph = paragraph.lower()
        count_word = {}
        for word in paragraph.split():
            if word in banned:
                continue
            if word not in count_word:
                count_word[word] = 1
            else:
                count_word[word] += 1

        return max(count_word, key=count_word.get)