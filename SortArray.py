'''
  Есть массив операций.
  Необходимо операции отсортировать по дате и сгруппировать их по году, а в качестве 
  значений представить массивы c датами в формате MM-DD.
  Пример результата:
  result = {
    "2017": [
      "07-31",
      "08-22"
    ],
    "2018": [
      "01-01"
      "02-22"
    ]
  }
*/
'''

def sortOperations(operations):
    result = {}
    for i in operations:
        date = i['date']
        if date[:4] not in result:
            result[date[:4]] = []
            result[date[:4]].append(date[5:])
        else:
            result[date[:4]].append(date[5:])
    for key,value in result.items():
        result[key] = sorted(value)
    print(result)


oper = [
    { "date": "2017-07-31", "amount": "5422" },
    { "date": "2017-06-30", "amount": "5220" },
    { "date": "2017-05-31", "amount": "5365" },
    { "date": "2017-08-31", "amount": "5451" },
    { "date": "2017-09-30", "amount": "5303" },
    { "date": "2018-03-31", "amount": "5654" },
    { "date": "2017-10-31", "amount": "5509" },
    { "date": "2017-12-31", "amount": "5567" },
    { "date": "2018-01-31", "amount": "5597" },
    { "date": "2017-11-30", "amount": "5359" },
    { "date": "2018-02-28", "amount": "5082" },
    { "date": "2018-04-14", "amount": "2567" },
    { "date": "2019-04-15", "amount": "2435" }
];

sortOperations(oper)