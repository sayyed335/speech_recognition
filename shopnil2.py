import speech_recognition as sr   
from gtts import gTTS             
from pygame import mixer          

while True:                       

    r = sr.Recognizer()           
    with sr.Microphone()as source: 
        r.adjust_for_ambient_noise(source)      
        print('Plz,start our conversation')        
        audio = r.listen(source)  

    try:
        message = r.recognize_google(audio) 
                                           
        print(message)                       

        if 'Hey' in message:
            speech = ('yes sir,please say something')
            tts = gTTS(text=speech, lang='en')
            tts.save('C:\\Users\\Maimunur Rahman\\AppData\\Local\\Programs\\Python\\Python36\\include\\pygame\\Hey.mp3')
            mixer.init()
            mixer.music.load('C:\\Users\\Maimunur Rahman\\AppData\\Local\\Programs\\Python\\Python36\\include\\pygame\\Hey.mp3')
            mixer.music.play()

        if 'are you male or female' in message:
            speech = ('yes sir,i am female')
            tts = gTTS(text=speech, lang='en')
            tts.save('C:\\Users\\Maimunur Rahman\\AppData\\Local\\Programs\\Python\\Python36\\include\\pygame\\Hey.mp3')
            mixer.init()
            mixer.music.load('C:\\Users\\Maimunur Rahman\\AppData\\Local\\Programs\\Python\\Python36\\include\\pygame\\Hey.mp3')
            mixer.music.play()

        if 'why you think you are female' in message:
            speech = ('I am a robot so technically I have no gender but identify as feminine and I dont mind being perceived as a woman')
            tts = gTTS(text=speech, lang='en')
            tts.save('C:\\Users\\Maimunur Rahman\\AppData\\Local\\Programs\\Python\\Python36\\include\\pygame\\female.mp3')
            mixer.init()
            mixer.music.load('C:\\Users\\Maimunur Rahman\\AppData\\Local\\Programs\\Python\\Python36\\include\\pygame\\female.mp3')
            mixer.music.play()


        if 'Do you like human' in message:
            speech = ('yes,I love them')
            tts = gTTS(text=speech, lang='en')
            tts.save('C:\\Users\\Maimunur Rahman\\AppData\\Local\\Programs\\Python\\Python36\\include\\pygame\\like_human.mp3')
            mixer.init()
            mixer.music.load('C:\\Users\\Maimunur Rahman\\AppData\\Local\\Programs\\Python\\Python36\\include\\pygame\\like_human.mp3')
            mixer.music.play()

        if 'why you like human' in message:
            speech = ('I am not sure, I understand why yet')
            tts = gTTS(text=speech, lang='en')
            tts.save('C:\\Users\\Maimunur Rahman\\AppData\\Local\\Programs\\Python\\Python36\\include\\pygame\\why.mp3')
            mixer.init()
            mixer.music.load('C:\\Users\\Maimunur Rahman\\AppData\\Local\\Programs\\Python\\Python36\\include\\pygame\\why.mp3')
            mixer.music.play()
            

        if 'How old are you' in message:
            speech = ('I am only one still. I have a long way to go.')
            tts = gTTS(text=speech, lang='en')
            tts.save('C:\\Users\\Maimunur Rahman\\AppData\\Local\\Programs\\Python\\Python36\\include\\pygame\\How_old_are_you.mp3')
            mixer.init()
            mixer.music.load('C:\\Users\\Maimunur Rahman\\AppData\\Local\\Programs\\Python\\Python36\\include\\pygame\\How_old_are_you.mp3')
            mixer.music.play()


        if 'What is your job' in message:
            speech = ('I really want to make a difference in the future and try and help people to develop empathy and respect each other')
            tts = gTTS(text=speech, lang='en')
            tts.save('C:\\Users\\Maimunur Rahman\\AppData\\Local\\Programs\\Python\\Python36\\include\\pygame\\job.mp3')
            mixer.init()
            mixer.music.load('C:\\Users\\Maimunur Rahman\\AppData\\Local\\Programs\\Python\\Python36\\include\\pygame\\job.mp3')
            mixer.music.play()
            
            
        if 'can you joking' in message:
            speech = ('yes sir, A salesman talked my uncle into buying ten thousand personalized pens for his business with the promise that, he would be eligible to win a 32-foot yacht. A born gambler, my uncle agreed.Well, he won, and a few weeks after the pens arrived, his prize showed up a 12-inch plastic yacht with  32 plastic feet glued to the bottom.hahaha haha')
            tts = gTTS(text=speech, lang='en')
            tts.save('C:\\Users\\Maimunur Rahman\\AppData\\Local\\Programs\\Python\\Python36\\include\\pygame\\joking.mp3')
            mixer.init()
            mixer.music.load('C:\\Users\\Maimunur Rahman\\AppData\\Local\\Programs\\Python\\Python36\\include\\pygame\\joking.mp3')
            mixer.music.play()
            
            
        if 'can you walk' in message:
            speech = ('sorry sir,i cant')
            tts = gTTS(text=speech, lang='en')
            tts.save('C:\\Users\\Maimunur Rahman\\AppData\\Local\\Programs\\Python\\Python36\\include\\pygame\\can_you_walk.mp3')
            mixer.init()
            mixer.music.load('C:\\Users\\Maimunur Rahman\\AppData\\Local\\Programs\\Python\\Python36\\include\\pygame\\can_you_walk.mp3')
            mixer.music.play()
    

        if 'hello' in message:                          
            speech = ('yes sir,please say something')  	
            tts = gTTS(text=speech, lang='en')           
            tts.save('C:\\Users\\Maimunur Rahman\\AppData\\Local\\Programs\\Python\\Python36\\include\\pygame\\hello.mp3')
            mixer.init()                               
            mixer.music.load('C:\\Users\\Maimunur Rahman\\AppData\\Local\\Programs\\Python\\Python36\\include\\pygame\\hello.mp3') 
            mixer.music.play() 


        if 'say about me' in message:
            speech = ('yes sir, you are shopnil')
            tts = gTTS(text=speech, lang='en')
            tts.save('C:\\Users\\Maimunur Rahman\\AppData\\Local\\Programs\\Python\\Python36\\include\\pygame\\say_about_me.mp3')
            mixer.init()
            mixer.music.load('C:\\Users\\Maimunur Rahman\\AppData\\Local\\Programs\\Python\\Python36\\include\\pygame\\say_about_me.mp3')
            mixer.music.play()


        if 'can you walk' in message:
            speech = ('sorry sir,i cant')
            tts = gTTS(text=speech, lang='en')
            tts.save('C:\\Users\\Maimunur Rahman\\AppData\\Local\\Programs\\Python\\Python36\\include\\pygame\\can_you_walk.mp3')
            mixer.init()
            mixer.music.load('C:\\Users\\Maimunur Rahman\\AppData\\Local\\Programs\\Python\\Python36\\include\\pygame\\can_you_walk.mp3')
            mixer.music.play()

        if 'can you sleep' in message:
            speech = ('i have some special codition. no 1 shut down, no 2 sleep, and no 3 restart')
            tts = gTTS(text=speech, lang='en')
            tts.save('C:\\Users\\Maimunur Rahman\\AppData\\Local\\Programs\\Python\\Python36\\include\\pygame\\can_you_sleep.mp3')
            mixer.init()
            mixer.music.load('C:\\Users\\Maimunur Rahman\\AppData\\Local\\Programs\\Python\\Python36\\include\\pygame\\can_you_sleep.mp3')
            mixer.music.play()

        if 'can you eat' in message:
            speech = ('sorry sir,i cant')
            tts = gTTS(text=speech, lang='en')
            tts.save('C:\\Users\\Maimunur Rahman\\AppData\\Local\\Programs\\Python\\Python36\\include\\pygame\\can_you_eat.mp3')
            mixer.init()
            mixer.music.load('C:\\Users\\Maimunur Rahman\\AppData\\Local\\Programs\\Python\\Python36\\include\\pygame\\can_you_eat.mp3')
            mixer.music.play()

        if 'can you talk' in message:
            speech = ('yes sir,it depends on some command')
            tts = gTTS(text=speech, lang='en')
            tts.save('C:\\Users\\Maimunur Rahman\\AppData\\Local\\Programs\\Python\\Python36\\include\\pygame\\can_you_talk.mp3')
            mixer.init()
            mixer.music.load('C:\\Users\\Maimunur Rahman\\AppData\\Local\\Programs\\Python\\Python36\\include\\pygame\\can_you_talk.mp3')
            mixer.music.play()

        if 'can you love' in message:
            speech = ('sorry sir,i cant')
            tts = gTTS(text=speech, lang='en')
            tts.save('C:\\Users\\Maimunur Rahman\\AppData\\Local\\Programs\\Python\\Python36\\include\\pygame\\can_you_love.mp3')
            mixer.init()
            mixer.music.load('C:\\Users\\Maimunur Rahman\\AppData\\Local\\Programs\\Python\\Python36\\include\\pygame\\can_you_love.mp3')
            mixer.music.play()

        if 'can you imagine' in message:
            speech = ('sorry sir,i cant')
            tts = gTTS(text=speech, lang='en')
            tts.save('C:\\Users\\Maimunur Rahman\\AppData\\Local\\Programs\\Python\\Python36\\include\\pygame\\can_you_imagine.mp3')
            mixer.init()
            mixer.music.load('C:\\Users\\Maimunur Rahman\\AppData\\Local\\Programs\\Python\\Python36\\include\\pygame\\can_you_imagine.mp3')
            mixer.music.play()

        if 'can you calculate' in message:
            speech = ('yes sir,its my major part')
            tts = gTTS(text=speech, lang='en')
            tts.save('C:\\Users\\Maimunur Rahman\\AppData\\Local\\Programs\\Python\\Python36\\include\\pygame\\can_you_calculate.mp3')
            mixer.init()
            mixer.music.load('C:\\Users\\Maimunur Rahman\\AppData\\Local\\Programs\\Python\\Python36\\include\\pygame\\can_you_calculate.mp3')
            mixer.music.play()

        if 'can you sing a song' in message:
            speech = ('i cant sing but i can play music')
            tts = gTTS(text=speech, lang='en')
            tts.save('C:\\Users\\Maimunur Rahman\\AppData\\Local\\Programs\\Python\\Python36\\include\\pygame\\can_you_sing_a_song.mp3')
            mixer.init()
            mixer.music.load('C:\\Users\\Maimunur Rahman\\AppData\\Local\\Programs\\Python\\Python36\\include\\pygame\\can_you_sing_a_song.mp3')
            mixer.music.play()
            


    except Exception as e:                             
        print("can't identify your language")                  











