import requests
import html

class Question:
    def __init__(self, category, questionStr, correctAnswerFlag):
        self.category = category
        self.questionStr = questionStr
        self.correctAnswerFlag = correctAnswerFlag

class Quiz:
    def __init__(self, numQuestions):
        self.apiUrl = "https://opentdb.com/api.php?difficulty=easy&type=boolean&amount="
        self.numQuestions = numQuestions
        self.questionsList = []
        self.loadQuestions(numQuestions)


    def loadQuestions(self, numQuestions):
        response = requests.get(self.apiUrl + str(numQuestions))

        if response.ok : 
            #print(response.json())
            data = response.json()
            results = data["results"]

            for q in results:
                category = q["category"]
                questionType = q["type"]
                difficulty = q["difficulty"]
                questionStr = html.unescape(q['question'])
                
                
                correctAnswerFlag = q["correct_answer"].lower() in ['true', '1', 'yes']
                

                qObj = Question(category, questionStr, correctAnswerFlag)
                self.questionsList.append(qObj)

    def startQuiz(self):
        print("\nWelcome in Ma' Quiz, bitches!\n")
        numCorrectUserAnswers = 0
        
        n=0
        numQuestions = len(self.questionsList)

        while (n < numQuestions):
            q = self.questionsList[n]
            print(f"Question number {str(n)}: {q.questionStr}")
            #print(f"Answer flag: {q.correctAnswerFlag}")

            answer = input("Give correct answer as y/n: ")
            answerBool = False
            if answer == 'y': answerBool = True

            if answerBool == q.correctAnswerFlag:
                print("\n\nCorrect, bitch!\n\n")
                numCorrectUserAnswers += 1

            else:
                print("\n\nYou wrooong, bitch! \n Try again!\n\n")

            n += 1
        
        if  numCorrectUserAnswers >= 8:
            print(f"You nailed {numCorrectUserAnswers} out of {len(self.questionsList)}. You rock...bitch!")
        
        elif numCorrectUserAnswers >= 4:
            print(f"You got {numCorrectUserAnswers} out of {len(self.questionsList)} questions right. \n Wanna play again?")
        
        elif numCorrectUserAnswers <5:
            print(f"You only answered {numCorrectUserAnswers} out of {len(self.questionsList)} correctly. You dumb or wat? \n\n ...Wanna play again?") 


quiz = Quiz(10)
quiz.startQuiz()