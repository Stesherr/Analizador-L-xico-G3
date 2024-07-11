#Aporte Kevin Valle - Conversion Implicita -----
# def p_arithmeticExpressionCastInt(p):
#     'arithmeticExpression : STRING'
#     if p[1].isdigit():
#         try:
#             n = int(p[1].strip('"'))
#             p[0] = n
#         except ValueError:
#             print("nose")