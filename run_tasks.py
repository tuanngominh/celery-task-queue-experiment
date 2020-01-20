from tasks import add

# add.delay(2, 2)
# -> celery.result.AsyncResult

# add.apply_async((3, 3), countdown=10)

# add.signature((2, 2), countdown=10)
# add.s(2, 2)
# -> celery.canvas.Signature

# s1 = add.s(2, 3)
# s1.delay()


s2 = add.s(2)
res = s2.delay(8)
res.get()
