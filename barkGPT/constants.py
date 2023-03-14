
BASELINE_MESSAGES = [
    '''
    Here is a python api doc for a quadruped robot called Pupper that resembles a real dog. Each line starting with `def` is a n api function call, whose function is intuitive from its name and the comments a line above.
    
    ''',
    '''
    For each following input, I'll give you a command to make pupper do something.
    Based on this doc, decompose the action into function calls, and output them in a python script.
    No extra comments or explanations are needed.
    ''',
    '''
    As much as you can, make pupper act as a real dog would do. Let it be active and vital
    ''',
    '''
    in a python script, compose more higher-order api calls (more than 15) that resembles and abstract actual dog motions, including but not limited to: drooling, shaking, scratching, sniffing, licking, etc.
    '''
]