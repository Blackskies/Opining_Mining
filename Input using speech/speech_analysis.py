import re
from textblob import TextBlob
import speech_recognition as sr

class Analysis():

    def CleanInput(self, input_statement):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", input_statement).split())
    
    def GetSentiment(self,input_statement):
        analysis = TextBlob(self.clean_input(input_statement))
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

class SpeechRecognition():
    record = sr.Recognizer()
    def recording(self):
        print("Device is ready and recording started \n(*Note: Wait atleast 1Min for voice to be recognised depending on the netspeed\t)")
        with sr.Microphone() as source:
            audio = self.record.listen(source)
            text = self.record.recognize_google(audio)
            print("you said "+ text )
        return text
        


def main():
    InputStatement = SpeechRecognition().recording()
    process = Analysis(InputStatement)
    CleanedText = process.CleanInput(InputStatement)
    result = process.GetSentiment(CleanedText)
    print("*****************************")
    print(result)

if __name__=="__main__":
    main()
