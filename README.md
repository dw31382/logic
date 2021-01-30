# demo

>>> import zeroth_order as z
>>> a = z.Prop("Existence exists", True)
>>> b = z.Prop("2 + 2 = 5", False)
>>> print(a.str + " and " + b.str + "?")
Existence exists and 2 + 2 = 5?
>>> print(z.and_(a.val, b.val))
False
