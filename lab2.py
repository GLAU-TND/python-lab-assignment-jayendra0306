try:
    g= int('gwtt') #value error
    g= '43' + 43    #type error
    obj= 'hello'    
    obj.remove()    #Attribute error

except ValueError as e:
    print('value error',e)

except TypeError as e:
    print('type error',e)


finally:
    print('process complete')
