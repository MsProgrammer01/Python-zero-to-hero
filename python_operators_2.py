
"""
لە پایتۆندا ئۆپەراتۆرەکان هێمای تایبەتن کە بۆ ئەنجامدانی ئۆپەراسیۆنەکان لەسەر گۆڕاوەکان و بەهاکان بەکاردەهێنرێن.
پایتۆن جۆرەها ئۆپەراتۆر دابین دەکات، کە دەتوانرێت بەم شێوەیە پۆلێن بکرێن

 Arithmetic Operators ,  Comparison Operators , Logical Operators , Bitwise Operators
 Identity Operators   ,  Assignment Operators  , Membership Operators
"""


# Arithmetic Operators
#ئەم ئۆپەراتۆرانە بۆ ئەنجامدانی ئۆپەراسیۆنە بنەڕەتییەکانی ژمێریاری بەکاردەهێنرێن

"""
+	Addition	
-	Subtraction	
*	Multiplication	
/	Division 	
//	Floor division 	
%	Modulus 
**	Exponentiation

"""
add=5+3
print (add)          # 8

sub=5-3
print(sub)           # 2

mult=5*3      #جاران
print(mult)         # 15

div=5/2
print(div)          # 2.5

floor=5//2      # , 5 دابەشکردن بەسەر 2دا 2.5 دەدات Floor Division دەگۆڕێت  بۆ نزیکترین ژمارەی تەواو
print (floor)      # 2

moduls= 5%2      # 2 ---> 5  2*2 =4 chandi mawa  ta bgat ba 5 ?  1 dana
print(moduls)     # 1

exp=5**3         # 5 * 5 * 5
print(exp)       # 125



#Comparison Operators
#ئەم ئۆپەراتۆرانە بۆ بەراوردکردنی دوو بەها و گەڕانەوەی بولی (ڕاست یان هەڵە) بەکاردەهێنرێن.

"""
==	Equal to	
!=	Not equal to
>	Greater than
<	Less than	
>=	Greater than or equal to	
<=	Less than or equal to

"""

Equal_1=5
Equal_2=4

print(Equal_1 == Equal_2)     # ئایا ئەوانە یەکسانن؟   False
print(Equal_1 != Equal_2)     # True ئایا ئەوانە یەکسان نین؟
print(Equal_1 > Equal_2)      # True 5 > 4
print(Equal_1 < Equal_2)      # False 5 < 4
print(Equal_1 >= Equal_2)     # True 5 >= 4
print(Equal_1 <= Equal_2)     # False 5 <= 4
print(6 >= 8)                 # False 6 <= 8



#Logical Operators
#ئەم ئۆپەراتۆرانە بۆ تێکەڵکردنی ڕستەی مەرجدار if  و گەڕانەوەی بەهایەکی bool بەکاردەهێنرێن.
"""
and 
True دەگەڕێنێتەوە ئەگەر هەردوو ئۆپەراندەکە ڕاست بن
True and True  -> True
True and False -> False
False and True  -> False
False and False -> False
 
or 
True دەگەڕێنێتەوە ئەگەر لانیکەم یەک ئۆپەراند ڕاست بێت
True and True  -> false
True and False -> true
False and True  -> true
False and False -> true
 
not دۆخی لۆژیکی ئۆپەراندەکەی پێچەوانە دەکاتەوە
true -> false 
false -> true

"""

logic_1 = 10
logic_2= 5
logic_3= 20


anjami_op_1= (logic_1 > logic_2) and (logic_3 > logic_1)
print(anjami_op_1)             #  True (10 > 5 and 20 > 10)

anjami_op_2= (logic_1 > logic_2) and (logic_3 < logic_1)
print(anjami_op_2)              # False (10 > 5  true, 20 < 10  false)



logic_3= 10
logic_4= 5
logic_5= 20

anjami_op_3 = (logic_3 > logic_4) or (logic_5 < logic_3)
print(anjami_op_3)  # True (10 > 5  true,  20 < 10  false)

anjami_op_4 = (logic_3 < logic_4) or (logic_5 < logic_3)
print(anjami_op_4)  #  False


logic_6= 10
logic_7= 5

anjami_op_5 = not (logic_6 > logic_7)
print(anjami_op_5)  #  False  (10 > 5  True )

anjami_op_6 = not (logic_6 < logic_7)
print(anjami_op_6)  # True ( 10 < 5 False )



logic_8= 10
logic_9 = 5
logic_10= 20


anjami_op_7 = (logic_8 > logic_9) and (logic_10 < logic_8 or logic_8 == 10) and not (logic_8 == logic_9) # ! (10 <5) or (10 > 5 and 20==20)
print(anjami_op_7)  #  True  (هەموو مەرجەکان ڕاستن)


anjami_op_7 = not (logic_8 < logic_9) or (logic_8 > logic_9 and logic_10 == 20)    # ! (10 <5) or (10 > 5 and 20==20)
print(anjami_op_7)  #  True




# Assignment Operators
# ئەم ئۆپەراتۆرانە بەکاردەهێنرێن بۆ تەرخانکردنی بەهاکان بۆ گۆڕاوەکان.

"""
=	Simple assignment	
+=	Add and assign	
-=	Subtract and assign
*=	Multiply and assign	
/=	Divide and assign	
//=	Floor divide and assign	
%=	Modulus and assign	
**=	Exponentiate and assign

"""

num_1 = 5
num_1 += 3    #  num_1 = num_1 + 3
print(num_1)    # 8

num_1 = 5
num_1 -= 3    #  num_1 = num_1 - 3
print(num_1)    # 2

num_1 = 5
num_1 *= 3    #  num_1 = num_1 * 3
print(num_1)    # 15

num_1 = 5
num_1 /= 3    #  num_1 = num_1 / 3
print(num_1)    # 1.6666666666666667

num_1 = 5
num_1 //= 3    #  num_1 = num_1 // 3
print(num_1)    # 1


num_1 = 5
num_1 %= 3    #  num_1 = num_1 % 3
print(num_1)    # 2

num_1 = 5
num_1 **= 3    #  num_1 = num_1 ** 3
print(num_1)    # 125




# Identity Operators

"""
لە پایتۆندا ئۆپەراتۆری ناسنامە بەکاردەهێنرێت بۆ ئەوەی بزانرێت ئایا دوو گۆڕاو ئاماژە بە هەمان شت دەکەن لە بیرگەدا.
 ئەم ئۆپەراتۆرانە بەکارناهێنرێن بۆ پشکنینی ئەوەی کە ئایا بەهاکانی گۆڕاوەکان یەکسانن یان نا،
  بەڵکو زیاتر ئاماژە بە هەمان شوێن دەکەن لە بیرگەدا یان نا.

"""

my_x = [1, 2, 3]
my_y = my_x
my_z = [1, 2, 3]

print(my_x is my_y)  #  True
print(my_x is my_z)  #  False

print(my_x == my_z)    #  True

print(my_x is not my_y)  # False
print(my_x is not my_z)  # True




# Membership Operators
#ئەم ئۆپەراتۆرانە بەکاردەهێنرێن بۆ پشکنینی ئەوەی کە ئایا بەهایەک لە زنجیرەیەکدا دۆزراوەتەوە یان نا (لیستی، توپڵ،  و هتد).

"""
 بەکاردەهێنرێن بۆ تاقیکردنەوەی ئەوەی کە ئایا بەهایەک لە زنجیرەیەک یان کۆمەڵێکدا ئامادەیە یان نا.
 ئەم ئۆپەراتۆرانە بە شێوەیەکی سەرەکی بۆ پشکنینی ئەوەی کە ئایا توخمێک لە ڕستە،
  لیست، توپڵ، کۆمەڵە، یان فەرهەنگەکاندا هەیە (یان بوونی نییە) بەکاردەهێنرێن.

in
not in 

in
ئۆپەراتۆری in پشکنین دەکات کە ئایا بەهایەک لە ناو زنجیرەیەک یان کۆمەڵەیەکدا بوونی هەیە یان نا.
 ئەگەر بەهاکە دۆزرایەوە، ئەوا True دەگەڕێنێتەوە؛ ئەگەرنا، False دەگەڕێنێتەوە.
 
"""

my_in= "apple"
print("a" in my_in)  #  True
print("z" in my_in)  #  False

fruits_in = ["apple", "banana", "cherry"]
print("apple" in fruits_in)           #  True
print("orange" in fruits_in)          #  False


colors_notin = {"red", "blue", "green"}
print("yellow" not in colors_notin)     #  True
print("blue" not in colors_notin)       # False

print("R" in "programming")  #  False

nested_list_in = [[1, 2], [3, 4], [5, 6]]
print([1, 2] in nested_list_in)  #  True
print(1 in nested_list_in)       #  False


#Bitwise Operators
#ئەم ئۆپەراتۆرانە بۆ ئەنجامدانی ئۆپەراسیۆنەکان لەسەر ژمارە دووانەییەکان لە ئاستی بیتەکاندا بەکاردەهێنرێن.


"""
ئۆپەراتۆرەکانی بیتوایەز لەسەر ژمارەکان لە ئاستی دووانەییدا کاردەکەن.
 لەبری ئەوەی کار لەگەڵ نوێنەرایەتی دەهەمی (بنەمای ١٠) ژمارەکان بکەن،
  دەستکاری بیتەکانی (ژمارە دووانەییەکان: ٠ یان ١) ژمارە تەواوەکان دەکەن.
   
"""

binary_1= 5       # Binary: 0101
binary_2= 3       # Binary: 0011
my_result = binary_1 & binary_2  # Binary: 0001
print(my_result)             #  1

"""

Bit of 5	Bit of 3 	Result
0	          0	            0    
1	          1         	0
0	          1	            0
1	          1	            1   = result = 0001 = 1


"""

binary_3= 5       # Binary: 0101
binary_4= 3       # Binary: 0011
my_result_2 = binary_3 & binary_4  # Binary: 0001
print(my_result_2)             #  7


"""

Bit of 5	Bit of 3 	Result
0	          0	            1    
1	          1         	1
0	          1	            1
1	          1	            0   = result = 0111 = 7

"""


binary_5= 5       # Binary: 0101
binary_6= 3       # Binary: 0011
my_result_3 = binary_5 & binary_6
print(my_result_3)             #  6


"""

Bit of 5	Bit of 3 	Result
0	          0	            0    
1	          1         	1
0	          1	            1
1	          1	            0   = result = 0110 = 6

"""

binary_7= 5       # Binary: 0101

my_result_4 = ~ binary_7
print(my_result_4)       # -(0101 + 1) = -0110 =-6



binary_8= 5       # Binary: 0101
my_result_5 = binary_8 << 1  #  یەک 0 زیاد دەکات بۆ ڕاست
print(my_result_5)   #  10           0101 → 1010


binary_9= 5       # Binary: 0101
my_result_6 = binary_9 >> 1  # لابردنی یەک 0 زیاد دەکات بۆ ڕاست
print(my_result_6)   #  2           0101 → 0010


list_1=[12,3]
list_2=[3,5]
print(list_1+list_2)    # [12, 3, 3, 5]
































