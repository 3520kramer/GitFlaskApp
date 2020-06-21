size_units = ['Bytes', 'KB', 'MB', 'GB']
def format_size(bytes):
    i = 0
    while bytes >= 1024: # as long as the number of bytes is above 1024 we perform the operation
        bytes /= 1024 # divides the number of bytes and assigns the value to the number of bytes
        # if bytes is still above 1024 we divide again
        i += 1 #increment the counter by one
    f = ('%.2f' % bytes) # rounds the number to two decimals
    #.rstrip('0').rstrip('.') removes the last decimals down to the last zerio if there is one
    return f'{f} {size_units[i]}'

# OLD ONE REALLY BAD
def format_size_(size_in_bytes):
    my_system = [
        (1024 ** 3, ' tb'),
        (1024 ** 2, ' gb'),            
        (1024 ** 1, ' mb'),
        (1024 ** 0, ' bytes')
    ]
    return size(size_in_bytes, system=my_system)