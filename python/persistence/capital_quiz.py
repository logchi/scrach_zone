import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico':
   'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia':
    'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


for num in range(1, 35+1):
    quizFile = open('quizFile%s.txt' % num, 'w')
    answerFile = open('answerFile%s' % num, 'w')

    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write('State Capitals Quiz (Form %s)\n\n' %  num)

    states = list(capitals.keys())
    random.shuffle(states)
    for q_num in range(50):
        state = states[q_num]
        correct_answer = capitals[state]
        wrong_answers = list(capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        option_answers = random.sample(wrong_answers, 3)
        option_answers.append(correct_answer)
        random.shuffle(option_answers)

        quizFile.write('%s. What is the capital of %s?\n' % ((q_num+1), state))
        orders = 'ABCD'
        for i in range(4):
            quizFile.write('\t%s. %s\n' % (orders[i], option_answers[i]))
        quizFile.write('\n')
        answerFile.write('%s. %s\n\n' % ((q_num+1), orders[option_answers.index(correct_answer)]))

    quizFile.close()
    answerFile.close()
