import pandas as pd
import os


def disease_desc(disease):
    print(os.getcwd())
    data = pd.read_csv('app/disease_data/disease_data.csv', sep=";")
    data = data[data['disease'] == disease]
    print(data.description)
    description = data['description'].values[0]
    solution = data['solution'].values[0]
    solution = solution.split('|')
    solution = [f'<li>{sol}</li>' for sol in solution]
    solution = ''.join(solution)
    reference = data['reference'].values[0]
    reference = reference.split('|')
    reference = [f'<li><a href = {ref}> {ref}</a></li>' for ref in reference]
    reference = ''.join(reference)
    return description, solution, reference
