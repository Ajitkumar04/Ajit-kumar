def process_scores(student):
  result ={}
  for name,marks in student.items():
    total = sum(marks)
    average = round(total/len(marks),2)
    result[name]=average

  return result
name ={"ajit"[80,90,70]}
process_scores(name)