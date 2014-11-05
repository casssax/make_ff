import csv
import sys

def fill_zero_length(fields):
    for e in range(len(fields)):
        if fields[e] == 0:
            fields[e] = 10
    return fields

def max_length(data):
    first_flag = 1
    fields = []
    for get_line in data:
        line = list(get_line)
        if first_flag == 1:
            for i in range(len(line)):
                fields.append(len(line[i]))
                first_flag = 0
        else:
            for i in range(len(line)):
                if fields[i] < len(line[i]):
                    fields[i] = len(line[i])
    return fields





def make_fixed_field(input_file,out_file,lay_out):
    print 'This program will convert a delimited file to fixed_field'
    print 'based on the longest value for each field of the file. '
    print '(fields with length of zero will be changed to l0.)'
    get_delim = raw_input("Enter delimiter(enter 't' for tab): ")
    delim_dict = {
                ',':',',
                '|':'|',
                't':'\t',
                'T':'\t'
                }
    delim_type = delim_dict[get_delim]
    data = csv.reader(input_file, delimiter=str(delim_type))
    #data = [row for row in data]
    #max_len = [max(len(str(x)) for x in line) for line in zip(*data)]
    max_len = max_length(data)
    fields = fill_zero_length(max_len)
    print 'layout: ', str(fields)
    lay_out.write(str(fields).replace(" ", "")[1:-1])
    total = 0
    input_file.seek(0)
    data = csv.reader(input_file, delimiter=str(delim_type))
    for get_line in data:
        line = list(get_line)
        total = total + 1
        count = 0
        num_fields = len(line)
        new = ''
        pos = 0
        for field in line:
            try:
                if len(field) > abs(fields[count]):
                    new = new + field[:abs(fields[count])]   #truncataes if field longer than layout (for header records)
                    count = count + 1
                else:
                    if fields[count] < 1:
                        new = new + field.rjust(abs(fields[count]))   #right justify if all digits
                    else:
                        new = new + field.ljust(fields[count])
                    count = count + 1
            except IndexError:
                print line
        out_file.write(new + '\n')
    print 'total records processed: {}'.format(total)

# def strip_suffix(name):  #strip suffix to create output file name w/'.csv'
#     return name[:-4]

# file_ext = '.ff'

# fname = 'newsupps.txt'
# with open(fname, 'r') as input_file, open(strip_suffix(fname) + file_ext, 'w') as out_file:
#                 make_fixed_field(input_file, out_file)



