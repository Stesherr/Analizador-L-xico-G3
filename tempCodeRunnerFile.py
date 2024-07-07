def p_stringConcatenation(p):
    """stringConcatenation : value CONCAT value SEMICOLON
                           | value CONCAT stringConcatenation
                           | stringConcatenation CONCAT value SEMICOLON
    """