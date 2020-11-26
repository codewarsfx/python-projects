def process_word(word):
    new_word = ""
    for character in word:
        if character.isalpha():
            new_word += character
    return new_word.lower()


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them",
                           "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being",
                           "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how",
                           "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    new_word_array = []
    # LEARNER CODE START HERE
    file_contents_array = file_contents.split()

    for word in file_contents_array:
        processed_word = process_word(word)
        if len(processed_word) > 0:
            new_word_array.append(processed_word)

    print(new_word_array)

    character_frequency = {}
    for word in new_word_array:
        if word not in uninteresting_words:
            if word not in character_frequency:
                character_frequency[word] = 0
            character_frequency[word] += 1
    # return character_frequency

    # wordcloud


frequencies = calculate_frequencies('''where do you see yourself by next year

id be a very great coder with a great source of income ..

how much work are you willing  to  put in

a lot of work but im just too lazy most times

chidera

yes chidera

we got to have this talk

i know right i was really looking forward to it...you wrote your first code in 2016 got your first laptop in 2019....its 2020 but you are still struglling to commit to it
why is that

i have a very short attention span for things... i love to code right..but the drooling hours of reading materials bores me 

of course it does..nothing great comes easy ...you have to pay the price chidera...everybody believes in you the question is do you believe in your self

nothing great comes easy...everyone had to pay the price...the level of greatness you wish to have comes at the price of continuosly studying getting better..improving your craft...making waves ..thats the important part chidera

tell me what stopping you from being the best out there 

i look down on myself like i dont deserve good things
i procrastinate alot
im lazy
i hate my life

but hey chidera consider the great things you have achieved in the past years...celebrate your small wins too

but my mates are doing better

they are not you ... you are chidera ...you are your own kind of amazing ...you are your own kind of better...you are somebodys reason to remain motivated...you are someones reason to not loose hope...think of the lives you would affect when you eventually get what you seek
i know you chidera because you are me ...you always strive to be the best at everything you do... i believe in you too..dont compare yourself with your mates ...learn from them ... tbh you are doing well too...you just cant see it and it pains me

you think this

of course i do...you rise above all challenges you face to be the best everytime...i belive in you chidera...you just got to put in work..dont skip any process ....the path is a daunting one but what GOd has written over your live would surely manifest 

now self chidera what do you need to do to be the best....to see your dreams get actualized 

1. dont shy away from opportunities
2.manage my time properly
3. make new friends and stop being socially awkward
4. make consiuous efforts in achieving your dreams
5. accept the place of God in your live....I am nothing without him...i belive in him and i believe he wants the best for me
6. network network network
7be happy...love everyone...everyone deserves fair treatment...irrespective of status and class..see the gem in people and cultivate it
8; do what you got to do when you got to do it...leave nothing for later....
9.be organized 
10.love yourself chidera...you are doing great  



i had a tlk with myself on the 7th of october 2020 ...hope my dreams get achieved ...hope to remain commited to the cause..lord in heaven help.. im ready to work as you instructed ...pls multiply my fruits i just want to make my family happy...thank you''')


print(frequencies)
