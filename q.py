a= input('atomic number:')

def check_greater():
    global l
    global n
    global stored_l
    global stored_n
    global ml
    global ms
    global Sum
    if Sum > a:
        ms = -1 *1.0/2
        iter_ml()
        ms = 1.0/2
        iter_ml()
            
def iter_ml():
    global l
    global n
    global stored_l
    global stored_n
    global ml
    global ms
    global Sum
    ml = l
    while(ml >= l * -1):
        check_equal()
        ml -= 1

def check_equal():
    global l
    global n
    global stored_l
    global stored_n
    global ml
    global ms
    global Sum
    if(Sum == a):
        print '' + str(n) + ' '+ str(l)+ ' ' + str(ml) + ' '+ str(ms)
        
def go_diagonal():
    global l
    global n
    global stored_l
    global stored_n
    global ml
    global ms
    global Sum
    if(l-1 > 0):
        n += 1
        l -= 1
        Sum += (l*2 - 1)*2
        save_ln()
        check_greater()
    else:
        restore_ln()
        go_right()

def go_right():
    global l
    global n
    global stored_l
    global stored_n
    global ml
    global ms
    global Sum
    if (l+1 <= n):
        l += 1
        Sum += (l*2 - 1)*2
        save_ln()
        check_greater()
    else:
        go_next_row()

def go_next_row():
    global l
    global n
    global stored_l
    global stored_n
    global ml
    global ms
    global Sum
    n += 1
    l = 1
    if(n - 2 > 0):
        l += n - 2
    save_ln()
    Sum += (l*2 - 1)*2
    check_greater()
    
def save_ln():
    global l
    global n
    global stored_l
    global stored_n
    global ml
    global ms
    global Sum
    stored_l = l
    stored_n = n

def restore_ln():
    global l
    global n
    global stored_l
    global stored_n
    global ml
    global ms
    global Sum
    l = stored_l
    n = stored_n


n = 1
l = 1

stored_l = 1
stored_n = 1

ml = 0
ms = 0
Sum = 2


go_diagonal()
