import tensorflow as tf
import numpy as np
tf.set_random_seed(66)

x_data = np.array([[0,0],[0,1],[1,0],[1,1]], dtype=np.float32)
y_data = np.array([[0],[1],[1],[0]], dtype=np.float32)

x = tf.placeholder(tf.float32, shape=[None, 2])
y = tf.placeholder(tf.float32, shape=[None, 1])

w = tf.Variable(tf.zeros([2, 1]), name='weight')
b = tf.Variable(tf.zeros([1]), name='bias')

hypothesis = tf.sigmoid(tf.matmul(x, w) + b)

# sigmoid cost
loss= -tf.reduce_mean(y * tf.log(hypothesis) + (1 - y) * tf.log(1-hypothesis))
train = tf.train.AdamOptimizer(learning_rate = 0.01).minimize(loss)

predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, y), dtype=tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(5001):
        cost_val, _ = sess.run([loss,train], feed_dict={x:x_data, y:y_data})

        if step % 200 ==0:
            print(step,cost_val)

    h , c, a = sess.run([hypothesis,predicted,accuracy], feed_dict={x:x_data, y:y_data})

    print("predict value :", h, "original value: ", c, "accuracy: ", a)