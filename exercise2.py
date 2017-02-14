ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

print "%s's email address is %s" %(ramit['name'], ramit['email'])
print "%s's interest is %s" %(ramit['name'], ramit['interests'][0])
print "%s" % (ramit['friends'][0]['email'])
print "%s" %(ramit['friends'][0]['interests'][1])
