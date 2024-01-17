# pie chart matplotlib
import matplotlib.pyplot as pp

#data
labels = ('ECET', 'CET', 'ESET')
sizes = [30, 50, 20]

pp.pie(sizes, labels=labels, autopct='%1.f%%', counterclock=False, startangle=105)

pp.ylabel('Percentage of Graduates')
pp.xlabel('Class of 2023')

#save chart file
#pp.plotsavefig('piechart.png', dpi=300)
pp.show()