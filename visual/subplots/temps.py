import matplotlib.pyplot as plt

def read_data(file_path):
  temps = []
  with open(file_path) as file:
    for line in file:
      temperature = float(line.strip())
      temps.append()
