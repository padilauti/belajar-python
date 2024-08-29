'''Type hints untuk fungsi'''

# bentuk standar fungsi yang udah kita pelajari

'''
studi kasus
def fungsi(parameter):
    hasil = parameter**2
    print(hasil)

fungsi(1)
fungsi("Uti")
fungsi(True)
'''

# penggunaan type hints

def fungsi_dengan_hints(argument:int):
    '''FUNGSI DENGAN HINTS'''
    output = 10**argument
    return output

HASIL = fungsi_dengan_hints(2)
print(HASIL)