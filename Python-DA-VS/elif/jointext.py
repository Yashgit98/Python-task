def join_text (*args,separator=''):
    return separator.join(args)
t1 = "my"
t2 = "world"

joined_text = join_text(t1,t2, separator='_')
print(joined_text)