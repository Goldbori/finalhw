from cgi import parse_qs
from template import html
import MyError as e

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    first_num = d.get("first_num", [''])[0]
    second_num = d.get("second_num", [''])[0]
    sum = 0
    mul = 0
    try:
        
        if first_num.isdigit() == False or second_num.isdigit() == False:
            raise e.StrError("You can't input string")

        if '' not in [first_num, second_num]:
            first_num, second_num = int(first_num) , int(second_num)
            sum = first_num + second_num
            mul = first_num * second_num
        elif '' in [first_num, second_num]:
            sum = "Please input"
            mul = "number"
            sum, mul = str(sum), str(mul)
    except e.StrError:
        sum = e.StrError
        mul = ''
        sum = str(sum)
        mul = str(mul)
    
    response_body = html % {'sum':sum , 'mul':mul}
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body]

