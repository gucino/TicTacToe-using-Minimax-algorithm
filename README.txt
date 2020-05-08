*******************************************************************
This code was developed for STfDS Lab 1 - Naughts and crosses coursework
as part of CM50267 Software technologies for data science module university of Bath
*******************************************************************

This code aim to implement simple AI that plays tic tac toe (Naughts and Crosses)
by using minimmiax algorithm

Minimax algorithm is used to find optimal move by assuming that the opponent plays best move
The value of +1,-1, and 0 are assigned to state where X win, O win, and draw ; respectively.

The "score" function recursively imagine the state after current state until the terminal state
in order to estimate the score of given current state.

The code was tested by letting 2 AI played against each other and refer to
this as "Perfect GAME" where the result must be a DRAW

