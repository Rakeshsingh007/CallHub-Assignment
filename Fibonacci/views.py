from django.shortcuts import render
import time

class StatsMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        response = None
        if  hasattr(self, 'process_request'):
            response = self.process_request(request)
            
        response =  self.get_response(request)

        if  hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response

    def process_request(self, request):

        "Store the start time when the request comes in."
        request.start_time = time.time()

    def process_response(self, request, response):
        "Calculate and output the page generation duration"
        # Get the start time from the request and calculate how long
        # the response took.
        duration = time.time() - request.start_time
        response['time'] = int(duration * 1000)
        print(response)
        return response


def Fibonacci(request):
    return render(request,'index.html')


def result(request):
    start_time = time.time()

    num = int(request.GET.get('num'))

    FibArray = [1,1]

    def fibonacci(num):
        if num<=len(FibArray):
            return FibArray[num-1]
        else:
            temp_fib = fibonacci(num-1)+fibonacci(num-2)
            FibArray.append(temp_fib)
            return temp_fib
  
    time_taken = float((time.time() - start_time)*1000)
    result={
    'result':fibonacci(num),
    'time_taken': time_taken
    }

    return render(request,'result.html',result)


