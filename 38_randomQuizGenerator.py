'''
Created on Jul 25, 2017

@author: Himanshu Ranjan
'''
# Generating random quiz file

import random

# the quiz data as a dictionary. keys are states and values are their capitals
capitals = {'Andhra Pradesh' : 'Amravathi', 'Arunachal Pradesh' : 'Itanagar', 'Assam' : 'Dispur', 'Bihar' : 'Patna',            
            'Chhattisgarh' : 'Raipur', 'Goa' : 'Panaji', 'Gujarat' : 'Gandhinagar', 'Haryana' : 'Chandigarh',
            'Himachal Pradesh' : 'Shimla', 'Jammu & Kashmir' : 'Srinagar (Summer) Jammu (Winter)', 'Jharkhand' : 'Ranchi',
            'Karnataka' : 'Bangalore', 'Kerala' : 'Thiruvananthapuram', 'Madhya Pradesh' : 'Bhopal', 'Maharashtra' : 'Mumbai',
            'Manipur' : 'Imphal', 'Meghalaya' : 'Shillong', 'Mizoram' : 'Aizawl', 'Nagaland' : 'Kohima',
            'Odisha' : 'Bhubaneshwar', 'Punjab' : 'Chandigarh', 'Rajasthan' : 'Jaipur',
            'Sikkim' :'Gangtok', 'Tamil Nadu' : 'Chennai', 'Telangana': 'Hyderabad ', 'Tripura' : 'Agartala', 
            'Uttar Pradesh' : 'Lucknow', 'Uttarakhand' :'Dehradun', 'West Bengal':'Kolkata' }

# generate 29 quiz files

for quizNum in range(35):
    # first create the quiz and answer files.
    quizFile = open('capitalsquiz%s.txt' % (quizNum+1), 'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum +1), 'w')
    
    # write out the header for the quiz
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' '*20 ) + 'State Capitals Quiz (Form %s)' % (quizNum +1))
    quizFile.write('\n\n')
    
    # shuffle the order of the states 
    states = list(capitals.keys())
    random.shuffle(states)
    
    
    # loop through all 29 states, making a question for each.
    for questionNum in range(29):
        # get right and wrong answers.
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
        
        # write the question and answer options to the quiz file.
        quizFile.write('%s. what is the capital of %s?\n' % (questionNum +1, states[questionNum]))
        quizFile.write('\n')
    
        for i in range(4):
            quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
            quizFile.write('\n')
    
        #write the answer key to a file.
        answerKeyFile.write('%s. %s\n' % (questionNum +1, 'ABCD'[answerOptions.index(correctAnswer)]))
    
    quizFile.close()
    answerKeyFile.close()