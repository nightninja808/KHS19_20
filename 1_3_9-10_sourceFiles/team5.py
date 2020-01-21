####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Eagle' # Only 10 chars displayed.
strategy_name = 'betray, collude, betray'
strategy_description = 'opponents history'

# Example 3. Collude but retaliate
def move(my_history, their_history, my_score, their_score):
    if len(my_history)==0: 
        return 'c'
    elif my_history[-1]=='c' and their_history[-1]=='b':
        return 'b' 
    else:
        return 'c' 
    if my_score>their_score:
        return 'c'
    else:
        return 'b'


           
