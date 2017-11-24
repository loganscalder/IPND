
import time  # I want to wait a second before sharing the results of the quiz
def blank_in_word(word, blanks):
    # checks to see if any blank in 'blanks' is in word
    # returns the corresponding blank in 'blanks' or None
    for blank in blanks:
        if blank in word:
            return blank
    return None

def opening():
    # This is used to open the test.
    # Asks the user for a difficulty level (easy, medium, hard)
    # outputs the difficulty chosen (as a string)
    # the output will be used to choose the quiz given
    greeting = '''\n \n \n \nWelcome to the quiz!
This quiz will test your memorization of select quotes by Paulo Freire
The quiz will allow for five mistakes before redirecting you.
\n \n \n \n'''
    print greeting
    prompt = "Choose your difficulty! (easy, medium, hard):  "
    user_input = raw_input(prompt)
    print "\n" + user_input + " quiz: \n"
    return user_input

def closing(score):
    # input: score (0-5)
    # if score >0, student passed the quize
    # if score == 0, student didn't pass
    time.sleep(1.7)  # I want to wait a second...
    if score >0:
        print "Hey, you passed"
        if score == 5:
            print '''   You must have learned this well.
    Looks like you're ready for a new challenge!'''
        else:
            print '''   Make sure you review what you missed!
    Then come back soon for another challenge!'''
    else:
        print '''   Good Try!
        Keep on studying and you'll learn what you need!'''
    print '''
    Thanks for playing. To report an error, email Logan '''

def fill_in_the_blanks():
    # This funciton will take no input.
    # it is meant to be played interactively in the command line
    # It will first ask the user for the desired level of Difficulty
    # then it will show the corresponding quiz and ask for an answer
    # to the first blank.
    # Each quiz will have atleast four unique blanks and allow for five
    # incorrect answers before ending the quiz.
    quizes = {
    'easy':
    '''A careful analysis of the teacher-student relationship at any level,
inside or outside the school, reveals its fundamentally ___1___ character.
This relationship involves a narrating Subject (the ___2___) and patient,
listening objects (the ___3___). The contents, whether values or empirical
dimensions of reality, tend in the process of being narrated to become ___4___
and petrified. Education is suffering from narration sickness.''',
    'medium':
    '''Education thus becomes an act of depositing, in which the students are
the ___1___ and the teacher is the ___2___. Instead of communicating,
the teacher issues communiques and makes deposits which the students patiently
receive, memorize and repeat. This is the "___3___" concept of education, in
which the scope of action allowed to the students extends only as far as
receiving, filing, and storing the ___4___. They do, it is true, have the
opportunity to become collectors or cataloguers of the things they store.
But in the last analysis, it is the people themselves who are filed away
through the lack of creativity, transformation, and knowledge in this
(at best) misguided system. ''',
    'hard':
    '''True generosity consists precisely in fighting to destroy the causes
    which nourish false ___1___. False ___1___ constrains the fearful and
    subdued, the "rejects of life" to extend their trembling hands. True
    generosity lies in striving so that these hands - whether of individuals
    or entire peoples - need be extended less and less in supplication, so
    that more and more they become human hands which ___2___ and, ___2___ing,
    transform the world. This lesson and this apprenticeship must come,
    however, from the ___3___ themselves and from those who are truly in
    solidarity with them. As individuals or as peoples, by fighting for the
    restoration of their humanity they will be attempting the restoration of
    true generosity. Who are better prepared than the ___3___ to understand
    the terrible significance of an oppressive society? Who suffer the effects
    of oppression more than the ___3___? Who can better understand the
    necessity of liberation? They will not gain this liberation by ___4___ but
    through the praxis of their quest for it, through their recognition of
    the necessity to fight for it. And this fight, because of the purpose
    given it by the oppressed, will actually constitute an act of ___5___
    opposing the ___5___lessness which lies at the heart of the oppressors'
    violence, ___5___lessness even when clothed in false generosity. '''
    }
    blanks = ["___1___", "___2___", "___3___", "___4___", "___5___"]
    easy_answers = ["narrative", "teacher", "students", "lifeless"]
    medium_answers = ["Depositories", "Depositor", "banking", "deposits"]
    hard_answers = ["charity","work", "oppressed", "chance", "love"]
    keys = {   # a question and answer key for easy access I think
    'easy':dict(zip(blanks,easy_answers)),
    'medium':dict(zip(blanks,medium_answers)),
    'hard':dict(zip(blanks,hard_answers))
    }

    difficulty = opening()
    quiz = quizes[difficulty]
    key = keys[difficulty]
    print quiz
    score = 5  # 5 chances for a wrong answer
    split_quiz = quiz.split()
    #print split_quiz
    for word in split_quiz:
        user_input = ""
        blank = blank_in_word(word, blanks)
        if blank != None:
            user_input = raw_input(blank + "?"*score + " ")
            while score >0: # if the score is greater than zero, they can get another chance
                while user_input.lower() != key[blank].lower():
                    if score <= 0:
                        break
                    score = score -1
                    print '''Maybe...
but my answer key says something different
Try again...'''
                    user_input = raw_input(blank + "?"*score + " ") # prompted with another chance
                if user_input.lower() == key[blank].lower():
                    print '''NICE! We got the same answer'''
                    quiz = quiz.replace(blank, key[blank],1)
                    print quiz
                    break
        if score <= 0:
            break
    closing(score)



fill_in_the_blanks()

data = {
    'easy': {
        'phrase': 'Easy __1__  .  __2__ .  __3__  .   __4__ .',
        'answers': ['one_easy', 'two_easy', 'three_easy', 'four_easy'],
        'failures': 5
    },
    'medium': {
        'phrase': 'Medium __1__  .  __2__ .  __3__  .   __4__ .',
        'answers': ['one_medium', 'two_medium', 'three_medium', 'four_medium'],
        'failures': 2
    },
    'hard': {
        'phrase': 'Hard__1__  .  __2__ .  __3__  .   __4__ .',
        'answers': ['one_hard', 'two_hard', 'three_hard', 'four_hard'],
        'failures': 0
    }
}
print data
