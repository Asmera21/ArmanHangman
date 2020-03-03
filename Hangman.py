wordBank ['sahib', 'water', 'pine', 'physics', 'mouse', 'rhyme', 'history', 'committee', 'keyboard', 'calabresi', 'anir', 'flag', 'test', 'break', 'perpendicular', 'cosine']


def initialize():
    
    space = "__ "
    
    print("Start guessing")
    
    print(space) * len(word)
    
    
  
def getLetter():
    
    letter = raw_input("What is your first guess? ")
    global letter
    
    letterList = []
    
    global letterList
    
    letterList.append(letter)

    
        
        
        
            
def checkIfWon():
                 
        if len(letterList) == len(word):
            
            print("You win yay")
            
        else:
            
            getLetter()
                            
                               
                                  
def main():
    
    initialize()

    getLetter()
    
    checkIfWon()
    
main()


def check():
    global updatedSpaces
    global lives
    global letter
    for x in range(0, int(wordLen)):
        if letter == wordList[x]:
            updatedSpaces[x] = wordList[x]
            print(updatedSpaces)
            print("You have:   ", lives, "   lives left!")
            checklist = "".join(updatedSpaces)
            master = "".join(wordList)
            if checklist == master:
                print("Congrats you solved the word!    ")
                #break
            else:
                getLetter()
        else:
            lives -= 1
            if lives != 0:
                print("You have:  " + str(lives) + "  lives left!")
                print(updatedSpaces)
                getLetter()
            else:
                print("Game Over   ")
                
 
                                                                                                      