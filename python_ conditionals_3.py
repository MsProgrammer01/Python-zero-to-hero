
# لە پایتۆندا، مەرجدارەکان  بەکاردەهێنرێن بۆ ئەنجامدانی کردارە جیاوازەکان لەسەر بنەمای ئەوەی کە ئایا مەرجێکی دیاریکراو ڕاستە یان هەڵە.
# جۆرەکانی Conditional Statements
"""
لە ناو IF ئەگەر یەکەم IF کار نەکات ئەوا ئێمە لەگەڵ یەکەم Else کار دەکەین
 ئەگەر یەکەم Else کار نەکات ئێمە لەگەڵ دووەم Else کار دەکەین
"""

x = 10                        #   bnosa programing  ئەگەر 10 گەورەتر بێت لە 5
if x > 5:      # 10 >5 ?     --> rasta kawata programming  run dabet
    print("programming")         #  programming



x_2 = 3
if x_2 > 5:                      # 3 > 5 ? no
    print("i like programing")
else:
    print("i don't like programing")          # i don't like programing   ( run it)


x_3 = 15
if x_3 < 10:                        # 15 < 10 ? no
    print("x is less than 10.")
elif x_3 == 15:                     # 15 == 15 ? yes
    print("x is exactly 15.")       # x is exactly 15  (run it)
else:
    print("x is greater than 10.")


fruits = ["apple", "banana", "cherry"]    # ئەگەر لەناو میوەکاندا سێومان هەبێت
if "apple" in fruits:
    print("Apple is available.")         # Apple is available  (run it)
else:
    print("Apple is not available.")



x_4= 10
y_5= 5

if x_4 < 5:  # Outer condition         10 < 5     xalata
    if y_5 > 3:  # Inner condition     5  > 3
        print("programming")     # هیچ شتێک نیشان نادات



num1 = 10
num2= 2

if num1 > 5:                #  ئەگەر 5 < 10     yes
    if num2 > 3:           #  no       ئەگەر 3 < 2
        print("i am kurd")           # don't run it beacuse the 2nd if isn't true
    else:
        print("live in kurdistan")     # live in kurdistan  (run it)
else:
    print("other ... ")             #  chonka stepi dwam ran bwa awa lera badwawa run nabet

                                    # agar stepi 2 am halabwaya else i kotay kari dakrd