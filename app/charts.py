import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.show()

if __name__ == '__main__':
    labels = ['Kratos', 'Raph', 'Alucard', 'Hanzo', 'Camus']
    values = [37, 34, 30, 42, 27]
    # generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)