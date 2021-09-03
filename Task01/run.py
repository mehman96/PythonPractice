#  1. str daxilində neçə xarakter olduğunu ekrana yazdırın
# txt= 'Proqramalaşdırma nə qədər çox şey bildiyinizlə yox, bildiyinizlə ortaya çıxardığınız işlərlə maraqlanır'

# x=(len(txt))
# print(x)


# 2. str daxilində neçə hərf olduğunu ekrana yazdırın

# herfler = "abcdefghijklmnopqrstuvwxyz"
# txt='Proqramalaşdırma nə qədər çox şey bildiyinizlə yox, bildiyinizlə ortaya çıxardığınız işlərlə maraqlanır'

# for char in herfler:
#   say = txt.count(char)
#   if say > 1:
#     print (char,say)
        

# 3. str daxilindəki sözləri ayrı bir massiv içərisində toplayın

# str='Proqramalaşdırma nə qədər çox şey bildiyinizlə yox, bildiyinizlə ortaya çıxardığınız işlərlə maraqlanır'
# def convert(str):
#     return str([0].split())
#     print(convert(str))




# 4. str daxilində neçə sait və neçə samit olduğunu ekrana çap edin

# samit=' b, q, v, ğ, d, j, z, y, g, c, l, m, n, r ,p, k, f, x, t, ç, s, x, l, ç, h'
# txt='Proqramalaşdırma nə qədər çox şey bildiyinizlə yox, bildiyinizlə ortaya çıxardığınız işlərlə maraqlanır'

# for herf in samit:
#     say = txt.count(herf)   
#     if say > 1:
#         print (herf ,say)

   
# sait=' a, ı, o, u , e, ə , i, ö, ü'
# txt='Proqramalaşdırma nə qədər çox şey bildiyinizlə yox, bildiyinizlə ortaya çıxardığınız işlərlə maraqlanır'
# for herf in sait:
#     say = txt.count(herf)   
#     if say > 1:
#         print (herf , say)
   


#  5. str daxilində son iki sözü silən metod yazın 

# str='Proqramalaşdırma nə qədər çox şey bildiyinizlə yox, bildiyinizlə ortaya çıxardığınız işlərlə maraqlanır'
# tek tek silmek ucun

# print("Cümləni daxil edin: ")
# text = input()

# print("silmek istediyiniz sozu daxil edin: ")
# word = input()

# text = text.replace(word,  "")

# print()
# print(text)


#  2 ci yol kimi her ikisini birden silmek ucun 
# import re
# print(re.sub("işlərlə|maraqlanır", "", "Proqramalaşdırma nə qədər çox şey bildiyinizlə yox, bildiyinizlə ortaya çıxardığınız işlərlə maraqlanır "))



# 6. str ni vergülə görə ayırıb iki string halına gətirin

# str='Proqramalaşdırma nə qədər çox şey bildiyinizlə yox, bildiyinizlə ortaya çıxardığınız işlərlə maraqlanır'
# import re
# x=re.split(',+', str)
# print(x)


# 7. stringSearch(word) adında bir metod yazın. daxil edilən sözün mətnin içində olub olmadığını ekrana çap edən metod yazın

# if 'qədər' in str:
#     print('var')
# else:
#     print('yoxdu')

