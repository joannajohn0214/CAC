def quiz_results(user_answers):
  major = user_answers['major']
  environment = user_answers['environment']
  size = user_answers['size']
  # price = user_answers['price']
  student_body = user_answers['student_body']

  #1
  if major.lower() == 'q1a1' and environment.lower() == 'q2a2' and size.lower() == 'q3a3' and student_body.lower() == 'q4a4':
    return "You should consider Appalachian State University, West Carolina University, and UNC Wilmington !"
  #2
  elif major.lower() == 'q1a2' and environment.lower() == 'q2a1' and size.lower() == 'q3a3' and student_body.lower() == 'q4a4':
    return "You should consider East Carolina University, UNC Greensboro, Winston-Salem State University, and North Carolina A&T State University!"
  #3
  elif major.lower() == 'q1a3' and environment.lower() == 'q2a1' and size.lower() == 'q3a2' and student_body.lower() == 'q4a4':
    return "You should consider North Carolina State University, North Carolina Central University, UNC Chapel Hill, and UNC Charlotte."
  #4
  elif major.lower() == 'q1a1' and environment.lower() == 'q2a3' and size.lower() == 'q3a2' and student_body.lower() == 'q4a4':
    return "You should consider North Carolina School of the Arts, UNC Pembroke, Fayetteville State University, Elizabeth City State University!"
#5
  elif major.lower() == 'q1a2' and environment.lower() == 'q2a3' and size.lower() == 'q3a1' and student_body.lower() == 'q4a4':
    return "You should consider Appalachian State University, West Carolina University, and UNC Asheville, and UNC Wilmington !"
#6
  elif major.lower() == 'q1a3' and environment.lower() == 'q2a2' and size.lower() == 'q3a1' and student_body.lower() == 'q4a4':
    return "You should consider Appalachian State University, West Carolina University, and UNC Asheville, and UNC Wilmington !"
#7
  elif major.lower() == 'q1a4' and environment.lower() == 'q2a2' and size.lower() == 'q3a1' and student_body.lower() == 'q4a3':
    return "You should consider Appalachian State University, West Carolina University, and UNC Asheville, and UNC Wilmington !"
#8
  elif major.lower() == 'q1a2' and environment.lower() == 'q2a4' and size.lower() == 'q3a1' and student_body.lower() == 'q4a3':
    return "You should consider Appalachian State University, West Carolina University, and UNC Asheville, and UNC Wilmington !"
#9
  elif major.lower() == 'q1a1' and environment.lower() == 'q2a4' and size.lower() == 'q3a2' and student_body.lower() == 'q4a3':
    return "You should consider Appalachian State University, West Carolina University, and UNC Asheville, and UNC Wilmington !"
#10
  elif major.lower() == 'q1a4' and environment.lower() == 'q2a1' and size.lower() == 'q3a2' and student_body.lower() == 'q4a3':
    return "You should consider Appalachian State University, West Carolina University, and UNC Asheville, and UNC Wilmington !"
#11
  elif major.lower() == 'q1a2' and environment.lower() == 'q2a1' and size.lower() == 'q3a4' and student_body.lower() == 'q4a3':
    return "You should consider Appalachian State University, West Carolina University, and UNC Asheville, and UNC Wilmington !"
#12
  elif major.lower() == 'q1a1' and environment.lower() == 'q2a2' and size.lower() == 'q3a4' and student_body.lower() == 'q4a3':
    return "You should consider Appalachian State University, West Carolina University, and UNC Asheville, and UNC Wilmington !"
#13
  elif major.lower() == 'q1a1' and environment.lower() == 'q2a3' and size.lower() == 'q3a4' and student_body.lower() == 'q4a2':
    return "You should consider Appalachian State University, West Carolina University, and UNC Asheville, and UNC Wilmington !"
#14
  elif major.lower() == 'q1a3' and environment.lower() == 'q2a1' and size.lower() == 'q3a4' and student_body.lower() == 'q4a2':
    return "You should consider Appalachian State University, West Carolina University, and UNC Asheville, and UNC Wilmington !"
#15
  elif major.lower() == 'q1a4' and environment.lower() == 'q2a1' and size.lower() == 'q3a3' and student_body.lower() == 'q4a2':
    return "You should consider Appalachian State University, West Carolina University, and UNC Asheville, and UNC Wilmington !"
#16
  elif major.lower() == 'q1a1' and environment.lower() == 'q2a4' and size.lower() == 'q3a3' and student_body.lower() == 'q4a2':
    return "You should consider Appalachian State University, West Carolina University, and UNC Asheville, and UNC Wilmington !"
#17
  elif major.lower() == 'q1a3' and environment.lower() == 'q2a4' and size.lower() == 'q3a1' and student_body.lower() == 'q4a2':
    return "You should consider Appalachian State University, West Carolina University, and UNC Asheville, and UNC Wilmington !"
#18
  elif major.lower() == 'q1a4' and environment.lower() == 'q2a3' and size.lower() == 'q3a1' and student_body.lower() == 'q4a2':
    return "You should consider Appalachian State University, West Carolina University, and UNC Asheville, and UNC Wilmington !"
#19
  elif major.lower() == 'q1a4' and environment.lower() == 'q2a3' and size.lower() == 'q3a2' and student_body.lower() == 'q4a1':
    return "You should consider Appalachian State University, West Carolina University, and UNC Asheville, and UNC Wilmington !"
#20
  elif major.lower() == 'q1a3' and environment.lower() == 'q2a4' and size.lower() == 'q3a2' and student_body.lower() == 'q4a1':
    return "You should consider Appalachian State University, West Carolina University, and UNC Asheville, and UNC Wilmington !"
#21
  elif major.lower() == 'q1a2' and environment.lower() == 'q2a4' and size.lower() == 'q3a3' and student_body.lower() == 'q4a1':
    return "You should consider Appalachian State University, West Carolina University, and UNC Asheville, and UNC Wilmington !"
#22
  elif major.lower() == 'q1a4' and environment.lower() == 'q2a2' and size.lower() == 'q3a3' and student_body.lower() == 'q4a1':
    return "You should consider Appalachian State University, West Carolina University, and UNC Asheville, and UNC Wilmington !"
#23
  elif major.lower() == 'q1a3' and environment.lower() == 'q2a2' and size.lower() == 'q3a4' and student_body.lower() == 'q4a1':
    return "You should consider Appalachian State University, West Carolina University, and UNC Asheville, and UNC Wilmington !"
#24
  elif major.lower() == 'q1a2' and environment.lower() == 'q2a3' and size.lower() == 'q3a4' and student_body.lower() == 'q4a1':
    return "You should consider Appalachian State University, West Carolina University, and UNC Asheville, and UNC Wilmington !"


#Questions: What would you like to study? What environments do you enjoy? What are your preferred class sizes? What is your price range? What is your preferred student body? What else would you like in a school? (Choose one) Anything else? Anything else?