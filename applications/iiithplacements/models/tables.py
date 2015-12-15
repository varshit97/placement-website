db.define_table('Placements',Field('student_name'),Field('companies'),Field('year_of_placement'),auth.signature)

db.define_table('Recruiters',Field('starting_with'),Field('name_of_company'),auth.signature)

db.define_table('Profile_for_others_to_see',Field('student_name','string',requires=IS_MATCH('[^0-9]',error_message='No numbers in name!!')),Field('father_name',requires=IS_MATCH('[^0-9]',error_message='No numbers in names!!')),Field('mother_name',requires=IS_MATCH('[^0-9]',error_message='No numbers in names!!')),Field('e_mail',requires=IS_EMAIL(error_message='Enter a valid e-mail!!')),Field('phone_number',requires=IS_MATCH('[^a-zA-Z]',error_message='Not a valid phone number')),Field('profile_picture','upload',requires=IS_IMAGE(error_message='Upload an image!!')),Field('coding_skills',requires=IS_NOT_EMPTY(error_message='You must be having at least one skill :) !!')),Field('academic_qualifications','list:string',requires=IS_NOT_EMPTY()),Field('other_interests','text'))

db.define_table('Registered_recruiters',Field('Name_of_company',requires=IS_NOT_EMPTY(error_message='Check out name is empty!!')),Field('Total_people_wanted',requires=IS_MATCH('[^a-zA-Z]',error_message='Give a correct number!!')),Field('e_mail',requires=IS_EMAIL(error_message='Enter a valid e-mail!!')))

db.define_table('msg_to_rec',Field('messaged_by'),Field('messaged_to',requires=IS_NOT_EMPTY()),Field('message_is','text',requires=IS_NOT_EMPTY()))

db.define_table('msg_to_stud',Field('name_of_student',requires=IS_NOT_EMPTY()),Field('messaged_by'),Field('message_is','text'))
