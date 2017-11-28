
data ={  # this will contain the quizes, their answers, and the number of failures
    'easy':{
        'quiz':
    ''' A careful analysis of the teacher-student relationship at any level,
inside or outside the school, reveals its fundamentally ___1___ character.
This relationship involves a narrating Subject (the ___2___) and patient,
listening objects (the ___3___). The contents, whether values or empirical
dimensions of reality, tend in the process of being narrated to become ___4___
and petrified. Education is suffering from narration sickness.''',
        'answers':['narrative', 'teacher', 'students', 'lifeless'],
        'failures': 5
    },
    'medium':{
        'quiz':
        ''' Education thus becomes an act of depositing, in which the students are
the ___1___ and the teacher is the ___2___. Instead of communicating,
the teacher issues communiques and makes deposits which the students patiently
receive, memorize and repeat. This is the "___3___" concept of education, in
which the scope of action allowed to the students extends only as far as
receiving, filing, and storing the ___4___. They do, it is true, have the
opportunity to become collectors or cataloguers of the things they store.
But in the last analysis, it is the people themselves who are filed away
through the lack of creativity, transformation, and knowledge in this
(at best) misguided system. ''',
        'answers':['depositories', 'depositor', 'banking', 'deposits'],
        'failures': 3
    },
    'hard':{
        'quiz':'''True generosity consists precisely in fighting to destroy the causes
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
        violence, ___5___lessness even when clothed in false generosity. ''',
        'answers':['charity', 'work', 'oppressed', 'chance', 'love'],
        'failures': 1
    }
}


def select_level():
    # prompts the user to choose easy, medium, or hard
    # the returned difficulty will be used by the play() function.
    while True:
        difficulty = raw_input('Choose a difficulty: (easy / medium / hard)\n').lower()
        if difficulty in data:  # the first terms in data are easy/medium/hard
            print "\n You asked for it; here's the " + difficulty + " quiz: \n"
            return difficulty
        print 'Incorrect difficulty! Try again!'


def play(difficulty):
    # input: difficulty from select_leve()
    # output: the number of remaining chances to make a mistake.
    quiz = data[difficulty]['quiz']  # from suggested data dictionary
    chances = data[difficulty]['failures'] # from suggested data dictionary
    print "You can pass this quiz with up to " + str(chances) + " mistakes"
    answered = 0
    while answered < len(data[difficulty]['answers']) and chances >= 0:
        print quiz # show blanks and completed in the same print
        answer = raw_input('Fill in the __' + str(answered + 1) + '__\n').lower()
        if answer == data[difficulty]['answers'][answered]:
            print "Correct!"
            quiz = quiz.replace("___" + str(answered + 1) + "___",
                data[difficulty]['answers'][answered])
            answered = answered + 1
        else:
            print "Try again! You have " + str(chances) + " chance(s) left this quiz"
            chances = chances - 1
    return chances

def closing(chances):
    # input: the number of remaining chances at the end of a quiz
    # prints the results: "Try again" for <0 chances,
    # "Good job" otherwise.
    if chances < 0:
        print '''   Make sure you review what you missed!
Then come back soon for another challenge!'''
    else:
        print '''   You must have learned this well.
Looks like you're ready for a new challenge!'''



closing(play(select_level()))  # is this a fine way to put everything together?
