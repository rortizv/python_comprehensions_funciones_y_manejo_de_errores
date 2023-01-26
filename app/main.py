import mod
import read_csv
import charts

def run():
    data = read_csv.read_csv('./app/data.csv')
    data = list(filter(lambda item: item['Continent'] == 'South America', data))
    countries = list(map(lambda item: item['Country'], data))
    percentages = list(map(lambda item: item['WorldPopulationPercentage'], data))
    charts.generate_pie_chart(countries, percentages)
    '''
    country = input('Type Country => ')
    result = mod.get_population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = mod.get_population(country)
        charts.generate_bar_chart(labels, values)
    '''

if __name__ == '__main__':
    run()