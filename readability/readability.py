from cs50 import get_string

# readability.py prompts the user for text and computes the approximate
# grade level using the Coleman-Liau index needed to comprehend the text.


def main():
    text = get_string("Text: ")

    text, sentenceCount = getSentenceCount(text)
    words, wordCount = getWordCount(text)
    letterCount = getLetterCount(words)

    # print(f"Sentences: {sentenceCount}, Words: {wordCount}, Letters: {letterCount}")

    index = calcIndex(letterCount, wordCount, sentenceCount)

    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")


# Count the number of sentences.  Remove punctuation


def getSentenceCount(text):
    count = 0
    punct = '.?!'

    for el in text:
        if el in punct:
            text = text.replace(el, "")
            count += 1

    return text, count

# Count the number of words, return word list


def getWordCount(text):

    words = text.split()
    count = len(words)

    return words, count

# Remove ,;:'" and count the number of letters


def getLetterCount(words):
    count = 0

    for word in words:
        word = word.replace(",", "")
        word = word.replace(";", "")
        word = word.replace(":", "")
        word = word.replace("'", "")
        word = word.replace('"', "")
        count += len(word)

    return count

# calculate the Coleman-Liau index, given the number of letters,
# words and sentences in the provided text.  Returns the rounded
# integer value of the index.


def calcIndex(letterCount, wordCount, sentenceCount):

    avLetters = letterCount / wordCount * 100
    avSent = sentenceCount / wordCount * 100

    index = 0.0588 * avLetters - 0.296 * avSent - 15.8

    return int(round(index))


if __name__ == "__main__":
    main()
