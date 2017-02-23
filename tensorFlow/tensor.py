import tensorflow as tf

hello = tf.constant('hello tensorFlow')

sess = tf.Session()

print sess.run(hello)
