import json
flight_names = ['a','b','c','d']
deps = ['1','2','3','4']
durations = ['10','20','30','40']
studentticketfare = [1,2,3]
count =0
result = {}
result = {
    "rows": []
          }
for i,j,k in zip(flight_names,deps,durations):
    row = {}
    row = {
        'Flight': i,
        'Duration': j,
        'Departure_time': k
}
    count+=1
    if count >len(studentticketfare):
        break
    else:
        result['rows'].append(row)
print(json.dumps(result))
