# Verilən nums=[1,2,3,6,7,8,23,78,34,12]


# 1. Ədədlərin cəmini tapan metod yazın

# nums=[1,2,3,6,7,8,23,78,34,12]
# total=sum(nums)
# print(total)


# 2. Ədədlərin böyükdən kiçiyə doğru sıralayın

# nums=[1,2,3,6,7,8,23,78,34,12] 
# nums.sort(reverse=True)
# print(nums)

# 3. Ədədlər arasında rəqəmlərinin cəmi ən böyük olan ədədi tapın

# nums=[1,2,3,6,7,8,23,78,34,12] 
# print( max(nums))
 
# 4.Ədədlərin kvadratlarının olduğu yeni bir massiv yaradan metod yazın

# nums=[1,2,3,6,7,8,23,78,34,12]
# kvadratlar=[number**2 for number in nums]
# print("ədədlərin kvadratı göstər")
# print(kvadratlar)

# 5.Tək ədədlərin cəmini tapan metod yazın

# nums=[1,2,3,6,7,8,23,78,34,12]
# cem=0

# for num in nums:
#     if num % 2 != 0:
#        print(num," ")
    
#        cem+=num
# print(cem)

        
# 6.Daxilində 3 rəqəmi olan neçə ədəd olduğunu ekrana çap edən metod yazın

# nums=[1,2,3,6,7,8,23,78,34,12]
# for num in nums:
#     if num ==3:
#         print(num)


# 7. Tək ədədləri ayıraraq ayrıca bir massivə yığan metod yazın

nums=[1,2,3,6,7,8,23,78,34,12]
tek_eded=[]
for i in nums :
    if i % 2!=0:
        tek_eded.append(i)
        print(tek_eded)

