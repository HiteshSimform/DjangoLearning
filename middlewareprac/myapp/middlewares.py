# Function based view Middleware

def my_function_middleware(get_response):
    print("Initial Middleware Execute")

    def function1(request):
        print("Before")
        response = get_response(request)
        print("After")
        return response
    return function1


class Middleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("Initial Middleware Execute")
    
    def __call__(self, request):
        print("Class Before")
        response = self.get_response(request)
        print("Class After")
        return response
