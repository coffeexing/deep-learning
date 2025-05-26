# A simple AND Gate
# Digital logic is not applicable to a perception

# Perceptron
def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1


print(AND(0, 0))
print(AND(0, 1))
print(AND(1, 0))
print(AND(1, 1))


# Digital logic
# Has no weights and biases
def my_and(x1, x2):
    if x1 == 1 and x2 == 1:
        return 1
    else:
        return 0


print(my_and(0, 0))
print(my_and(0, 1))
print(my_and(1, 0))
print(my_and(1, 1))