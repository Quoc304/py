def draw(n):
    for i in range(0, n): 
      
        # inner loop to handle number of columns 
        # values changing acc. to outer loop 
        for j in range(0, i+1): 
          
            # printing stars 
            print("* ",end="") 
       
        # ending line after each row 
        print("\r") 
#draw(10)
def draw_1(n):
    k = 2*n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end = " ")
        k -= 2
        for j in range(0, i+1): 
          
            # printing stars 
            print("* ",end="") 
       
        # ending line after each row 
        print("\r")
#draw_1(10)
def triangle(n):
    # number of spaces 
    k = 2*n - 2
  
    # outer loop to handle number of rows 
    for i in range(0, n): 
      
        # inner loop to handle number spaces 
        # values changing acc. to requirement 
        for j in range(0, k): 
            print(end=" ") 
      
        # decrementing k after each loop 
        k = k - 1
      
        # inner loop to handle number of columns 
        # values changing acc. to outer loop 
        for j in range(0, i+1): 
          
            # printing stars 
            print("* ", end="") 
      
        # ending line after each row 
        print("\r") 
def draw_num(n): 
      
    # initialising starting number  
    num = 1
  
    # outer loop to handle number of rows 
    for i in range(0, n): 
      
        # re assigning num 
        num = 1
      
        # inner loop to handle number of columns 
            # values changing acc. to outer loop 
        for j in range(0, i+1): 
          
                # printing number 
            print(num, end=" ") 
          
            # incrementing number at each column 
            num = num + 1
      
        # ending line after each row 
        print("\r") 
def draw_num_1(n): 
      
    # initializing starting number  
    num = 1
  
    # outer loop to handle number of rows 
    for i in range(0, n): 
      
        # not re assigning num 
        # num = 1 
      
        # inner loop to handle number of columns 
        # values changing acc. to outer loop 
        for j in range(0, i+1): 
          
            # printing number 
            print(num, end=" ") 
          
            # incrementing number at each column 
            num = num + 1
      
        # ending line after each row 
        print("\r")   
def draw_alpha(n): 
      
    # initializing value corresponding to 'A'  
    # ASCII value 
    num = 65
  
    # outer loop to handle number of rows 
    # 5 in this case 
    for i in range(0, n): 
      
        # inner loop to handle number of columns 
        # values changing acc. to outer loop 
        for j in range(0, i+1): 
          
            # explicitely converting to char 
            ch = chr(num) 
          
            # printing char value  
            print(ch, end=" ") 
      
        # incrementing number 
        num = num + 1
      
        # ending line after each row 
        print("\r") 
def  draw_alpha_1(n): 
    # initializing value corresponding to 'A'  
    # ASCII value 
    num = 65
  
    # outer loop to handle number of rows 
    for i in range(0, n): 
      
        # inner loop to handle number of columns 
        # values changing acc. to outer loop 
        for j in range(0, i+1): 
          
            # explicitely converting to char 
            ch = chr(num) 
          
            # printing char value  
            print(ch, end=" ") 
          
            # incrementing at each column 
            num = num +1
      
      
        # ending line after each row 
        print("\r")
