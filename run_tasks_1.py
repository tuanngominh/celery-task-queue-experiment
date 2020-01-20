from celery import group, chain, chord

from tasks import add, mul, xsum

# add.delay(2, 2)
# -> celery.result.AsyncResult

# add.apply_async((3, 3), countdown=10)

# add.signature((2, 2), countdown=10)
# add.s(2, 2)
# -> celery.canvas.Signature

# s1 = add.s(2, 3)
# s1.delay()

# s2 = add.s(2)
# res = s2.delay(8)
# res.get()

# group(add.s(i, i) for i in range(10))().get()

# g = group(add.s(i) for i in range(10))
# g(10).get()


# chain(add.s(4, 4) | mul.s(8))().get()

# g = chain(add.s(4) | mul.s(8))
# g(4).get()


# (add.s(4, 4) | mul.s(9))().get()

# chord((add.s(i, i) for i in range(10)), xsum.s())().get()

# group(
#     (add.s(4, 4) | mul.s(2)), # 16
#     (add.s(5, 4) | mul.s(3)), # 27
#     (add.s(5, 5) | mul.s(4))  # 40
# )()
