numbers=[10,13,24,56,99,21]
even_count=0
odd_count=0
for num in numbers:
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1
print("No.of Even Numbers",even_count)
print("No.of Odd Numbers",odd_count)