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
    
 
                                                                                                      