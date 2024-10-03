from modules.questions import ques
from modules.answers import *
from modules.options import *
import os
import subprocess
from modules.playmedia import play


def clear():
    os.system('cls')
    subprocess.call('cls', shell=True)

def main():
    clear()
    while True:
        for num in range(1,21):
            print(ques[num])
            answer = input('Your answer? (Choose the question Number or write the answer with correct spelling): ').lower()

            while not answer:
                answer = input('Enter Valid Option!: ').lower()

            while answer.isalpha():
                while answer not in word_opts:
                    answer = input('Enter Valid answer! (Answer must not be any number or blank space!): ').lower()

                clear()

                if answer == word_ans[num-1]:
                    print("Your previous answer was Correct!")

                else:
                    print("Your previous answer was Incorrect!")

                break

            while answer.isdigit():
                while answer not in num_opts:
                    answer = input('Enter Valid answer! (Answer must not be any word or blank space!): ')

                clear()

                if answer == num_ans[num-1]:
                    print("Your previous answer was Correct!")

                else:
                    print("Your previous answer was Incorrect!")

                break

            print()
            print()

        fque = input('Ready for the final question?: ')
        if fque or not fque:
            play()
            
        quizagain = input('Do you want to do the quiz again? (y/n): ').lower()

        while quizagain.replace(' ', '') not in ['y','n','yes','no'] or not quizagain:
            quizagain = input('Enter valid option: ')

        if quizagain in ['y','yes']:
            main()

        elif quizagain in ['n', 'no']:
            print('Thankyou for your attempt!')
        
        break

if __name__ == '__main__':
    main()
