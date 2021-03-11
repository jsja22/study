import tensorflow as tf
import matplotlib.pyplot as plt

x = [1., 2., 3.]
y = [2., 4., 6.]

w = tf.compat.v1.placeholder(tf.float32)

#tensorflow variable이 아니라 ptrhon variable 이기에 initalize 안해줘도 돌아간다!
hypothesis = x*w
cost = tf.reduce_mean(tf.square(hypothesis-y))

w_history = []
cost_history = []

with tf.compat.v1.Session() as sess:
    for i in range(-30, 50):
        curr_w = i *0.1
        curr_cost = sess.run(cost, feed_dict={w:curr_w})

        w_history.append(curr_w)
        cost_history.append(curr_cost)


print(w_history)
print("=====================")
print(cost_history)

plt.plot(w_history, cost_history)
plt.show()

#weight 2 loss lowest