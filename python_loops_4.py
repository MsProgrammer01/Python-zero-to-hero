""""
لە پایتۆندا، لوپەکان بەکاردەهێنرێن بۆ جێبەجێکردنی کۆد بە دووبارە و سێبارە،
 یان بۆ ژمارەیەکی دیاریکراوی جار یان لە کاتێکدا کە مەرجێک ڕاستە
"""

# for loop

"""
بەکاردێت بۆ دووبارەکردنەوە لەسەر زنجیرەیەک (وەک لیست، توپڵ،dictionary، set....) یان range of numbers

"""



singers= ['hasan zirak', 'mamle', 'chopy fatah']     # ئێمە لیستێکمان هەیە ناوی گۆرانیبێژ

for singer in singers:               # لوپەکە لە ڕێگەی هەر element ێکی ناو لیستی گۆرانیبێژەکانەوە دووبارە دەبێتەوە.
    print(singer)                    # لەجیاتی ئەوەی سێجار پرێنت بنوسین بوو  نیشاندانی ناوی گورانیبێژەکان ،
                                     # لەرێگەی لوپێکەوە یێکجار دەینوسین و ناوی هەموو گورانیبێژەکان دەنوسێت

# hasan zirak
# mamle
# cherry


for my_num in range(5):      #  range (5) --> 0 1 2 3 4
    print(my_num)

"""
0
1
2
3
4
"""

for num in range(5):      #  range (5) --> 0 1 2 3 4
    print(num**2)

"""
0
1
4
9
16
"""


for num_2 in range(10):      #  range (5) --> 0 1 2 3 4 5 6  7 8 9
    if num_2 == 5:
        break             # ئەگەر ئەو ژمارانەی کە لەناو Range دان یێکسانبن بە 5 ئەوا یێکسەر لوپەکە بوەستێنە
    print(num_2)       # Prints 0 to 4
#0
#1
#2
#3
#4


for num_2 in range(5):         #  range (5) --> 0 1 2 3 4 5 6  7 8 9
    if num_2 == 2:
        continue
    print(num_2)               # ئەگەر  ئەو ژمارانەی کە لەناو Range دان یێکسانبن بە 2 ئەوا ژمارە دوو مەنوسە دواتر بەردەوام بە
#0
#1
#3
#4



#  کۆدێک دووبارە دەکاتەوە بە مەرجێک  ڕاست بێت.

num_3 = 1                # tanha jari yekam deta era dwatr har badway while da dasoretawa tawako marjaka hala dabet .
while num_3 <= 5:       # 1<=5?yes 2<=5?yes 3<=5?yes 4<=5?yes 5<=5?yes 6<=5?no
    print(num_3)
    num_3 += 1          # 1+1=2  2+1=3  3+1=4 4+1=5 5+1=6  stop

#1
#2
#3
#4
#5



colors = ['red', 'green']
items = ['car', 'bike']
for color in colors:
    for item in items:                    # nested loop
        print(color, item)
"""
1st  loop
red 

2nd loop
car , bike 

1st loop
green 

2nd loop
car bike


red car
red bike
green car
green bike

"""


miwa = ['sew', 'hanar', 'kiwi', 'prtaqal']
for pit in miwa:
    if 'a' in pit:  # Check if 'a' is in the word
        print(f"' lanaw {pit}' piti 'a' haya ")

#' lanaw hanar' piti 'a' haya
#' lanaw prtaqal' piti 'a' haya