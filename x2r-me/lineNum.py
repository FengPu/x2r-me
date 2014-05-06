import StringIO
st = open("MAD_J.rdf","r").read()
print type(st)
sio = StringIO.StringIO(st.decode('utf-8'))
lookup = 'http://140.109.21.188/facilities#store2'


def get_lines(sio, lookup):   
    sio.seek(0)         
    nums = []
    for num, line in enumerate(sio, 1):
        if lookup in line:
            nums.append(str(num))
    return ','.join(nums)

print get_lines(sio, lookup)
print "---"
print get_lines(sio, "http://140.109.21.188/facilities#store85")
print "---"
print get_lines(sio, "http://140.109.21.188/facilities#store8\"")