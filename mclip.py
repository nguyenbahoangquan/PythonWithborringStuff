import os
import sys, pyperclip

def main():
    print(r'Do nothing do!!!!')
    TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

    if len(sys.argv) < 2:
        print('Usage: py mclip.py [keyphrase] - copy phrase text')
        sys.exit()
    keyphrase = sys.argv[1]
    
    if keyphrase in TEXT:
        pyperclip.copy(TEXT[keyphrase])
        print('Text for "' + keyphrase + '" copied to clipboard.')
    else:
        print('There is no text for ' + keyphrase)
    print("Howl's Moving Castle")


if __name__ == "__main__":
    main()