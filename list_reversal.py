# Reverse a List
input_value = ""
input_list=[]
reversed_list=[]


def reverse_list(list):
    print(f"Original List: {list}" )
    list_length=len(list)
    i=-1
    y=list_length-1
    while i<=y:
      reversed_list.append(list.pop(y))
      y = y - 1
      if i==y:
         break
    print(f"Updated List: {reversed_list}")
  

print("Welcome to List Reversal World")
while input_value != "done":
    input_value = input("Keeping entering , Enter done to start reversal: ")
    if input_value == "done":
       break
    input_list.append(input_value)

print(f"You entered: {input_list}")
reverse_list(input_list)    
