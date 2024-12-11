 # python Function


 # فەنکشنی پایتۆن بلۆکێکی کۆدە کە دەتوانرێت دووبارە بەکاربهێنرێتەوە و ئەرکێکی دیاریکراو ئەنجام دەدات.
 # فەنکشنەکان یارمەتی ڕێکخستنی کۆدەکان دەدەن بۆ بەشە لۆژیکیەکان،
  # ئەمەش تێگەیشتن و پاراستن و دووبارە بەکارهێنانەوە ئاسانتر دەکات


def my_function(parameter1, parameter2):    #فەنکشنێک بە بەکارهێنانی وشەی سەرەکی def پێناسە دەکرێت و دواتر ناوی فەنکشن
    # Function body
    result = parameter1 + parameter2
    return result



def greet(name):
    print(f"slaw {name}")

greet("firdaws")     # "slaw firdaws"

# chon kar dakat?
# 1 def greet(name)  2-print(f"slaw {name}") 3-(greet("firdaws")



def add(a, b):               # a=5 b=3
    return a + b

result = add(5, 3)
print(result)                   #8

# chon kar dakat ?
# 1-def add(a, b)  2-result = add(5, 3)  3-return a + b  4-result = add(5, 3)  5-print(result)



def example():
    local_var = 10     # awa local varible a, aw variblanay lanaw function ta3rif dakren
    print(local_var)

example()    #10

# chon kar dakat ?
# 1- def example()  2-local_var=10  3-print(local_var)  4-example()




def greet(name="firdaws"):
    print(f"naw : {name}")

greet()   # naw :firdaws
greet("Azad")   # naw : Azad


#chon kardakat ?
# 1-def greet(name="firdaws") 2-print(f"naw : {name}")  3-greet()  4-greet("Azad")




add = lambda x, y: x + y                 #فەنکشنی بچووک و بێناون کە بە بەکارهێنانی وشەی سەرەکی لامبدا پێناسە کراونlambda .
print(add(3, 5))  #  8


# chon kar dakat?
#1-lambda x, y: x + y   2-add  3-add(3, 5)   4-print(add(3, 5))  (prenting)




def factorial(num):               #ئەو کێشانە بەسوودە کە دەتوانرێت دابەش بکرێن بۆ کێشەی لاوەکی بچووکتر
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(5))  #  120        # 5 * 4 * 3 * 2 * 1 = 120


# chon kardakat ?
# 1-def factorial(num)   2-if num == 1   3-else: return num * factorial(num-1)  4-factorial(5):
