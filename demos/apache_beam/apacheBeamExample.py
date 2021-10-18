import apache_beam
from apache_beam.io.textio import WriteToText

class Split(apache_beam.DoFn):
    
    def process(self, element):
        """
        Splits each row on commas and returns a dictionary representing the
        row
        """
        country, duration, user = element.split(",")

        return [{
            'country': country,
            'duration': float(duration),
            'user': user
        }]

#spliter = Split()
#pcollection = spliter.process("United States Of America,0.5,John Doe")

myText = apache_beam.Create([
    'Bermuda (BM),0.7,Benjamin Sala',
    'Bangladesh (BD),0.3,Chris Batie',
    'Jersey (JE),4.4,Maia Addison',
    'State of Palestine (PS),1.0,Delpha Nevels',
    'Latvia (LV),4.1,Christiana Swaby',
])

output_filename = "./demos/apache_beam/myDemo.txt"

with apache_beam.Pipeline() as p:

    rows = (
        p |
        myText |
        apache_beam.ParDo(Split()) |
        WriteToText(output_filename)
    )

print("All good :)") 

