import matplotlib.pyplot as plt

data = [['steel', 1.1],
        ['steel', 2.3],
        ['steel', 3.6],
        ['plastic', 2.5],
        ['plastic', 1.3],
        ['plastic', 4.6]]

data_dict = {}
for row in data:
    if row[0] in data_dict.keys():
        data_dict[row[0]].append(row[1])
    else:
        data_dict[row[0]] = [row[1]]

x = [int(i) for i in range(len(data_dict['steel']))]
for name in data_dict.keys():
    plt.plot(x, data_dict[name], label = name)
    
plt.title('fig')
plt.legend()
plt.savefig('result.png')