"""Scenario is we are having 2 numpy array as training data set and we , we want to calculate m & b such
that it is the best possible line, also it can predict the outcomes accurately. At the backend we are
 aware that equation is y=2x+3, where m is 2 and b is 3, but we want the model to predict best m & b or
 best possible line"""
import numpy as np

def gradient_descent(x,y):
    m_curr = b_curr = 0
    # We took some point as a reference and started with it
    iterations = 10000
    n = len(x)
    learning_rate = 0.0002

    # Baby step size we want to take to find out the global minima

    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        add = 0
        print("Value of Add in each iteration",add)
        # we already know y=mx+b
        for val in (y-y_predicted):
            print(val)
            Add1=val**2
            add=add+Add1
            print("Intermediate Add", add)
        print("Final Add",add)
        cost = (1/n) * add
        # cost=(1/n)*sum([val**2 for val in (y-y_predicted)])
        # print("SUM",sum([val**2 for val in (y-y_predicted)]))

        # MSE This is the formula to find  Mean Square error
        md = -(2/n)*sum(x*(y-y_predicted))

        bd = -(2/n)*sum(y-y_predicted)

        # mb and bd are derivatives, mb with respect to m and bd with respect to b
        # The reason we did for both as we are reducing m & b both to find the best possible line
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print ("m {}, b {}, cost {} iteration {}".format(m_curr,b_curr,cost, i))



if __name__=='__main__':
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([5, 7, 9, 11, 13])
    gradient_descent(x,y)