from cgi import parse_qs
from template import html


def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    first_num = d.get("first_num", [''])[0]
    second_num = d.get("second_num", [''])[0]
    sum = 0
    mul = 0
    msg = ""
    
    

    
    if first_num.isdigit() == False or second_num.isdigit() == False:
        sum = ""
        mul = ""
        msg = "You can't input string"
    
    else:
        
        if '' not in [first_num, second_num]:
            
            if first_num.isdigit() == False or second_num.isdigit() == False:

                sum = ""
                mul = ""
                msg = "You can't input string"
                
                
                
            else:    
                first_num, second_num = int(first_num) , int(second_num)
                sum = first_num + second_num
                mul = first_num * second_num
        
        elif '' in [first_num, second_num]:
            
            if first_num.isdigit() == False or second_num.isdigit() == False:
                sum,mul,msg="","","You can't input string"
            
            else: 
                
                sum = ""
                mul = ""
                msg = "Please input number"


    response_body = html % {'sum':sum , 'mul':mul, 'msg':msg}
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body]

