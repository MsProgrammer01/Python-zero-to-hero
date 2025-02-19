

""""
Encapsulation لە پایتۆن چییە؟
کەپسولکردن یەکێکە لە بنەما بنەڕەتییەکانی بەرنامەسازی  (OOP)
. ئاماژەیە بۆ کۆکردنەوەی ئەو داتایانە (attributes) و شێوازەکان (functions) کە لەسەر داتاکان کاردەکەن بۆ یەک یەکە، واتە پۆلێک.
 هەروەها بریتییە لە سنووردارکردنی دەستڕاگەیشتنێکی ڕاستەوخۆ بۆ هەندێک تایبەتمەندی و شێواز بۆ پاراستنی یەکپارچەیی شتەکە.

کەپسولکردن ڕێگە دەدات
شاردنەوەی داتا:  کردنی هەندێک بەش لە ئۆبجێکتی تایبەت بۆ ڕێگریکردن لە دەستکاریکردنی ڕاستەوخۆ لە دەرەوەی پۆلەکەوە..
پاراستنی کۆد:  گۆڕانکاری لە پێکهاتەی ناوخۆیی کاریگەری لەسەر کۆدی دەرەکی نییە.



ncapsulation
پایتۆن سێ ئاستی کۆنترۆڵی دەستگەیشتن دابین دەکات:

1-Public Attributes/Methods
تایبەتمەندییە گشتیەکان/شێوازەکان: لە هەر شوێنێکەوە دەستیان پێدەگات.
بەبێ هیچ پێشگرێک پێناسە کراوە (بۆ نموونە، self.attribute).

2-Protected Attributes/Methods
تایبەتمەندی/شێوازە پارێزراوەکان: لەناو پۆلەکە و ژێرپۆلەکانیدا دەستیان پێدەگات.
بە یەک هێڵی ژێرەوە پێناسە کراوە (بۆ نموونە، self._attribute).

3-Private Attributes/Methods
تایبەتمەندی/شێوازە تایبەتەکان: تەنها لەناو پۆلەکەدا دەستدەکەوێت (name mangling بەکاردێت).
بە دوو هێڵی ژێرەوە پێناسە کراوە (بۆ نموونە، self.__attribute).

"""




class Employee:
    def __init__(self, name, salary):    # method
        self.name = name   # Public attribute
        self.__salary = salary   # Private attribute (Encapsulation)


    def get_salary(self):       # شێوازی Getter بۆ دەستگەیشتن بە تایبەتمەندی تایبەت (private attribute)
        return self.__salary

    
    def set_salary(self, new_salary):   #  شێوازی Setter بۆ دەستکاریکردنی تایبەتمەندی تایبە( attribute prive)
        if new_salary > 0:
            self.__salary = new_salary
            print(f" mocha dabeta : {self.__salary}")
        else:
            print("مووچەی نابەجێ! مووچە دەبێت ئەرێنی بێت.")


if __name__ == "__main__":

    emp = Employee("firdaws", 50)

    print(emp.name)  # Output: firdaws
    print("مووچەی ئێستا:", emp.get_salary())  #  مووچەی ئێستا: 50
    emp.set_salary(60)  #  mocha dabeta  60
    print("موچەی نوێکراوە:", emp.get_salary())  # موچەی نوێکراوە : 60

    emp.set_salary(-1000)  # مووچەی نابەجێ! مووچە دەبێت ئەرێنی بێت. yani posetive



