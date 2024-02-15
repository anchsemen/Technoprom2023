import nltk
import pymorphy2
import openpyxl
import shutil
from nltk.corpus import stopwords
import re

nltk.download('punkt')
nltk.download('stopwords')

source_file = 'result.xlsx'
destination_file = 'text preprocessing.xlsx'
shutil.copy(source_file, destination_file)

workbook = openpyxl.load_workbook(source_file)
sheet = workbook['Sheet']

stop_words = set(stopwords.words('russian'))
morph = pymorphy2.MorphAnalyzer()


def preprocess_text(text):
    if text is not None:
        text = text.lower()
        text = re.sub(r'\W', ' ', text)
        text = re.sub(r'\s+', ' ', text)
        words = text.split()
        lemmatized_words = [morph.parse(word)[0].normal_form for word in words]
        filtered_words = [word for word in lemmatized_words if word not in stop_words]
        return ' '.join(filtered_words)
    return ' '


def process_column(column, column_number):
    for i, cell in enumerate(column, start=1):
        sheet.cell(row=i, column=column_number, value=preprocess_text(cell.value))


columns = ['D', 'E', 'F', 'G']
for idx, column_letter in enumerate(columns, start=4):
    column = sheet[column_letter]
    process_column(column, idx)

workbook.save(destination_file)
workbook.close()
