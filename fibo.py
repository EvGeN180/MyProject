class Fibonacci:
    def __init__(self, n):
        self.n = n 
        self.arr = []  

    def generateFibo(self):
        a, b = 0, 1
        for _ in range(self.n):
            self.arr.append(a)
            a, b = b, a + b 

    def displayFibo(self):
        print("Fibonacci array:", self.arr)


fibonacci = Fibonacci(15)
fibonacci.generateFibo()
fibonacci.displayFibo()
