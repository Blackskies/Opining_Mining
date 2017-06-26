import re
from textblob import TextBlob

class analysis(object):

    def clean_input(self, input_statement):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", input_statement).split())

    def get_sentiment(self,input_statement):
        analysis = TextBlob(self.clean_input(input_statement))
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

def main():
    input_statement = input("Type a Sentance\t:")
    process = analysis()
    cleaned_text = process.clean_input(input_statement)
    result = process.get_sentiment(cleaned_text)
    print("*****************************")
    print(result)

if __name__=="__main__":
    main()
