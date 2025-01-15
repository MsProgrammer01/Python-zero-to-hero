

# (OOP) چییە؟
#  پارادایمێکی بەرنامەسازییە کە کۆد لە دەوری شتەکان و کارلێکەکانیان ڕێکدەخات.
#  ئۆبجێکتی یەکەیەکی جیهانی ڕاستەقینە، وەک ئۆتۆمبێل، کەسێک، یان ئەژمێری بانکی، کە بە کۆد مۆدێل کراوە.
#  شتەکان لە پۆلەکانەوە دروست دەکرێن، کە وەک نەخشە کاردەکەن.

""""
بۆچی OOP بەکاربهێنرێت؟
مۆدیۆلاریتی: کۆد دابەشکراوە بەسەر پێکهاتەی بچووکتر و دووبارە بەکارهێنەرەوە.
دووبارە بەکارهێنانەوە: دەتوانرێت پۆلەکان و شتەکان لە سەرانسەری بەرنامەکاندا دووبارە بەکاربهێنرێنەوە.
توانای گەورەکردن: بەڕێوەبردنی سیستەمی گەورە و ئاڵۆز بە ئاسانی.
پاراستن: کۆدی ڕێکخراو و ئاسان بۆ نوێکردنەوە.
Encapsulation : داتاکان دەپارێزێت بە سنووردارکردنی دەستگەیشتن.

"""


"""
چەمکە سەرەکییەکان
پۆل: نەخشەیەک بۆ دروستکردنی شتەکان. class
object ئۆبجێکتی: نموونەیەکی پۆلێکە.
تایبەتمەندییەکان: ئەو گۆڕاوانەی کە سەر بە پۆلێک/ئۆبجێکتە.Attributes
Methods شێوازەکان: ئەو ئەرکانەی کە سەر بە پۆلێک/ئۆبجێکتە. 
TB:function yan method haman shtn .


"""


# class
# پۆلێک پێکهاتە و هەڵسوکەوت (تایبەتمەندی و شێوازەکان)ی ئۆبژێکت پێناسە دەکات.

# Constructor چییە؟  __init__
#شێوازی __init__ شێوازێکی تایبەتە لە پایتۆن کە کاتێک ئۆبجێکتی دروست دەکرێت بە شێوەیەکی ئۆتۆماتیکی بانگ دەکرێت.
# بەکاردێت بۆ دەستپێکردنی تایبەتمەندییەکانی شتەکە


class Person:
    def __init__(self, name, age):     # def --> method
        self.name = name              # Assign values to instance attributes
        self.age = age


p1 = Person("firdaws",22)   # Creating objects
p2 = Person("Abdulla", 50)  #  Call the method

print(p1.name, p1.age)  # firdaws 22
print(p2.name, p2.age)  #  Abdulla 50


#چۆن کاردەکات
#  1-class Person  2-def __init__(self, name, age):  3- self.name = name  4-self.age = age  5-p1  6-p2 7-print






class Animal:                # aw class a paywandi ba classakay sarawa nya yani natwani data lanawbaynyan bgwazyawa
    gyanawar = "Azhell"        # class attribute   ta3rifkrdn la daraway function pey dawtre class atribute

    def __init__(self, type, name):   # __init__ is the constructor method
        self.type = type             # Instance attribute      ta3rifkrdn lanaw function yan method
        self.name = name             # Instance attribute       واتە تایبەتن بە هەر ئۆبجێکتی پۆلەکە


dog = Animal("sagi harir", "gdo")    # dog is a object

print(dog.gyanawar)      # accessing Class Attribute
print(dog.type)       # Accessing Instance Attribute
print(dog.name)       # accessing Instance Attribute

#Azhell
#sagi harir
# gdo


# Class Attribute:
# هەر ئۆبجێکتی پۆلەکە دەتوانێت دەستی پێ بگات، بەڵام بەهاکەی بۆ هەموو نموونەکان وەک یەکە مەگەر بە ڕوونی دەستکاری نەکرێت.
# Instance Attributes:
# هەر ئۆبجێکتی دەتوانێت بەهای جیاوازی هەبێت بۆ ئەم سیفەتانە


"""
لە پرۆگرامسازیدا هەندێک وشەمان هەیە بە ئینگلیزی ئێمە ناتوانین بە کوردی بڵێین , 
باشترە لە ئینگلیزی چونکە ئینگلیزی ستانداردە لە هەموو شوێنێک بۆ فێربوون لەگەڵ کەسانی تر ,
 هەوڵدەدەم زۆرترین بە زمانی کوردی بنووسم بەڵام بۆ هەندێک وشە بە ئینگلیزی باشە .

"""










