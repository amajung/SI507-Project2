# Define a class Movie that accepts as constructor input one row of the movies_clean.csv file
class Movie():
    def __init__(self, row):
        cells = row.strip().split(',')
        self.title = cells[0]
        self.IMDBrating = cells[14]

    def __str__(self):
        return "{} | {}<br>".format(self.title, self.IMDBrating)
