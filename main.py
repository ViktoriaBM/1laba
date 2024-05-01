from hhru import parseVacancies
from write import writeExcel

def main():
    vacancies = parseVacancies()
    writeExcel(vacancies)

if __name__ == "__main__":
    main()