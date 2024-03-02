import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os
import pywhatkit
import time
import pyjokes
import wikipedia


engine = pyttsx3.init()
engine.setProperty("rate", 150)

voices= engine.getProperty("voices")
engine.setProperty( "voice", voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognizing")
            query = r.recognize_google(audio, language="en")
            return query
        
        except Exception as e:
            return "Error Occurred. Sorry."
import time
def time_command():
    timee=int(time.strftime(("%H")))
    if timee>=4  and timee<12:
        output="Good Morning"
    elif timee>=12 and timee<18:
        output="Good Afternoon"
    else:
        output="Good Evening"
    return output

if __name__ == "__main__":
    output=time_command()
    print(f"{output} Iam Your Assistant")
    speak(f"{output} Iam Your Assistant")
        
    while True:
        print("Listening")
        query = takeCommand()
        print(f"User Said: {query}")


        if "exit" in query.lower():
            print("Exiting the assistant.")
            speak("Goodbye!")
            break

    
        sites = [
    ["Google", "https://www.google.com"],
    ["YouTube", "https://www.youtube.com"],
    ["Facebook", "https://www.facebook.com"],
    ["Twitter", "https://www.twitter.com"],
    ["Instagram", "https://www.instagram.com"],
    ["LinkedIn", "https://www.linkedin.com"],
    ["Amazon India", "https://www.amazon.in"],
    ["Flipkart", "https://www.flipkart.com"],
    ["Snapdeal", "https://www.snapdeal.com"],
    ["Paytm", "https://www.paytm.com"],
    ["IRCTC (Indian Railways)", "https://www.irctc.co.in"],
    ["NDTV", "https://www.ndtv.com"],
    ["The Times of India", "https://timesofindia.indiatimes.com"],
    ["BookMyShow", "https://in.bookmyshow.com"],
    ["Zomato", "https://www.zomato.com"],
    ["MakeMyTrip", "https://www.makemytrip.com"],
    ["WhatsApp", "https://www.whatsapp.com"],
    ["Telegram", "https://telegram.org"],
    ["ShareChat", "https://www.sharechat.com"],
    ["RESSO", "https://www.resso.com"],
    ["MXTakatak", "https://www.mxtakatak.com"],
    ["Amazon Prime Video", "https://www.primevideo.com"],
    ["Hotstar", "https://www.hotstar.com"],
    ["Netflix", "https://www.netflix.com"],
    ["Voot", "https://www.voot.com"],
    ["SonyLIV", "https://www.sonyliv.com"],
    ["Hindustan Times", "https://www.hindustantimes.com"],
    ["The Indian Express", "https://indianexpress.com"],
    ["ABP News", "https://www.abplive.com"],
    ["MoneyControl", "https://www.moneycontrol.com"],
    ["Cricbuzz", "https://www.cricbuzz.com"],
    ["ESPNcricinfo", "https://www.espncricinfo.com"],
    ["HDFC Bank", "https://www.hdfcbank.com"],
    ["ICICI Bank", "https://www.icicibank.com"],
    ["Axis Bank", "https://www.axisbank.com"],
    ["State Bank of India", "https://www.sbi.co.in"],
    ["Naukri.com", "https://www.naukri.com"],
    ["Monster India", "https://www.monsterindia.com"],
    ["Indeed", "https://www.indeed.co.in"],
    ["Quikr", "https://www.quikr.com"],
    ["OLX India", "https://www.olx.in"],
    ["Justdial", "https://www.justdial.com"],
    ["Magicbricks", "https://www.magicbricks.com"],
    ["99acres", "https://www.99acres.com"],
    ["Jio", "https://www.jio.com"],
    ["Airtel", "https://www.airtel.in"],
    ["Vodafone Idea", "https://www.myvi.in"],
    ["Hindustan Unilever", "https://www.hul.co.in"],
    ["Tata Consultancy Services", "https://www.tcs.com"],
    ["Infosys", "https://www.infosys.com"],
    ["Wipro", "https://www.wipro.com"],
    ["Tech Mahindra", "https://www.techmahindra.com"],
    ["Reliance Industries", "https://www.ril.com"],
    ["Tata Motors", "https://www.tatamotors.com"],
    ["Mahindra & Mahindra", "https://www.mahindra.com"],
    ["Hero MotoCorp", "https://www.heromotocorp.com"],
    ["Bajaj Auto", "https://www.bajajauto.com"],
    ["Maruti Suzuki", "https://www.marutisuzuki.com"],
    ["RIL (Reliance Jio)", "https://www.jio.com"],
    ["Airtel (Bharti Airtel)", "https://www.airtel.in"],
    ["Vodafone Idea (Vi)", "https://www.myvi.in"],
    ["HDFC Bank", "https://www.hdfcbank.com"],
    ["ICICI Bank", "https://www.icicibank.com"],
    ["Axis Bank", "https://www.axisbank.com"],
    ["State Bank of India", "https://www.sbi.co.in"],
    ["HCL Technologies", "https://www.hcltech.com"],
    ["Wipro", "https://www.wipro.com"],
    ["Infosys", "https://www.infosys.com"],
    ["Tata Consultancy Services (TCS)", "https://www.tcs.com"],
    ["Accenture", "https://www.accenture.com"],
    ["Cognizant", "https://www.cognizant.com"],
    ["Tech Mahindra", "https://www.techmahindra.com"],
    ["Amazon Web Services (AWS)", "https://aws.amazon.com"],
    ["IBM India", "https://www.ibm.com/in-en"],
    ["Microsoft India", "https://www.microsoft.com/en-in"],
    ["Flipkart", "https://www.flipkart.com"],
    ["Snapdeal", "https://www.snapdeal.com"],
    ["Myntra", "https://www.myntra.com"],
    ["BigBasket", "https://www.bigbasket.com"],
    ["Swiggy", "https://www.swiggy.com"],
    ["Zomato", "https://www.zomato.com"],
    ["Foodpanda", "https://www.foodpanda.in"],
    ["BookMyShow", "https://in.bookmyshow.com"],
    ["Paytm Mall", "https://paytmmall.com"],
    ["Ola Cabs", "https://www.olacabs.com"],
    ["Uber India", "https://www.uber.com/in/en"],
    ["MakeMyTrip", "https://www.makemytrip.com"],
    ["Cleartrip", "https://www.cleartrip.com"],
    ["Goibibo", "https://www.goibibo.com"],
    ["RedBus", "https://www.redbus.in"],
    ["Chatbot", "https://chat.openai.com"],
    ["Anime", "https://aniwatch.to/"]
    ]

        for site in sites:
         if f"Open {site[0]}".lower() in query.lower():
             print(f"Opening {site[0]}")
             speak(f"Opening {site[0]}")
             webbrowser.open(site[1])

        if "Search".lower() in query.lower():
         search=query.replace("search", "")
         print(f"Searching{search}")
         speak(f"Searching{search}")
         pywhatkit.search(search)
        if "how are you".lower() in query.lower():
            response="i am good how about you"
            print(response)
            speak(response)

        dt=datetime.datetime.now()
        if "time".lower() in query:
             hour=dt.strftime("%I")
             mine=dt.now().strftime("%M")
             print(f'The time is {hour} hours and {mine} Minutes')
             speak(f'The time is {hour} hours and {mine} Minutes')
        if "today's date".lower() in query:
             date = dt.today().strftime('%D')
             print(f"Today's Date is {date}")
             speak(f"Today's Date is {date}")
     
        if 'who are you'.lower() in query:
           print("I am your personal assistant.")
           speak("I am your personal assistant.")

        if "date tomorrow" in query:
           tomorrow = (datetime.date.today() + datetime.timedelta(days=1))
           tomorrow_formatted = tomorrow.strftime('%D')
           print(f"The date tomorrow is: {tomorrow_formatted}")
           speak(f"The date tomorrow is: {tomorrow_formatted}")
        if "date yesterday".lower() in query.lower():
             yesterday = (datetime.date.today() + datetime.timedelta(days=-1))
             yesterday_formatted = yesterday.strftime('%D')
             print(f"The date yesterday was: {yesterday_formatted}")
             speak(f"The date yesterday was: {yesterday_formatted}")

        if "send a message".lower() in query.lower():
         print("Say the number")
         speak("Say the number")
         number = "+91" + takeCommand()
         number1 = ''.join(filter(str.isdigit, number))
         print(number1)
         time.sleep(2)
         print("Say the message")
         speak("Say the message")
         message1 = takeCommand()
         print(message1)
         try:
             pywhatkit.sendwhatmsg_instantly(f"+{number1}", message1)
             print("Message sent successfully!")
         except Exception as e:
              print(f"An error occurred: {str(e)}")

        if "play".lower() in query.lower():
            songName= query.replace("play","")
            RealName= songName.replace("hey assistant","")
            print(f"Playing{RealName}")
            speak(f"Playing{RealName}")
            pywhatkit.playonyt(RealName)

        if 'Joke'.lower() in query.lower():
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)
            
        if 'get information'.lower() in query.lower():
            info = query.replace("get information of", "")
            results = wikipedia.summary(info, sentences=3)
            print(results)
            speak(results)

        if "i am fine".lower() in query.lower():
            response="good to hear that, How can i help you"
            print(response)
            speak(response)
        



        

    
    

        
        
            










