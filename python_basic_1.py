
#print
# ئەمە فەنکشنێکی Built-in ە کە دەتوانیت ئەنجامەکان ببینیت بە بەکارهێنانی Print

print("Hello, World!")    #Hello, World!
print (1)                  # 1



# Varible و Data Type لە پایتۆندا

"""
1- Varible لە پایتۆندا 

گۆڕاو بریتییە لە دەفرێک بۆ هەڵگرتنی بەهاکانی داتاData value 
 لە پایتۆندا، پێویست ناکات جۆری گۆڕاوێک هەڵبژێریت؛
  بە شێوەیەکی ئۆتۆماتیکی دیاری دەکرێت.
  
  . یاساکانی ناونانی گۆڕاوەکان
ناوی گۆڕاوەکان تەنها دەتوانێت پیت و ژمارە و هێڵی ژێرەوە (_) لەخۆبگرێت.
دەبێت بە پیت یان هێڵی ژێرەوە دەست پێبکەن بەڵام ناتوانن بە ژمارەیەک دەست پێبکەن.
ناوی گۆڕاوەکان هەستیارن بە گەورە و بچووک (تەمەن و تەمەن جیاوازن).
ناوی وەسفکەر بەکاربهێنە بۆ خوێندنەوەی باشتر.

"""

age = 25                  #age --> varible
                          #25 --> value
Age=32
_name = "Alice"
total_marks = 95

#2name = "John"             # ناتوانرێت بە ژمارەیەک دەست پێبکات
#total-marks = 90           # هێڵکاری ڕێگەپێدراو نییە(-)

x = 10         # Integer  x گۆڕاوێکە     integer واتە ژمارەکان
y = "Hello"    # String   y گۆڕاوێکە     string بە واتای دەق یان ڕستە یان وشە دێت
yy = "5"        # String   y گۆڕاوێکە     string بە واتای دەق یان ڕستە یان وشە دێت
z = 3.14       # Float    z گۆڕاوێکە     float واتە ژمارەی خاڵەکان

"""
2- Data type لە پایتۆن
جۆری داتا لە بەرنامەسازیدا جۆری بەهاکە دیاری دەکات کە گۆڕاوێک دەتوانێت هەڵیبگرێت.
 لە پایتۆندا هەموو بەهایەک سەر بە جۆرێکی داتا تایبەتە و
  ئەمەش دیاری دەکات کە چ کارێک دەتوانرێت لەسەر ئەو بەهایە ئەنجام بدرێت.

جۆری دەق: string
جۆرە ژمارەییەکان: int، float، complex
جۆرەکانی زنجیرە: list, tuple, range
جۆری نەخشەسازی: dict
جۆرەکانی کۆمەڵە: set, frozenset
جۆری بولی: bool
جۆرەکانی دووانەیی: bytes, bytearray, memoryview
"""

x_1 = "Hello World"	                           #string
x_2 = 20                                         #int
x_3= 20.5	                                   #float
x_4 = 1j	                                    #complex
x_5=["apple", "banana", "cherry"]	           #list
x_6= ("apple", "banana", "cherry")	           #tuple
x_7= range(6)	                                #range
x_8= {"name" : "kale", "age" : 36}               #dict
x_9= {"apple", "banana", "cherry"}	            #set
x_10= frozenset({"apple", "banana", "cherry"})	#frozenset
x_11= True	                                     #bool
x_12= b"Hello"	                                 #bytes
x_13= bytearray(5)                                # bytearray
x_14= memoryview(bytes(5))	                    #memoryview

print(x_3)            # 20.5


"""
INT 

تێگەیشتن لە int جۆری داتا لە پایتۆن

جۆری داتاکانی int لە پایتۆن بەکاردێت بۆ نوێنەرایەتیکردنی ژمارە تەواوەکان (ژمارە تەواوەکان).
 یەکێکە لە جۆرە ژمارەییەکان کە زۆرترین بەکارهێنانی هەیە لە بەرنامەسازی پایتۆندا.
 
 جۆری int هەردوو ژمارەی ئەرێنی و نەرێنی لەخۆدەگرێت، لەوانەش سفر.
"""

x_int = 10      # ژمارەیەکی تەواو ئەرێنی
y_int = -15     #ژمارەیەکی تەواو نەرێنی
z_int= 0       # سفر
largest_int= 12345678901234567890  # گەورەترین ژمارەی تەواو

print(z_int)      #0


"""
String
 بریتییە لە زنجیرەیەک لە کاراکتەرەکان کە لە ناو یەک (') یان دوو (") کۆت داخراون.
  یەکێکە لە جۆرە داتا هەرە گشتگیرەکان و بەکارهێنراوترین جۆرەکانی داتا لە پایتۆندا.
  
"""

single_quote = 'Hello'
sting_double_quote = "Hello"
string_double_quote_characrer = "A"
string_double_quote_number = "3"

print(string_double_quote_number)    #3


"""

float
فلۆت جۆرێکی داتایە کە نوێنەرایەتی ژمارە دەهەمیەکان یان ژمارە ڕاستەقینەکان دەکات.
 فلۆتەکان بۆ نوێنەرایەتیکردنی ئەو ژمارانە بەکاردەهێنرێن کە بە خاڵێکی دەهەمی دەنووسرێن.
"""

x_float = 20.5    # فلۆتێکی ئەرێنی
y_float = -3.14   # فلۆتێکی نەرێنی
z_float = 0.0001  # فلۆتێکی زۆر بچووکە

print(z_float)             #0.0001



"""

Complex
لە پایتۆندا 1j بەکاردێت بۆ نیشاندانی ژمارەیەکی ئاڵۆز 
 ژمارە ئاڵۆزەکان ئەو ژمارانەن کە هەم بەشێکی ڕاستەقینە و هەم بەشێکی خەیاڵییان هەیە.
 
 
 ژمارە ئاڵۆزەکان لە پایتۆندا

بەشی ڕاستەقینە: ژمارەی ڕاستەقینە (بۆ نموونە 3 لە 3 + 4j).
بەشە خەیاڵی: بەشە خەیاڵییەکە، کە چەند هێندەیەکی j یە (بۆ نموونە 4j لە 3 + 4j ). 


ڕستەسازی  ئاڵۆز لە پایتۆن:

ژمارەیەکی ئاڵۆز بە شێوەی a + bj دەنووسرێت، کە:
a بەشە ڕاستەقینەکەیە.
ب بەشی خەیاڵییە

"""

x_complex= 1j
a_complex = 3 + 4j
b_complex = 1 + 2j

print(a_complex)           #(3+4j)



#list

"""
List 

لیست لە پایتۆن چییە؟
لیست بریتییە لە جۆرێکی داتاکانی پایتۆن کە لەناوەوەیە کە بەکاردێت بۆ هەڵگرتنی کۆمەڵەیەکی ڕێکخراو لە بابەتە.
 لیستەکان گۆڕاون، ئەمەش واتە دەتوانیت ناوەڕۆکەکانیان دوای دروستکردن بگۆڕیت 
 (بۆ نموونە زیادکردن، لابردنی، یان دەستکاریکردنی شتەکان).
 
 
 تایبەتمەندییە سەرەکییەکانی لیستەکان:

لە لیستەکاندا دەتوانیت دەستکاری ناوەڕۆکەکان بکەیت (شتەکان بگۆڕیت، زیاد بکەیت، یان لاببەیت).
ئیندێکس: هەر شتێک ئیندێکسێکی هەیە، لە 0ەوە دەست پێدەکات بۆ یەکەم بابەتی.
 لیستێک دەتوانێت جۆری جیاوازی داتا لەخۆبگرێت، لەوانە ژمارە تەواوەکان، ڕستە و تەنانەت لیستەکانی تر
 
"""


#         [index 0 , index 1 , index 2 ]   or
#         [index -3, index -2, index -1 ]
my_list = ["apple", "banana", "cherry"]              # apple" "banana" "cherry" --> Element بریتیە لە


print (my_list[0])   # apple

print (my_list[1])   #banana

print (my_list[2])   #cherry

print (my_list[-3])  #cherry


# "apple", "banana", "cherry"

#دەستکاریکردنی Element
my_list[1] = "orange"
print(my_list)           #['apple', 'orange', 'cherry']


#زیادکردنی Element
# append() , insert() ,extend()

my_list.append("kiwi")  # لە کۆتاییدا 'کیوی' زیاد بکە
print(my_list)          #['apple', 'orange', 'cherry', 'kiwi']

my_list.insert(2,"kiwi") #  'کیوی' زیاد بکە بۆ ئیندێکسی 2
print(my_list)                          #['apple', 'orange', 'kiwi', 'cherry', 'kiwi']

my_list.extend(["mango", "pear"])   #لە کۆتاییدا چەندین Element زیاد بکە
print(my_list)                     #['apple', 'orange', 'kiwi', 'cherry', 'kiwi', 'mango', 'pear']



# لابردنی Element
#remove() pop()  clear()

# 'apple', 'orange', 'kiwi', 'cherry', 'kiwi', 'mango', 'pear'

my_list.remove("orange")   # لابردنی Element
print(my_list)             #['apple', 'kiwi', 'cherry', 'kiwi', 'mango', 'pear']

my_list.pop(2)              #  لابردنی Element لە ئیندێکسی ٢
print(my_list)              # ['apple', 'kiwi', 'kiwi', 'mango', 'pear']

my_list.clear()              #هەموو توخمەکان لە لیستەکەدا لاببە
print(my_list)               # [ ]


# دۆزینەوەی Element
# index() count()

my_list2= ["apple", "banana", "cherry", "banana"]

print(my_list2.index("banana"))      # 1
print(my_list2.count("banana"))      #2


# پارچەکردنى list
#دەتوانیت لیستێک پارچە پارچە بکەیت بۆ ئەوەی subset لێ وەربگریت بە بەکارهێنانی [start:end].
# sub set بەشێکە لە لیستەکە

#          [    -6    ,  -5     ,  -4   ,  -3    , -2    ,  -1    ]
#          [   0      ,   1     ,  2    ,   3    ,    4  ,   5    ]
my_list3 = ["apple", "banana", "cherry", "orange", "mango", "pear"]

# list[start:end]

print(my_list3[1:4])     #['banana', 'cherry', 'orange']
print(my_list3[:3])     #['apple', 'banana', 'cherry']            [0:3]
print(my_list3[2:])      #['cherry', 'orange', 'mango', 'pear']   [2:0]
print(my_list3[-3:])     #['orange', 'mango', 'pear']             [-3:0]



# sort method and reverse
# شێوازی sort() توخمەکانی لیستێک بە ڕیزبەندی بەرزبوونەوە ڕیز دەکات بە شێوەی ئۆتۆماتیک.

fruits = ["orange", "apple", "banana", "pear", "mango"]
fruits.sort()    # بە ڕیزبەندی ئەلفوبێ ڕیز دەکرێت
print(fruits)     #  ['apple', 'banana', 'mango', 'orange', 'pear']


number = [5,7,8,3,6]
number.sort()    # بە ڕیزبەندی ژمارە ڕیز دەکرێت
print(number)     #  [3, 5, 6, 7, 8]

numbers2 = [5, 2, 9, 1, 7]
numbers2.sort(reverse=True)  # ڕیزکردنی گەورە بۆ  بچووک
print(numbers2)             #[9, 7, 5, 2, 1]

fruits = ["apple", "banana", "cherry", "date"]
fruits.reverse()     # لیستەکە پێچەوانە دەکاتەوە  Reverce
print(fruits)        # Output: ['date', 'cherry', 'banana', 'apple']

numalpha= [10,"kawa",8,"syamand",6,"ahmad"]     # دەتوانیت ژمارە و دەق لەناو لیستێکدا بنووسیت
print(numalpha)                                  #[10, 'kawa', 8, 'syamand', 6, 'ahmad']

my_numbers = [5, 2, 9, 1, 7]
my_numbers.sort()    # بە ڕیزبەندی ژمارە ڕیز دەکرێت
my_numbers.reverse()  # ڕیزکردنی گەورە بۆ  بچووک
print(my_numbers)     # [9, 7, 5, 2, 1]


#copy() - کۆپیکردنی لیستێک

car=["marcedes" ,"bugaty", "BMW"]
car2=car.copy()
car2.append("nisan")
print(car)               #['marcedes', 'bugaty', 'BMW']
print(car2)              #['marcedes', 'bugaty', 'BMW', 'nisan']

#end of list



#Tuple

"""
توپڵ لە پایتۆن چییە؟
توپڵ بریتییە لە کۆمەڵێک شتومەکی ڕێکخراو و نەگۆڕ.
 توپڵەکان هاوشێوەی لیستەکانن، بەڵام بە پێچەوانەی لیستەکانەوە،
  توپڵەکان ناتوانرێت دەستکاری بکرێن (ناگۆڕێن) دوای دروستکردنیان.
   بە شێوەیەکی گشتی بەکاردەهێنرێن بۆ گرووپکردنی داتا پەیوەندیدارەکان بەیەکەوە
    و دڵنیابوون لەوەی داتاکان بە نەگۆڕان دەمێننەوە.
    
    --ئەگەر توپڵێک شتە گۆڕاوەکانی تێدابێت (وەک لیستێک)، دەتوانرێت ئەو شتانە دەستکاری بکرێن.
    --توپڵ دەتوانێت توخمەکانی جۆری جیاوازی داتا لەخۆبگرێت، لەوانەش توپڵەکانی تر، لیستەکان، یانdictionaries  .
    
    -- بەزۆری توپڵەکان بە داخستنی توخمەکان لە نێو کەوانەدا () دروست دەکرێن
   -- بۆ لیست [ ] بەکاربهێنە
   
"""

my_tuple = (1, 2, 2, 3, 3, 3)
print(my_tuple)    #  (1, 2, 2, 3, 3, 3)

my_tuple_2= 1, 2, 3     #ئەمەش توپڵە
print(my_tuple_2)      #(1, 2, 3)

list_to_tuple = tuple([1, 2, 3])
string_to_tuple = tuple("programming")
print(list_to_tuple)                     # (1, 2, 3)
print(string_to_tuple)                   # ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g')


single_tuple = (5,)  # یەکelement  لەناو tuple دا
not_a_tuple =(5)  # تەنها ژمارەیەک لە نێو کەوانەدا

tupel_fruite= ("apple", "banana", "cherry")
print(tupel_fruite[0:2])                       #('apple', 'banana')

# in و not in
print("apple" in tupel_fruite)  #  True      ئایا سێوەکە لەناو توپڵی میوە دایە .
print("grape" not in tupel_fruite)  # True     ئایا سێوەکە لەناو توپڵی میوە نییە .

# #true واتە بەڵێ    # false واتە نەخێر

#count():
tuple_count = (1, 2, 2, 3, 3, 3)
print(tuple_count.count(2))  #  2

#index():
# یەکەم ئیندێکسی بەهایەکی دیاریکراو دەگەڕێنێتەوە

tuple_index = ("apple", "banana", "cherry","banana")
print(tuple_index.index("banana"))    # 1

#هەرچەندە توپڵەکان نەگۆڕن، بەڵام ئەگەر توپڵێک شتێکی گۆڕاو وەک لیستێک لەخۆبگرێت، دەتوانرێت شتە گۆڕاوەکە بگۆڕدرێت

#            ( ,  [0 , 1], )        # Secound
#            (0,    1   , 2)        # First
list_tuple = (1, [2 , 3], 4)
list_tuple[1][0] = 99
print(list_tuple)         # (1, [99, 3], 4)     # la shweni zhmara 2 zhmara 99 danra


#        ((0, 1) , (0,1))       #secound
#        (  0    ,   1  )       #first
nested = ((1, 2), (3, 4))              #توپڵەکان دەتوانن توپڵەکانی تر لەخۆ بگرن.
print(nested[0])           #  (1, 2)
print(nested[0][1])        #  2


# end of tuple



#Range

"""
Range لە پایتۆن چییە؟
جۆری داتاکانی مەودا بەکاردێت بۆ نوێنەرایەتیکردنی زنجیرەیەک لە ژمارەکان. 
بە شێوەیەکی باو لە لوپەکاندا بەکاردەهێنرێت یان لە کاتی کارکردن لەگەڵ دووبارەکردنەوەکان.
"""

my_range = range(6)        # range(stop)
print(my_range)            #  0, 1, 2, 3, 4, 5

my_range_2 = range(2,6)    # range(start, stop)
print(my_range_2)          # 2, 3, 4, 5


my_range_3 = range(1, 10, 2)     #range(start, stop, step)
print(my_range_3)                # 1, 3, 5, 7, 9

my_range_4 = range(10, 1, -2)
print(my_range_4)                # 10, 8, 6, 4, 2


#گۆڕینی Range  بۆ لیست یان tuple

my_range_5= range(6)
print(list(my_range_5))    #  [0, 1, 2, 3, 4, 5]
print(tuple(my_range_5))    #  (0, 1, 2, 3, 4, 5)

# end of Range


#Dictionary

"""
Dictionary لە زمانی پایتۆن چییە؟
فەرهەنگ پێکهاتەیەکی داتاکانی پایتۆنە کە داتاکان بە جووتە بەهای کلیل هەڵدەگرێت.
 هەر کلیلێک تایبەتە، و بەکاردێت بۆ دەستگەیشتن بە بەهای هاوتای خۆی.
 
 فەرهەنگ لە کلیل و بەها پەیوەندیدارەکانیان پێکدێت

"""

my_dict = {"key1": "value1", "key2": "value2"}     #بەکارهێنانی Curly Braces {} بۆ دروستکردنیDictionaries

print (my_dict )                    #{'key1': 'value1', 'key2': 'value2'}

my_dict2= {"name": "layla", "age": 36}
print( my_dict2["name"])               #  layla
print( my_dict2["age"])                # 36


#زیادکردنی Key-Value نوێ

my_dict2["ragaz"] = "me"
print(my_dict2)           #{'name': 'layla', 'age': 36, 'ragaz': 'me'}

#دەستکاری Key-Value

my_dict2["age"] = 37
print(my_dict2)     # {'name': 'layla', 'age': 37, 'ragaz': 'me'}

my_dict2.pop("age")               # لابردنی item
print(my_dict2)                 # {'name': 'layla', 'ragaz': 'me'}


# کلیلێکی دیاریکراو یان تەواوی dictionary دەسڕێتەوە. del

del my_dict2["name"]
print(my_dict2)              #{'ragaz': 'me'}


my_dict3= {"name": "gazhbin", "age": 19}

#تەواوی dictionary دەسڕێتەوە

my_dict3.clear()
print(my_dict3)   #  {}


#end of dictionary



# Set

"""
set 
 بۆ توخمە ناوازەکان و ناڕێکخراوەکان بەکاردێت
 
 سێتەکان بە شێوەیەکی ئۆتۆماتیکی بەها دووبارەبووەکان لا دەبەن،
 
 کۆمەڵەکان پشتگیری لە ئیندێکسکردن، پارچەکردن، یان دەستگەیشتن بە توخمەکان ناکەن
  بە بەکارهێنانی ئیندێکسی ژمارەیی وەک لیستەکان یان توپڵەکان.
  
  دەتوانرێت کۆمەڵەکان دەستکاری بکرێن (element زیاد بکرێت یان لاببرێن)
  
  بەکارهێنانی Curly Braces  {}
  
"""

set_one= {1, 2, 2, 3}          #سێتەکان بە شێوەیەکی ئۆتۆماتیکی بەها دووبارەبووەکان لا دەبەن،
print(set_one)                        #  {1, 2, 3}


set_fruits = {"apple", "banana", "cherry"}
print(set_fruits)                         # {'apple', 'banana', 'cherry'} or {'banana', 'cherry', 'apple'} .... it is random


set_fruits.add("orange")      # زیادکردنیElement بۆ set
print(set_fruits)            #  {'orange', 'banana', 'cherry', 'apple'}


set_fruits.update(["grape", "mango"])   #بەکارهێنانی update()
print(set_fruits)                      #  {'grape', 'orange', 'mango', 'cherry', 'apple', 'banana'}


set_fruits.remove("banana")        #توخمێکی element  دیاریکراو لا دەبات و KeyError نیشان دەدات ئەگەر توخمەکە نەدۆزرایەوە
print(set_fruits)                 # {'grape', 'orange', 'mango', 'cherry', 'apple'}


set_fruits.discard("banana")        #توخمێکی element  دیاریکراو لا دەبات و KeyError نیشان نادات ئەگەر توخمەکە نەدۆزرایەوە
print(set_fruits)                  # {'grape', 'orange', 'mango', 'cherry', 'apple'}

set_fruits.clear()                #هەموو توخمەکان لە کۆمەڵەکە لادەبات
print(set_fruits)                 #  set()


set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "kiwi", "mango"}
anjam = set1.union(set2)                   # بەکاردێت بۆ کۆکردنەوەی توخمەکانی چەندین کۆمەڵە union
print(anjam)                              #{'apple', 'banana', 'cherry', 'kiwi', 'mango'}

anjam_2 = set1.union(set2)            #  intersection بەکاردێت بۆ دۆزینەوەی توخمە باوەکانی نێوان دوو کۆمەڵە یان زیات
print(anjam_2)                        #{'banana', 'cherry', 'apple', 'kiwi', 'mango'}

anjam_3= set1.difference(set2)       # difference بەکاردێت بۆ دۆزینەوەی ئەو توخمانەی کە لە کۆمەڵەیەکدا هەن بەڵام لە کۆمەڵەکانی تردا نین
print(anjam_3)                      # {'cherry', 'apple'}


# end of set



# boolean

"""

جۆری داتاکانی bool ( "boolean") لە پایتۆن یەکێک لە دوو بەها نیشان دەدات: ڕاست یان هەڵە.
 بە شێوەیەکی باو بۆ بڕیاردان و دەربڕینی مەرجدار لە بەرنامەسازیدا بەکاردێت.

True  نوێنەرایەتی بەهای لۆژیکی "بەڵێ" دەکات.
False  نوێنەرایەتی بەهای لۆژیکی "نا" دەکات.

ڕاست و هەڵە دەبێت بە پیتی یەکەمی گەورە بنووسرێت

"""

bool_true=True
print(bool_true)          #True

bool_false=False
print(bool_false)        # False

# I will talk about bool in the condition and operator  part

















