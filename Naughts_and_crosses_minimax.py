# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 13:18:41 2019

@author: Tisana
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 19:10:59 2019

@author: Tisana
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 17:24:37 2019

@author: Tisana
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 20:00:59 2019

@author: Tisana
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 10:21:45 2019

@author: Tisana
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 12:00:29 2019

@author: Tisana
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 10:15:09 2019

@author: Tisana
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 16:11:16 2019

@author: Tisana
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 18:38:57 2019

@author: Tisana
"""



def print_state(state):
    print(state[0][0]+'|'+state[0][1]+'|'+state[0][2])
    print(state[1][0]+'|'+state[1][1]+'|'+state[1][2])
    print(state[2][0]+'|'+state[2][1]+'|'+state[2][2])




################################################################################
################################################################################
################################################################################

def score_end(state):
    def converter(position):
        if position==1:
            row=0
            column=0      
        elif position==2:
            row=0
            column=1
        elif position==3:
            row=0
            column=2        
        elif position==4:
            row=1
            column=0
        elif position==5:
            row=1
            column=1
        elif position==6:
            row=1
            column=2
        elif position==7:
            row=2
            column=0
        elif position==8:
            row=2
            column=1
        elif position==9:
            row=2
            column=2
        list=[row,column]
        return list
    
    win_position_list=[[1,4,7],
                       [2,5,8],
                       [3,6,9],
                       [1,2,3],
                       [4,5,6],
                       [7,8,9],
                       [3,5,7],
                       [1,5,9]]
    score=0
    for each_win_position in win_position_list:
        if state[converter(each_win_position[0])[0]][converter(each_win_position[0])[1]]=='x' and state[converter(each_win_position[1])[0]][converter(each_win_position[1])[1]]=='x' and state[converter(each_win_position[2])[0]][converter(each_win_position[2])[1]]=='x':
            score=1
            break
        elif state[converter(each_win_position[0])[0]][converter(each_win_position[0])[1]]=='o' and state[converter(each_win_position[1])[0]][converter(each_win_position[1])[1]]=='o' and state[converter(each_win_position[2])[0]][converter(each_win_position[2])[1]]=='o':
            score=-1
            break

    if score==0:
        for each_list in state:
            if " " in each_list:
                score=None
    return score
        



################################################################################
################################################################################
################################################################################

def play(state, row, col, mark):
     #convert to list
    state=list(state)
    state[0]=list(state[0])
    state[1]=list(state[1])
    state[2]=list(state[2])
    
    state[row][col]=mark
    
    #convert back to tuple
    state[0]=tuple(state[0])
    state[1]=tuple(state[1])
    state[2]=tuple(state[2])    
    state=tuple(state)
    
    return state
    





################################################################################
################################################################################
################################################################################

def moves(state):

    
    posible_move_list=[]
    for each_row in range(0,3):
        for each_column in range(0,3):
            if state[each_row][each_column]==" ":
                posible_move_list.append((each_row,each_column))
    return posible_move_list
    


################################################################################
################################################################################
################################################################################

################################################################################
################################################################################
################################################################################
def score(current_state,current_player):

    

    def simplify_choice(any_list,player,outcome_list=[],layer=0):
        
        list=[]
        for each_item in any_list:
    
                
        
            if type(each_item)==int:
                list.append(each_item)
              
            
            else:
                if player=="x":
                    player="o"
                else:
                    player="x"   
              
                score=simplify_choice(each_item,player,outcome_list,layer=layer+1)
                if player=="x":
                    player="o"
                else:
                    player="x"  
               
                
              
                list.append(score)
        
        if player=="x":
            score=max(list)
        else:
            score=min(list)
    
        if layer==0:
       
            return list
        return score  
        
    
    def score_list(current_state, current_player):
        """Given the game state and whose turn it is returns a tuple (estimated game score, best move to play)"""
        

        def repeat_function(current_state,current_player,layer,choice,func_list=[]):
            
         
            possible_move_list=moves(current_state)
          
            rev=0
            for each_possible_move in possible_move_list:
                rev=rev+1
                if layer==1:
                    
                    choice=choice+1
                   
                 
                
           
                recover_state=current_state
                recover_player=current_player
                current_state=play(current_state,each_possible_move[0],each_possible_move[1],current_player)
        
             
                end_score=score_end(current_state)
                if end_score!=None:
                  
                    current_state=recover_state
                    current_player=recover_player
                  
                    
                    func_list.append(end_score)
                    
                   
                    
                    if rev==len(possible_move_list): #must do all possible move to get back
                        return func_list
    
                    #EXITTTTTTT
                    
                else:
                   
                    if current_player=="x":
                        current_player="o"
                    else:
                        current_player="x"
               
                    layer=layer+1
                  
                   
                    
                    list=repeat_function(current_state,current_player,layer,choice,func_list=[])
                    
    
                    
                   
                    func_list.append(list)
                   
                    
                    layer=layer-1
                 
                   
                    current_state=recover_state
                    current_player=recover_player
    
                    
                    
                   
                    if rev==len(possible_move_list):
                        return func_list
        
        
        
        
        
        
        
        
        layer=1
        choice=0  
        score_list=repeat_function(current_state,current_player,layer,choice,func_list=[])
        
        return score_list
    
    
    score_list=score_list(current_state, current_player)
    current_possible_move_list=moves(current_state)
   
    simple_choice_list=simplify_choice(score_list,current_player)
    
    if current_player=="x":
        index_of_best_choice=simple_choice_list.index(max(simple_choice_list))
    else:
        index_of_best_choice=simple_choice_list.index(min(simple_choice_list))
    best_move=current_possible_move_list[index_of_best_choice]
    score=simple_choice_list[index_of_best_choice]
    return score,best_move,current_possible_move_list,score_list


################################################################################
################################################################################
################################################################################

current_state=((' ',' ',' '),(' ',' ',' '),(' ',' ',' '))
current_player="x"
#x=score(current_state,current_player)


print_state(current_state)
i=0
while True:
  
    i=i+1

    
    #find best move for this player



    best_move_tuple=score(current_state,current_player)[1]
    
    current_state=play(current_state,best_move_tuple[0],best_move_tuple[1],current_player)
    print("")
    print_state(current_state)
    print("")
    
    #check end condition
    end_score=score_end(current_state)
    if end_score==None:
        #switch player
        if current_player=="x":
            current_player="o"
        else:
            current_player="x"
    else:
        #END GAME
        if end_score==1:
            print("X WIN")
        elif end_score==-1:
            print("O WIN")
        else:
            print("DRAW")
        break
