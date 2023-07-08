import requests

class TheBest_Superhero:
    def __init__(self, list_Superhero, comparison_parameters):
        self.list_Superhero = list_Superhero
        self.comparison_parameters = comparison_parameters

    def comparisons(self):
        '''
        Метод скачивает API по информации о супергероях с информацией по всем супергероям.
        На входе получает парметры для сравнения, возвращает кто самыйй (intelligence) из трех супергероев- Hulk, Captain America, Thanos. 
        '''
        
        url = 'https://akabab.github.io/superhero-api/api/all.json'

        result = {}
        
        for lists in requests.get(url).json():
            if lists['name'] in list_Superhero:
                result[lists['name']] = lists['powerstats'][comparison_parameters]
          
        print('Самый умный: ', ', '.join(list(map(lambda x: x[0], filter(lambda x: x[1] == max(result.items(), key=lambda x: x[1])[1], result.items())))))
     

if __name__ == '__main__':
    list_Superhero = ['Thanos', 'Hulk', 'Captain America']
    comparison_parameters = 'intelligence'
    result = TheBest_Superhero(list_Superhero, comparison_parameters)
    result.comparisons()