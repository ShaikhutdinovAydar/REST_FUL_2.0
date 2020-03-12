from requests import get, delete, post

print(get('http://localhost:5000/api/v2/users').json())

print(delete('http://localhost:5000/api/v2/users/4').json())

print(post('http://127.0.0.1:5000/api/v2/users', json={'id': 3, 'name': 'Almaz','surname': 'Almazov','email': 'almaz@mail.ru','password': 'test', 'address': 'Almet'}, ).json())

print(get('http://localhost:5000/api/v2/jobs').json())

print(get('http://localhost:5000/api/v2/jobs/1').json())