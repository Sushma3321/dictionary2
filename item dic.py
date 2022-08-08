# dic={"name":"sushma","id":100,"branch":"cse"}
# print(dic.items())







a=[{"maths":90,"science":92},{"maths":89,"science":94},{"maths":92,"science":88}] 
sub=input("enter the sub:")
for i in a:
    for j in i:
        if j==sub:
            print(i[j])
       