# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

sess =  tf.compat.v1.Session()
node1 = tf.constant(3.0)
node2 = tf.constant(4.0)
node3 = tf.add(node1,node2)
    
print("node1 : ", node1)
print("node2 : ", node2)
print("node3 : ", node3)
    
print("sess.run([node1, node2]) : ", sess.run([node1, node2]))
print("sess.run(node3) : ", sess.run(node3))
# -

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
add_note = a + b
print(sess.run(add_note, feed_dict={a:3, b:4}))
print(sess.run(add_note, feed_dict={a: [1.5, 3.2], b:[5.6, 9.2]}))


