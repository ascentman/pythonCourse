def own_print(x):
	def internal(y):
		print(x, "it's", y)
	return internal

func = own_print('foo')
func('bar')